# IITH-AI
This repo has all the code I did.
Project Title: NLP Applications with BERT and LangChain
Overview
This project demonstrates various applications of natural language processing (NLP) using BERT and LangChain. It includes examples of building models, handling CSV data, and extracting meaningful insights from text.

Files Included
1. LangChain Introduction
This file introduces LangChain, a framework for working with language models. It covers:

Setting up the environment and necessary libraries.
Using OpenAI's models for various tasks, including text predictions and prompt handling.
2. app_csv_qa.py
A Streamlit application that allows users to upload CSV files and ask questions about the data. The app:

Displays the contents of the uploaded CSV.
Accepts user questions and provides responses based on the data using a custom CSV query function.
3. BERT Introduction.ipynb
An introductory notebook that covers:

What BERT is and how it works.
Applications of BERT in tasks like sentiment analysis and question answering.
The benefits of using BERT for NLP tasks.
4. BERT Tokenizer Model Introduction.ipynb
This notebook provides insights into the BERT tokenizer, covering:

Tokenization and vocabulary.
Use cases for measuring text similarity and extracting word embeddings.
5. CSV Agent.py
A custom module designed for handling queries related to CSV data, facilitating interaction with the app and enabling users to retrieve specific information from datasets.

6. Example BERT MSM.ipynb
A notebook showcasing examples of BERT's capabilities, including masked language modeling and token embeddings.

7. requirements.txt
Lists the necessary Python packages for the project, including:

openai, jupyter, scikit-learn, langchain, transformers, huggingface-hub, streamlit, python-dotenv, tiktoken, and bertviz.
How to Run the Project
Clone the repository.
Install the required packages using:
bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:
bash
Copy code
streamlit run app_csv_qa.py
Explore the Jupyter notebooks to see examples and learn more about BERT and LangChain.
License
This project is open-source. Feel free to contribute!
