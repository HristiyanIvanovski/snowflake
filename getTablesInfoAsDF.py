import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col

def main(session: snowpark.Session): 
    schema_name = '<your_schema_name>'
    
    rows = session.sql(f"SHOW TABLES IN SCHEMA {schema_name}").collect()

    # Convert the list of Row objects to a Snowpark DataFrame
    tables = session.createDataFrame(rows)

    # Print a sample of the dataframe to standard output.
    tables.show()

    # Return value will appear in the Results tab.
    return tables
