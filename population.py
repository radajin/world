import MySQLdb
import pandas as pd

connect_datas = {"host": "3.36.4.108", "user": "root", "passwd": "dss",
                 "db": "world", "charset": "utf8"}
client = MySQLdb.connect(**connect_datas)
df = pd.read_sql("SELECT code, name, population FROM country", client)
print(df.tail())
