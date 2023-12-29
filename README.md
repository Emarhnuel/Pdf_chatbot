Multiple PDF Chatbot
Overview
The Multiple PDF Chatbot is a Streamlit application designed to facilitate interactive conversations with content extracted from multiple PDF documents. Utilizing advanced NLP models from OpenAI and Google, this chatbot can understand and respond to user queries by referencing specific information found within the uploaded PDF files.

Features
PDF Processing: Upload and process text from multiple PDF documents.
Conversational AI: Leverage OpenAI's powerful language models for natural and context-aware interactions.
Responsive Interface: Built with Streamlit, the chatbot offers a user-friendly web interface.
Clear Chat History: Option to clear the chat history for fresh interactions.
Requirements:
Python 3.x
Streamlit
PyPDF2
LangChain
FAISS (CPU version)
OpenAI API key
Google Generative AI Embeddings
Other dependencies as listed in requirements.txt.
Installation
To run this application, you need to have Python installed on your system. Follow these steps to set up the project:

Clone the Repository:

bash
Copy code
git clone (https://github.com/Emarhnuel/Pdf_chatbot/tree/main/Multiplepdf)
cd [PDF chatbot]
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Set up Environment Variables:

Create a .env file in the project root directory.
Add your OpenAI API key and Google API key:
makefile
Copy code
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
Running the Application
To start the Streamlit application, run the following command in the terminal:

bash
Copy code
streamlit run main.py
Navigate to the local URL provided by Streamlit to interact with the chatbot.

Usage
Upload PDFs: Use the sidebar to upload one or more PDF documents.
Ask Questions: Type your queries in the chat input box and get responses based on the content of the uploaded PDFs.
Clear Chat: Click the "Clear Chat" button if you need to reset the conversation.
Contributing
Contributions to enhance the Multiple PDF Chatbot are welcome. Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.



Contact the Creator
Created by: Emmanuel Ezeokeke
