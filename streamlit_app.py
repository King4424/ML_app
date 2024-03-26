import streamlit as st

conn = st.connection("snowflake")

df = conn.query("SELECT * from mytable;", ttl=600)

for row in df.itertuples():
    st.write(f"{row.Name} has a :{row.PET}:")
