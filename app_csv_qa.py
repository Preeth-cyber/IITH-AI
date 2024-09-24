import streamlit as st
import pandas as pd
import csv_agent  # Assuming this is your custom module for handling queries

# Title of the application
st.title('Pose Questions from File')

# File uploader for CSV files
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)

    # Show the dataframe (CSV content)
    st.write("### Data:")
    st.dataframe(df.head())  # Display the first few rows of the dataframe
    
    # Get the file name of the uploaded CSV file
    filename = uploaded_file.name
    
    # Subheading for the question section
    st.write("### Ask a Question")
    
    # Input area for users to ask questions
    question = st.text_input("Enter your question about the data")

    # Button to submit the question
    if st.button("Ask"):
        if question:
            # Pass the CSV file name and the question to the csv_query function
            response = csv_agent.csv_query(filename, question)
            
            # Display the question and the response from the csv_query function
            st.write(f"You asked: {question}")
            st.write(f"Response: {response}")
        else:
            st.write("Please enter a question.")
else:
    st.write("Please upload a CSV file to view its contents.")
