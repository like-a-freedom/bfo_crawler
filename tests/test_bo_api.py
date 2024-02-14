import bo_api

bo_exist_inns = [7710668349]
bfo_non_exist_org_ids = [77362278855]

bfo_exist_ids = [4878266]
bfo_non_exist_ids = [0000000]


class TestApi:
    def test_search_org(self):
        result = bo_api.search_org(bo_exist_inns[0])
        assert isinstance(result, dict)

    def test_get_org_bfo_details(self):
        result = bo_api.get_org_bfo_details(bfo_exist_ids[0])
        assert isinstance(result, list)

    def test_get_org_summary(self):
        result = bo_api.get_org_summary(bfo_exist_ids[0])
        assert isinstance(result, dict)

    def test_get_bo_statistics(self):
        result = bo_api.get_bo_statistics()
        assert isinstance(result, dict)
