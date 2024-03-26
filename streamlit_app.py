import streamlit as st
import pandas as pd

# Function to fetch images data from Snowflake external stage
def fetch_images_data(folder_name, image_name, snowflake_client):
    query = f"SELECT * FROM @MANGO_LEAF_ML_DB.ML_APP_SCHEMA.MANGO WHERE folder = '{folder_name}' AND image_name = '{image_name}'"
    result = snowflake_client.execute(query)
    df = pd.DataFrame(result.fetchall(), columns=result.column_names)
    return df

# Streamlit app
st.title('AWS S3 Images Viewer')

# Dropdown to select folder
selected_folder = st.selectbox('Select a folder:', ['Sooty Mould', 'Powdery Mildew', 'Healthy', 'Gall Midge', 'Die Back', 'Cutting Weevil', 'Bacterial Canker', 'Anthracnose'])

# Fetch images data based on selected folder
images_df = fetch_images_data(selected_folder, '', snowflake_client)  # Assuming 'snowflake_client' is the Snowflake client object

# Get unique image names for the selected folder
image_names = images_df['image_name'].unique().tolist()

# Dropdown to select image
selected_image = st.selectbox('Select an image:', [''] + image_names)  # Include an empty option for no image selected

if selected_image:
    # Fetch images data based on selected folder and image
    selected_image_df = fetch_images_data(selected_folder, selected_image, snowflake_client)
    
    # Display selected image data
    st.write(selected_image_df)
else:
    st.warning('Please select an image to view its data.')
