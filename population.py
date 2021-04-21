import configparser
import MySQLdb
import pandas as pd

config = configparser.ConfigParser()
config.read("../datas.ini")
datas = config["dss"]

connect_datas = {"host": datas["PUBLIC_ID"], "user": datas["USER"], "passwd": datas["PASSWORD"],
                 "db": "world", "charset": "utf8"}
client = MySQLdb.connect(**connect_datas)
df = pd.read_sql("SELECT code, name, population FROM country", client)
print(df.tail())
