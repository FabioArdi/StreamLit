import streamlit as st
import pandas as pd

# Load sample dataset
def load_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    data = pd.read_csv(url)
    return data

# Main function
def main():
    st.title("Titanic Dataset Explorer")
    
    # Load the dataset
    data = load_data()
    
    # Display the data in a table
    st.subheader("Dataset")
    st.dataframe(data)
    
    # Control the display
    st.sidebar.subheader("Display Options")
    
    # Checkbox for selecting columns to display
    selected_columns = st.sidebar.multiselect("Select Columns", data.columns)
    
    # Filter the dataset based on selected columns
    filtered_data = data[selected_columns]
    
    # Display the filtered data
    st.subheader("Filtered Dataset")
    st.dataframe(filtered_data)

# Run the app
if __name__ == "__main__":
    main()
