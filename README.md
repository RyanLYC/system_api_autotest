## 接口自动化测试

`Python + Pytest + Allure 接口自动化测试框架 + Demo + 连接mysql数据验证`

- python
- pytest
- allure 系统中需要安装allure
- ddddocr - 1.4.11 验证码识别
- pytest-assume
- allure-pytest
- PyMySQL 数据断言

## 安装依赖

pip install -r requirements.txt

## 配置

config/environment.yaml

```yaml
user:
  lyc:
    username: username
    password: password

url: your api url


mysql:
  db: 数据库名称
  host: ip地址
  password: 密码
  port: 端口
  user: 用户名


```

## 生成测试报告

```shell
pytest testcases/user/test_user_info.py -s --alluredir=report
# 系统中需要安装allure
allure serve report
```