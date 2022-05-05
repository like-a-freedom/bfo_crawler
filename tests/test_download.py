from sys import getsizeof
from bfo_crawler.downloader import download_excel_from_nalog

bfo_org_ids = [7136976, 7152470]


class TestDownloader:
    def test_downloader(self):
        for org_id in bfo_org_ids:
            result = download_excel_from_nalog(org_id)
            assert isinstance(result, bytes)
            assert getsizeof(result) > 0
