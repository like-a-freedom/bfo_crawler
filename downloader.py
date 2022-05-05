import io
from typing import Dict
import zipfile
import httpx

PERIOD: int = 2021
http_client: httpx.Client = httpx.Client()


def download_excel_from_nalog(bfo_id: int) -> bytes:
    """
    Downloads zipped excel by bfo_id of organization.
    """
    headers: Dict[str, str] = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    url = f"https://bo.nalog.ru/download/bfo/{bfo_id}?auditReport=false&balance=true&capitalChange=true&clarification=false&targetedFundsUsing=false&correctionNumber=0&financialResult=true&fundsMovement=true&type=XLS&period={PERIOD}"

    try:
        downloaded_zip: bytes = http_client.get(
            url, headers=headers, timeout=30
        ).content
    except Exception as e:
        raise Exception(f"An error occured during download excel: {e}")
    try:
        zf: zipfile.ZipFile = zipfile.ZipFile(io.BytesIO(downloaded_zip), "r")
    except Exception as e:
        raise Exception(f"ZIP broken: {e}")

    with zf.open(zf.namelist()[0], "r") as file:
        excelfile: bytes = file.read()
    return excelfile
