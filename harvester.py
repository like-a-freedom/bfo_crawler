import re
import db
import formulas
import bo_api as api
import pandas as pd
from typing import Dict, List, Union
from uuid import uuid4
from datetime import datetime
from models.org_model import Organization, Financials

HTML_TAG_REGEX = re.compile(r"<[^>]+>")
ORG_DATA_FILE: str = "./data/ru_cybersecurity_market_companies.csv"


def _remove_html_tags(string: str) -> str:
    return HTML_TAG_REGEX.sub("", string)


def get_bfo_id(inn: int) -> int | None:
    response = api.search_org(inn)

    if len(response["content"]) > 0:
        return int(response.get("content", None)[0].get("id", None))
    else:
        return None


def parse_bfo_data(inn: int, data: List[Dict]) -> List[Financials]:
    """
    Parse and calculate financial
    results over past years
    """
    bfo_data = []
    for item in data:
        bfo_data.append(
            Financials(
                id=uuid4().hex,
                inn=inn,
                revenue=int(
                    item.get("corrections", [{}])[0]
                    .get("financialResult", {})
                    .get("current2110", 0)
                    * 1000
                    or 0
                ),
                income=int(
                    item.get("corrections", [{}])[0]
                    .get("financialResult", {})
                    .get("previous2400", 0)
                    * 1000
                    or 0
                ),
                revenue_growth_yoy=formulas.calculate_revenue_growth_yoy(
                    int(
                        item.get("corrections", [{}])[0]
                        .get("financialResult", {})
                        .get("current2110", 0)
                        or 0
                    ),
                    int(
                        item.get("corrections", [{}])[0]
                        .get("financialResult", {})
                        .get("previous2110", 0)
                        or 0
                    ),
                ),
                profit_margin=formulas.calculate_profit_margin(
                    item.get("corrections", [{}])[0]
                    .get("financialResult", {})
                    .get("current2400", 0)
                    or 0,
                    item.get("corrections", [{}])[0]
                    .get("financialResult", {})
                    .get("current2110", 0)
                    or 0,
                ),
                ebit_margin=formulas.calculate_ebit_margin(
                    int(
                        item.get("corrections", [{}])[0]
                        .get("financialResult", {})
                        .get("current2300", 0)
                        or 0
                    ),
                    int(
                        item.get("corrections", [{}])[0]
                        .get("financialResult", {})
                        .get("current2110", 0)
                        or 0
                    ),
                ),
                sales_margin=formulas.calculate_sales_margin(
                    int(
                        item.get("corrections", [{}])[0]
                        .get("financialResult", {})
                        .get("current2200", 0)
                        or 0
                    ),
                    int(
                        item.get("corrections", [{}])[0]
                        .get("financialResult", {})
                        .get("current2110", 0)
                        or 0
                    ),
                ),
                gross_margin=formulas.calculate_gross_margin(
                    int(
                        item.get("corrections", [{}])[0]
                        .get("financialResult", {})
                        .get("current2100", 0)
                        or 0
                    ),
                    int(
                        item.get("corrections", [{}])[0]
                        .get("financialResult", {})
                        .get("current2110", 0)
                        or 0
                    ),
                ),
                roe=formulas.calculate_roe(
                    int(
                        item.get("corrections", [{}])[0]
                        .get("financialResult", {})
                        .get("current2400", 0)
                        or 0
                    ),
                    int(
                        item.get("corrections", [{}])[0]
                        .get("balance", {})
                        .get("current1300", 0)
                        or 0
                    ),
                    int(
                        item.get("corrections", [{}])[0]
                        .get("balance", {})
                        .get("previous1300", 0)
                        or 0
                    ),
                ),
                created_at=str(datetime.now()),
                updated_at=None,
                year=int(item.get("period", None)),
            )
        )
    return bfo_data


def get_finance_details(inn: int, bfo_id=None) -> Union[Organization, None]:
    if inn and bfo_id:
        raise ValueError("Only one of inn or bfo_id can be provided")
    elif inn:
        bfo_id = get_bfo_id(inn)

    if bfo_id:
        response = api.get_organization_bfo_details(bfo_id)
        org_finance_results = parse_bfo_data(inn, response)

        org_id = uuid4().hex

        org_data = Organization(
            id=org_id,
            inn=int(response[0].get("organizationInfo", None).get("inn", None)),
            bfo_id=bfo_id,
            name=None,
            tags=[],
            business_type=None,  # json.dumps(["mssp", "integrator"]),
            legal_name=response[0].get("organizationInfo", None).get("fullName", None),
            results=org_finance_results,
        )
        return org_data
    else:
        print(f"[SKIPPED] Organization with INN: {inn} not found in BFO")
        return None


def _get_source_data() -> pd.DataFrame:
    return pd.read_csv(ORG_DATA_FILE).fillna("")


def load_data_into_db():
    data = _get_source_data()

    for row in data.to_dict("records"):
        print(f"Processing {row['org_name']}, INN: {int(row["inn"])}...")
        org_data = get_finance_details(int(row["inn"]))
        if org_data:
            org_data.name = row["org_name"]
            org_data.tags = (
                [
                    db.get_or_create_tag(tag_name)
                    for tag_name in list(set(row["tags"].split(", ")))
                ]
                if row["tags"]
                else []
            )
            org_data.business_type = row["org_type"]
            db.insert(org_data)


load_data_into_db()
