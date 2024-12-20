import random
import time

import allure
from pytest_assume.plugin import assume

from common.common_requests import Requests
from common.tools import get_project_path, sep


# pip install pytest-assume
# pip install allure-pytest
# 生成测试报告
# pytest testcases/user/test_user_info.py -s --alluredir=report
# allure serve report

class TestUserInfo:
    @allure.description("新建场站接口")
    @allure.epic("场站信息管理")
    @allure.feature("新建")
    @allure.story("新建场站")
    @allure.tag("新建场站")
    def test_get_user_info(self, token, upload_img, area_dict, get_data_from_db):
        with allure.step("登录"):
            token_str = token('lyc')
            headers = {"authorization": f"Bearer {token_str}"}
        with allure.step("上传图片"):
            img_path1 = get_project_path() + sep(["img", "station", "1.jpeg"], add_sep_before=True)
            img_url1 = upload_img(img_path1, token_str)
            img_path2 = get_project_path() + sep(["img", "station", "2.jpeg"], add_sep_before=True)
            img_url2 = upload_img(img_path2, token_str)
        with allure.step("获取片区"):
            area_list = area_dict(headers)
            print(area_list)
        with allure.step('新增站点'):
            time_stamp = round(time.time() * 1000)
            station_name = "测试-" + str(time_stamp)  # 时间戳毫秒级别 站名
            data = {
                "address": "广东省******",
                "operationUidList": ["1805849904620654593"],  # 用户id 数组
                "stationName": station_name,
                "regionId": area_list[0],  # 取片区数组的第一个片区
                "organizationId": 109,  # 类似片区  to do ...
                "serviceZoneId": 109,  # 类似片区  to do ...
                "sectionUnitId": 109,  # 类似片区  to do ...
                "operationalTime": time_stamp,  # 当前时间戳
                "picUrls": img_url1 + ',' + img_url2,  # 两张图片URL 拼接
                "longitude": 113.382735 + (random.randint(0, 1) * 2 - 1) * 10,  # 0 - 2之间的随机数 - 1就是 -1 到 1 *10 -10 到 10
                "latitude": 22.557046 + (random.randint(0, 1) * 2 - 1) * 5
            }
            res = Requests(headers).post('/operate_platform/v1/station/addStation', json=data)
        with allure.step("response断言"):
            with assume: assert res.json()["status"] == 0
            with assume: assert res.json()["statusText"] == "OK"
            with assume: assert res.json()["data"]["code"] == 1
        with allure.step("数据库断言"):
            sql = f"select station_name from station where station_name='{station_name}';"
            db_res = get_data_from_db(sql)
            with assume: assert len(db_res) == 1
