import httpx


USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
HEADERS = {"User-Agent": USER_AGENT}
HTTP_CLIENT = httpx.Client(
    base_url="https://bo.nalog.ru", headers=HEADERS, timeout=60, follow_redirects=True
)


def api_request(method: str, path: str, params: dict = {}) -> dict:
    """
    Make an API request using the HTTP client instance.

    :param method: HTTP method for the request.
    :param path: API endpoint path.
    :param params: Dictionary of parameters for the request.
    :return: JSON response from the API request.
    """
    try:
        response = HTTP_CLIENT.request(method, path, params=params)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise e


def search_organization(inn: int) -> dict:
    """
    Search for an organization by INN.

    :param inn: The INN of the organization to search for.
    :return: JSON response from the API request.
    """
    return api_request(
        "get", "/advanced-search/organizations/search", {"query": str(inn), "page": "0"}
    )


def get_organization_bfo_details(bfo_id: int) -> dict:
    """
    Get BFO details for an organization.

    :param bfo_id: The ID of the organization.
    :return: JSON response from the API request.
    """
    return api_request("get", f"/nbo/organizations/{bfo_id}/bfo")


def get_organization_summary(bfo_id: int) -> dict:
    """
    Get summary information for an organization.

    :param bfo_id: The ID of the organization.
    :return: JSON response from the API request.
    """
    return api_request("get", f"/nbo/organizations/{bfo_id}")


def get_bo_statistics() -> dict:
    """
    Get statistics for BFO.

    :return: JSON response from the API request.
    """
    return api_request("get", "/nbo/context")
