import allure
from urllib3 import encode_multipart_formdata

from common.common_requests import Requests


def upload_img(img_path, token):
    file_data = {"file": ("upload_img", open(img_path, "rb").read())}
    encode_data = encode_multipart_formdata(file_data)
    # print(encode_data)
    data = encode_data[0]
    headers = {"authorization": f"Bearer {token}", "Content-Type": encode_data[1]}
    res = Requests(headers).post("/operate_platform/v1/aliYun/uploadFile", data=data)
    print(res.json())
    return res.json()['data']
