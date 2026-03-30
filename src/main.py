"""from sqlalchemy import create_engine
import pandas as pd

# load data
df = pd.read_csv("data/Superstore.csv", encoding="windows-1252")

# connection
URL = "postgresql://postgres.kvnklalnsobpxbhsiobv:QKBR6uAV5IFPYqls@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres?sslmode=require"

engine = create_engine(URL)

# insert ke database
df.to_sql(
    "orders",  # nama tabel
    engine,
    if_exists="replace",  # replace kalau sudah ada
    index=False,  # jangan simpan index
    chunksize=1000,  # biar stabil
)

print("Data berhasil masuk ke tabel 'orders' 🚀")"""

""" 
from sqlalchemy import create_engine

DB_URL = "postgresql://postgres.kvnklalnsobpxbhsiobv:QKBR6uAV5IFPYqls@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres?sslmode=require"

engine = create_engine(DB_URL)

with engine.connect() as conn:
    print("Connected!")
 """

""" from sqlalchemy import create_engine

DB_URL = "postgresql://postgres:QKBR6uAV5IFPYqls@db.kvnklalnsobpxbhsiobv.supabase.co:5432/postgres"

engine = create_engine(
    DB_URL, connect_args={"sslmode": "require", "options": "-c client_encoding=utf8"}
)

with engine.connect() as conn:
    print("Connected!") """
