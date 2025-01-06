import os
import json
import streamlit as st
from groq import Groq
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

st.set_page_config(
    page_title="Chatbot em Groq",
    page_icon=":robot:",
    layout="centered",
)

working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))

GROQ_API_KEY = config_data.get("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("Chave da API ausente no arquivo config.json.")
    st.stop()

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

try:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
except Exception as e:
    st.error(f"Falha ao inicializar o cliente Groq: {e}")
    st.stop()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
faiss_index = faiss.IndexFlatL2(384)

st.title("Chatbot de Italo Cajado")

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_prompt = st.chat_input("Envie sua mensagem...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    messages = [
        {"role": "system", "content": "Você é um assistente útil."},
        *st.session_state.chat_history 
    ]

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages
        )

        assistant_response = response.choices[0].message.content
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

        with st.chat_message("assistant"):
            st.markdown(assistant_response)

        if "informação" in user_prompt.lower():
            embedding = embedding_model.encode(user_prompt)
            faiss_index.add(np.array([embedding], dtype=np.float32))

    except Exception as e:
        st.error(f"Erro ao buscar a resposta do GROQ: {e}")

def retrieve_from_faiss(query):
    query_embedding = embedding_model.encode(query)
    D, I = faiss_index.search(np.array([query_embedding], dtype=np.float32), k=1)
    return I

if st.button("Consultar informações armazenadas"):
    query = st.text_input("Digite sua consulta")
    if query:
        result = retrieve_from_faiss(query)
        st.write(f"Resultado da consulta: {result}")
