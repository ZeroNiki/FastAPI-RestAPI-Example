from sqlalchemy import Table, String, Integer, TIMESTAMP, Column, Boolean, MetaData
from sqlalchemy.sql import func

metadata = MetaData()

task = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("description", String, nullable=True),
    Column("done", Boolean, default=False),
    Column("created_at", TIMESTAMP, default=func.now(), nullable=False),
)
