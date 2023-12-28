import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_google_genai import GoogleGenerativeAIEmbeddings
#from langchain_google_genai import ChatGoogleGenerativeAI
#from langchain.llms import GooglePalm
import os
from langchain.chat_models import ChatOpenAI
from htmlTemplates import css, bot_template, user_template


# Set your Google API Key
os.environ['GOOGLE_API_KEY'] = 'AIzaSyATBqqkTFy5c39UnK4m7pBbjKE8gvC09e8'
OPENAI_API_KEY = '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'

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=10000, chunk_overlap=200, length_function=len)
    chunks = text_splitter.split_text(text)
    return chunks


def clear_chat_history():
    st.session_state.chat_history = []

def get_vector_store(text_chunks):
    #embeddings=OpenAIEmbeddings()
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    # Custom prompt to request responses in English
    #english_prompt = "You are a helpful assistant speaking English. Respond to the following questions in English."

    #llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.1, convert_system_message_to_human=True,
                                 #prompt=english_prompt)  # Add the prompt here

    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vectorstore.as_retriever(), memory=memory)
    return conversation_chain


def handle_user_input(user_question):
    response=st.session_state.conversation({'question':user_question})
    #st.write(response)
    st.session_state.chat_history = response['chat_history']
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2==0:
            #st.write(message)
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            #st.write(message)
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)



def main():
    load_dotenv()
    st.set_page_config("Chat with Multiple PDFs", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)
    st.header("Chat with Multiple PDFs :books:")

    if "conversation" not in st.session_state:
        st.session_state.conversation=None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history=None
    user_question = st.chat_input("Ask a question from your documents")

    if user_question:
        handle_user_input(user_question)

    with st.sidebar:
        st.header("Chat with PDF 💬")
        st.title("LLM Chatapp using OpenAI")
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload the PDF Files here and Click on Process", accept_multiple_files=True)

        if st.button('Process'):
            with st.spinner("Processing"):
                #Extract Text from PDF
                raw_text = get_pdf_text(pdf_docs)
                #Split the Text into Chunks
                text_chunks = get_text_chunks(raw_text)
                #Create Vector Store
                vectorstore=get_vector_store(text_chunks)
                # Create Conversation Chain
                st.session_state.conversation=get_conversation_chain(vectorstore)
                st.success("Done!")

        # Add a button to clear chat history
        if st.button("Clear Chat"):
            clear_chat_history()

        # Contact Information in a Dropdown
        with st.expander("Contact the Creator"):
            st.markdown("- This chatbot was created by Emmanuel Ezeokeke")
            st.markdown("- Contact him [LinkedIn Profile](https://www.linkedin.com/in/emma-ezeokeke/)")

if __name__ == "__main__":
    main()