import httpx

USER_AGENT: str = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
HEADERS = {"user-agent": USER_AGENT}

client = httpx.Client(base_url="https://bo.nalog.ru", headers=HEADERS, timeout=60)


def search_org(inn: int):
    try:
        response = client.get(f"/nbo/organizations/search?query={inn}&page=0")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise e


def get_org_bfo_details(bfo_id: int):
    try:
        response = client.get(f"/nbo/organizations/{bfo_id}/bfo/")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise e


def get_org_summary(bfo_id: int):
    try:
        response = client.get(f"/nbo/organizations/{bfo_id}")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise e


def get_bo_statistics():
    try:
        response = client.get("/nbo/context")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise e

