import pandas as pd
from sqlalchemy import create_engine

def load_from_sql(db_url: str, table: str = None, query: str = None):
    """
    Load data from any SQL database using SQLAlchemy.
    
    Parameters:
        db_url: SQLAlchemy formatted database URL 
                Examples:
                - sqlite:///mydb.db
                - mysql+pymysql://user:pass@localhost/dbname
                - postgresql://user:pass@localhost/dbname

        table: Name of table to read (optional)
        query: SQL query to execute (optional)

    Returns:
        Pandas DataFrame
    """

    engine = create_engine(db_url)

    if query:
        df = pd.read_sql_query(query, engine)
    elif table:
        df = pd.read_sql_table(table, engine)
    else:
        raise ValueError("Provide either 'table' or 'query' when loading from SQL.")

    return df
