from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import declarative_base, Session

db_url = "sqlite+pysqlite:///2. SQLalchemy/database.db"
engine = create_engine(db_url, echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)

# Database connection
""" ##not commited
with engine.connect() as conn:
    result = conn.execute(text("select 'Hello Word'"))
    print(result.all)"""

""" ## commit as you go
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE my_2nd_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO my_2nd_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    )
    conn.commit() """

""" ## begin once
with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO my_2nd_table (x, y) VALUES (:x, :y)"),
        [{"x": 6, "y": 8}, {"x": 9, "y": 10}, {"x": 13, "y": 11}, {"x": 20, "y": 9}],
    ) """

# Fetching Rows
"""with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM my_2nd_table"))
    for row in result:
        print(f"x:{row.x} y:{row.y}") """

# Using session
"""stmt = text("SELECT x, y FROM my_2nd_table WHERE y > :y ORDER BY x,y")
with Session(engine) as session:
    result = session.execute(stmt, {"y": 6})
    for row in result:
        print(f"x:{row.x} y:{row.y}")"""

with Session(engine) as session:
    result = session.execute(
        text("Update my_2nd_table SET y=:y WHERE x=:x"),
        [{"x": 9, "y": 11}, {"x": 13, "y": 15}, {"x": 45, "y": 74}],
    )
    session.commit()
