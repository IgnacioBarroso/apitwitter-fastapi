import datetime
from sqlalchemy import Table, Column
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DATE, DATETIME, Integer, String
from config.db import meta, engine

users = Table("users", meta, 
               Column("id", Integer, primary_key=True, autoincrement=True), 
               Column("email", String(60), nullable=False),
               Column("first_name", String(50), nullable=False),
               Column("last_name", String(50), nullable=True),
               Column("birth_date", DATE, default=null),
               Column("password", String(140), nullable=False),
               Column("tweets", Integer, ForeignKey("tweets_table.id"))
            )

tweets_table = Table("tweets_table", meta, 
               Column("id", Integer, primary_key=True, autoincrement=True), 
               Column("content", String(140), nullable=False),
               Column("created_at", DATETIME, default=datetime.datetime.now, nullable=False),
               Column("updated_at", DATETIME, onupdate=datetime.datetime.now, nullable=True),
               Column("user", Integer, ForeignKey("users.id"))
            )

meta.create_all(engine)