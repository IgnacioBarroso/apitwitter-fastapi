from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:root@twitterapi_mysql_1:3306/twitter')

meta = MetaData()

db = engine.connect()
