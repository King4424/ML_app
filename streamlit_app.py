import streamlit as st
import pandas as pd
import snowflake.connector as snowflake

# Snowflake connection parameters
snowflake_user = 'vaibhavk'
snowflake_password = 'King@4424'
snowflake_account = 'LFAQUDB-HF93281'
snowflake_warehouse = 'vaibhav'
snowflake_database = 'MANGO_LEAF_ML_DB'
snowflake_schema = 'ML_APP_SCHEMA'

# Snowflake connection
conn = snowflake.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account,
    warehouse=snowflake_warehouse,
    database=snowflake_database,
    schema=snowflake_schema
)

# Function to fetch images data from Snowflake external stage
def fetch_images_data(folder_name):
    query = f"SELECT * FROM @MANGO_LEAF_ML_DB.ML_APP_SCHEMA.MANGO WHERE folder = '{folder_name}'"
    df = pd.read_sql_query(query, conn)
    return df

# Streamlit app
st.title('AWS S3 Images Viewer')

# Dropdown to select folder
selected_folder = st.selectbox('Select a folder:', ['Sooty Mould', 'Powdery Mildew', 'Healthy', 'Gall Midge', 'Die Back', 'Cutting Weevil', 'Bacterial Canker', 'Anthracnose'])

# Fetch images data based on selected folder
images_df = fetch_images_data(selected_folder)

# Display images data
st.write(images_df)
