import pytest

from common.common_requests import Requests


@pytest.fixture()
def area_dict():
    def _area_dict(headers):
        """
        获取片区列表数据，提取里面的id
        :param headers:
        :return: 片区id的数组
        """
        res = Requests(headers).get("/operate_platform/v1/station/queryRegionList?pageNo=1&pageSize=99999")
        area_list = res.json()['data']['data']
        array = []
        for item in area_list:
            array.append(item["id"])
        return array

    return _area_dict
