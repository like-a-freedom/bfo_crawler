from typing import Any, Dict, List
from bfo_crawler.functions import *
from bfo_crawler.excel_parser import FinStatements
from bfo_crawler.downloader import download_excel_from_nalog
from bfo_crawler.models.finance_model import FinanceResultsModel

YEARS: List[int] = [2021, 2020]


def get_org_financial_details(org_info: Dict[str, Any]) -> Dict[str, Any]:
    try:
        fin = FinStatements(download_excel_from_nalog(org_info["bfo_id"]))
    except Exception as e:
        raise Exception(f"Unable to download or read xlsx file: {e}")

    results = []

    for year in YEARS:
        try:
            results.append(
                {
                    year: FinanceResultsModel(
                        revenue=calculate_revenue(fin, year),
                        income=calculate_income(fin, year),
                        revenue_growth_yoy=calculate_revenue_growth_yoy(fin, year)
                        if year is not YEARS[-1]
                        else None,
                        profit_margin=calculate_profit_margin(fin, year),
                        ebit_margin=calculate_ebit_margin(fin, year),
                        sales_margin=calculate_sales_margin(fin, year),
                        gross_margin=calculate_gross_margin(fin, year),
                        roe=calculate_roe(fin, year) if year is not YEARS[-1] else None,
                    ).dict()
                }
            )
        except Exception as e:
            print(f"{org_info['bfo_id']}: {e}")

        org_info.update({"results": results})

    return org_info
