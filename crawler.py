from tinydb import TinyDB, Query

from bfo_crawler.scraper import get_bfo_org_ids
from bfo_crawler.process_engine import get_org_financial_details

db = TinyDB("db.json")
table = db.table("organizations")
query = Query()


def get_org_data(inn: int):
    result = table.get(query.inn == inn)

    if result:
        if result["results"]:
            return result  # The data already exists, so return it
        else:
            # In case if we have org inn and bfo_id in db
            # then let's enrich it with finance data
            print("Org finance data not found, start quering bo.nalog.ru")
            if result["bfo_id"]:
                return table.upsert(
                    {"results": get_org_financial_details(result)["results"]},
                    query.inn == inn,
                )
            else:
                print("Org not found on bo.nalog.ru, skipping...")
                return result
    else:
        # In case if we have not inn or bfo_id so then
        # let's try to grab the data from bo.nalog.ru
        org_data = get_bfo_org_ids([inn])  # Let's scrape org id from bo.nalog.ru
        if org_data:
            if org_data[0]["bfo_id"]:
                print("Org data not found, start quering bo.nalog.ru")
                org_finance_data = get_org_financial_details(org_data[0])
                org_data[0].update(org_finance_data)
                table.insert(org_data[0])
                return org_data[0]
            else:
                print("Org not found on bo.nalog.ru, skipping...")
                table.insert(org_data[0])
                return org_data
