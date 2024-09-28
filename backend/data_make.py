import pyarrow.parquet as pq
import pandas as pd
import psycopg2 
import numpy as np
from config import (
    DB_HOST,
    DB_NAME,
    DB_PASS,
    DB_USER,
)
import sys
#pq_file = pq.ParquetFile("video_stat.parquet")
#pq_file.write.csv("video_stat_csv.csv")

param_dic = {
    "host"      : "localhost",
    "database"  : "cold_start_hakaton",
    "user"      : "postgres", 
    "password"  :  "0000"
}


def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn


def execute_many(conn, df, table):
    """
    Using cursor.executemany() to insert the dataframe
    """
    # Create a list of tupples from the dataframe values
    tuples = [tuple(x) for x in df.to_numpy()]
    # Comma-separated dataframe columns
    cols = ','.join(list(df.columns))
    # SQL quert to execute
    query  = "INSERT INTO %s(%s) VALUES(%%s,%%s,%%s)" % (table, cols)
    cursor = conn.cursor()
    try:
        cursor.executemany(query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("execute_many() done")
    cursor.close()

# Run the execute_many strategy






