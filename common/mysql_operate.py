import pymysql
from pymysql import cursors

from common.yaml_config import GetConf


class MysqlOperate:
    def __init__(self):
        mysql_conf = GetConf().get_mysql_config()
        self.host = mysql_conf["host"]
        self.db = mysql_conf["db"]
        self.port = mysql_conf["port"]
        self.user = mysql_conf["user"]
        self.password = mysql_conf["password"]
        self.conn = None
        self.cur = None

    def __conn_db(self):
        try:
            self.conn = pymysql.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db,
                port=self.port,
                charset="utf8",
                cursorclass=cursors.DictCursor
            )
        except Exception as e:
            print(e)
            return False
        self.cur = self.conn.cursor()
        return True

    def __close_conn(self):
        self.cur.close()
        self.conn.close()
        return True

    def __commit(self):
        self.conn.commit()
        return True

    def query(self, sql):
        print(self.__conn_db())
        self.cur.execute(sql)
        query_data = self.cur.fetchall()
        if query_data == ():
            query_data = None
            print("没有获取到数据")
        else:
            pass
        self.__close_conn()
        return query_data


if __name__ == '__main__':
    sql = "select station_name from station where station_name='测试-1734595408559';"
    db_res = MysqlOperate().query(sql)
    print(db_res)
    print(type(db_res))  # 38897
