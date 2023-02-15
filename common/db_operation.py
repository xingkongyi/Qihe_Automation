import pymysql


class DBHandler():
    """数据库操作"""

    def __init__(self, host='10.12.107.159',
                 port=3306, username='root',
                 password='cci_Qihe_@123', db_name='sgup_product',
                 charset='utf8mb4'
                 ):
        # 得到一个连接对象
        self.connection = pymysql.connect(host=host,
                                          port=port,
                                          user=username,
                                          password=password,
                                          database=db_name,
                                          charset=charset)

    def query_one(self, sql):
        """查询一条记录"""
        # 得到游标
        cursor = self.connection.cursor()
        # 提交
        self.connection.commit()
        # 执行
        cursor.execute(sql)
        # 得到执行结果
        data = cursor.fetchone()
        # 关闭游标
        cursor.close()
        return data

    def query_all(self, sql):
        """查询所有的记录"""
        cursor = self.connection.cursor()
        # 提交
        self.connection.commit()

        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        return data

    def close(self):
        self.connection.close()


if __name__ == '__main__':
    db = DBHandler()
    #ret = db.query_all('select * from element_basic_house limit 5;')
    sql = f"select id from element_basic_house where house_name='测试房屋02'"
    ret = db.query_one(sql)
    print(ret)
    db.close()
