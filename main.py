import os
from pathlib import Path
import sys
import streamlit as st
from strimlitbook import read_ipynb

# Get the absolute path of the current file
current_file_path = Path('main.py').resolve()

# Get the directory of the current file
project_dir = current_file_path.parent

print(project_dir)

# Add the project directory to sys.path
sys.path.insert(0, str(project_dir))

# Define the directory path
notebooks_dir = 'notebooks'

# Create the notebooks directory if it doesn't exist
os.makedirs(notebooks_dir, exist_ok=True)

# Streamlit UI
st.title("Upload and Display Jupyter Notebooks")

# Upload .ipynb files
uploaded_file = st.file_uploader("Upload a .ipynb file", type="ipynb")

if uploaded_file is not None:
    # Save the uploaded file to the notebooks directory
    with open(os.path.join(notebooks_dir, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")

# List all files in the notebooks directory
files_in_notebooks = os.listdir(notebooks_dir)

# Filter out .ipynb files
ipynb_files = [file for file in files_in_notebooks if file.endswith('.ipynb')]

# Function to delete a file
def delete_file(filename):
    file_path = os.path.join(notebooks_dir, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        st.success(f"File '{filename}' deleted successfully!")
    else:
        st.error(f"File '{filename}' not found!")

# Print the .ipynb files with delete options
for ipynb_file in ipynb_files:
    st.write(ipynb_file)
    nb = read_ipynb(f"./notebooks/{ipynb_file}")
    nb.display()
    if st.button(f"Delete '{ipynb_file}'", key=ipynb_file):
        delete_file(ipynb_file)
        st.experimental_rerun()
