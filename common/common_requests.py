import requests
from requests.adapters import HTTPAdapter

from common.yaml_config import GetConf
from common.deal_with_response import deal_with_res


class Requests:
    def __init__(self, headers=None, timeout=10):
        """
        requests封装
        :param headers:
        :param timeout:
        """
        self.s = requests.Session()
        # 在session实例上挂载adapter实例，目的就是请求异常时，自动重试
        self.s.mount("http://", HTTPAdapter(max_retries=3))
        self.s.mount("https://", HTTPAdapter(max_retries=3))

        # 公共的请求头设置
        self.s.headers['x-zg-system'] = 'operate_platform'
        self.s.headers.update(headers)
        self.timeout = timeout
        self.url = GetConf().get_url()

    def get(self, url, params=None):
        """
        GET
        :param url: 接口地址
        :param params: 一般GET的参数都是放在URL查询参数里面
        :return:
        """
        res = self.s.get(self.url + url, params=params, timeout=self.timeout)
        deal_with_res(params, res)
        return res

    def post(self, url, data=None, json=None):
        """
        POST
        :param url: 接口地址
        :param data: 参数放在表单中
        :param json: 参数放在请求体重，一般是json
        :return:
        """
        if data:
            res = self.s.post(self.url + url, data=data, timeout=self.timeout)
            deal_with_res(data, res)
            return res
        if json:
            res = self.s.post(self.url + url, json=json, timeout=self.timeout)
            deal_with_res(json, res)
            return res
        res = self.s.post(self.url + url, timeout=self.timeout)
        deal_with_res(json, res)
        return res

    def __del__(self):
        """
        当实例被销毁时，释放掉session所持有的连接
        :return:
        """
        if self.s:
            self.s.close()
