import yaml
from common.tools import get_project_path, sep


class GetConf:
    def __init__(self):
        project_path = get_project_path()
        with open(project_path + sep(["config", "environment.yaml"], add_sep_before=True), "r") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)

    def get_username_password(self, user):
        return self.env["user"][user]["username"], self.env["user"][user]["password"]

    def get_url(self):
        """
        测试地址
        :return:
        """
        return self.env["url"]

    def get_mysql_config(self):
        return self.env["mysql"]


if __name__ == '__main__':
    # print(GetConf().get_username_password("jay"))
    print(GetConf().get_url())
