from sqlalchemy import Table, Column, Integer, String, Boolean
from .database import metadata

todos = Table(
    "todos",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("description", String(250)),
    Column("completed", Boolean, default=False),   
)