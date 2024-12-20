import base64

from common.common_requests import Requests
from common.tools import get_project_path, sep
from common.ocr_identify import OcrIdentify


def save_base64_image(base64_str, output_path):
    # 去掉可能存在的前缀 'data:image/png;base64,' 或类似的部分
    if base64_str.startswith('data:image'):
        base64_str = base64_str.split(',')[1]

    # 将Base64字符串解码
    img_data = base64.b64decode(base64_str)

    # 将解码后的数据写入文件
    with open(output_path, 'wb') as f:
        f.write(img_data)


class TestApi:
    def test_login(self):
        # 图片验证码处理
        valid_res = Requests().get("/auth/v1/uaa/getValidBase64Code")
        valid_dict = valid_res.json()
        # 获取base64字符串
        base64_str = valid_dict['data']['base64']
        validate_key = valid_dict['data']['validateCodeKey']
        path = get_project_path() + sep(["img", "code", "validateCode.png"], add_sep_before=True)
        save_base64_image(base64_str, path)
        identify = OcrIdentify().identify(path)
        data = {
            "username": "zgadmin",
            "password": "Zg8760",
            "validateCode": identify,
            "platform": "operate_platform",
            "validateKey": validate_key
        }
        header = {'x-zg-system': 'operate_platform'}
        res = Requests(header).post("/auth/v1/uaa/loginByPasswordWithCode", json=data)
        print("token的值为:", res.json())
