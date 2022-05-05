from bfo_crawler.scraper import get_bfo_org_ids

inns = [7729058675, 7736227885, 7801003920]
bfo_org_ids = [7136976, 7152470, None]


class TestBfoScraper:
    def test_bfo_scraper(self):
        result = get_bfo_org_ids(inns)
        assert result[0]["bfo_id"] == bfo_org_ids[0]
        assert result[1]["bfo_id"] == bfo_org_ids[1]
        assert result[2]["bfo_id"] == bfo_org_ids[2]
