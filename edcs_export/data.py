import os
import shutil
from pathlib import Path

import environ
import pandas as pd
import sqlalchemy as db
from sqlalchemy import text

from .choices import DATA_MODEL

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_DIR = str(Path(os.path.join(BASE_DIR, ".env")))

env = environ.Env(
    DJANGO_DEBUG=(bool, False),
    DEBUG_TOOLBAR=(bool, False),
)

environ.Env.read_env(ENV_DIR)

DB_DT_URL = env.str("DB_DT_URL")
EDCS_DATA_DIR = env.str("EDCS_DATA_DIR")

MYSQL_CONN = DB_DT_URL
engine = db.create_engine(MYSQL_CONN).connect()


def get_table_data(data):
    myQuery = text(f"select * from {data}")
    df = pd.read_sql_query(myQuery, engine)
    df.to_excel(f"{EDCS_DATA_DIR}/{data}.xlsx")
    return df


for data in DATA_MODEL:
    get_table_data(data)

shutil.make_archive(EDCS_DATA_DIR, "zip", EDCS_DATA_DIR)
