import allure

from common.common_requests import Requests


# pip install allure-pytest
# 生成测试报告
# pytest testcases/user/test_user_info.py -s --alluredir=report
# allure serve report

class TestUserInfo:
    @allure.description("获取用户信息接口")
    @allure.epic("主页")
    @allure.feature("顶部菜单栏")
    @allure.story("用户信息")
    @allure.tag("用户信息")
    def test_get_user_info(self, token):
        with allure.step("登录"):
            headers = {"authorization": f"Bearer {token('lyc')}"}
        with allure.step("获取用户信息"):
            res = Requests(headers).get("/auth/v1/users/self/info")
            print('res:', res.json())
        with allure.step("断言"):
            assert res.json()["status"] == 0
            assert res.json()["statusText"] == "OK"
