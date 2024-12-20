import os
import pytest
import json

from urllib3 import encode_multipart_formdata

from common.common_requests import Requests
from common.login import login
from common.mysql_operate import MysqlOperate
from common.tools import sep, get_project_path


@pytest.fixture()
def token():
    def _token(user):
        # 判断存放token的目录是否存在，不存在则自动创建
        token_json_dir = sep([get_project_path(), "token_dir"])
        if not os.path.exists(token_json_dir):
            os.mkdir(token_json_dir)
        # 用户user对应的token的json文件
        token_json_path = sep([token_json_dir, user + "_token.json"])
        if not os.path.exists(token_json_path):
            # 文件不存在，调用登录接口，并把token写入json文件
            print(f"{user}对应的token的json文件不存在，调用登录接口")
            token = login(user).json()["data"]["access_token"]
            print(f"写入{user}对应的token的json文件")
            with open(token_json_path, "w+") as write_token:
                write_token.write(json.dumps({"token": token}))
            return token
        else:
            # 文件存在，则取出token的值
            print(f"{user}对应的token的json文件已存在，读取json文件中的token")
            with open(token_json_path, "r") as token_info:
                token = json.loads(token_info.read())
                return token["token"]

    return _token


@pytest.fixture()
def upload_img():
    def _upload_img(img_path, token):
        file_data = {"file": ("upload_img", open(img_path, "rb").read())}
        encode_data = encode_multipart_formdata(file_data)
        # print(encode_data)
        data = encode_data[0]
        headers = {"authorization": f"Bearer {token}", "Content-Type": encode_data[1]}
        res = Requests(headers).post("/operate_platform/v1/aliYun/uploadFile", data=data)
        print(res.json())
        return res.json()['data']

    return _upload_img


@pytest.fixture()
def get_data_from_db():
    def _get_data_from_db(sql):
        res = MysqlOperate().query(sql)
        return res

    return _get_data_from_db
