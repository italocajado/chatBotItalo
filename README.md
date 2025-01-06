# **Projeto Chatbot Italo Cajado**

Este é um chatbot interativo desenvolvido utilizando **Groq**, **Langchain**, **FAISS** e **Streamlit**. O chatbot pode interagir com o usuario atraves de requisições feitas no campo designado, o mesmo armazena essas informações utilizando FAISS, é utilizado docker para rodar a aplicação

## **1. Pré-requisitos**

Antes de rodar a aplicação, você precisará ter as seguintes ferramentas instaladas:

- **Python 3.13.0 ou superior**
- **Docker** (para rodar a aplicação em container)
- **Streamlit** (para executar a interface web)

Se você optar por executar a aplicação localmente, siga as instruções abaixo. Caso contrário, o Docker pode ser utilizado para rodar a aplicação de forma isolada e sem a necessidade de instalação de dependências localmente.

---

## **2. Instalação Local**

### **Passo 1: Clonar o repositório**

Primeiro, clone o repositório para o seu ambiente local:

```bash
git clone <https://github.com/italocajado/chatBotItalo.git>
cd chatbotitalo
```

### **Passo 2: Criar um ambiente virtual**

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python3 -m venv venv
source venv/bin/activate
venv\Scripts\activate
```

### **Passo 3: Instalar as dependências**

Com o ambiente virtual ativado, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### **Passo 4: Configuração**

Antes de executar o chatbot, é necessário configurar a chave da API do **Groq**. Para isso, vá ao arquivo `config.json` dentro da pasta `src/` com o seguinte conteúdo:

```json
{
    "GROQ_API_KEY": "your_groq_api_key_here"
}
```

Substitua `"your_groq_api_key_here"` pela sua chave de API do Groq.

Aqui esta o link para o site para caso queira utilizar sua propria conta e gerar sua chave API: https://groq.com/

### **Passo 5: Executar a aplicação**

Agora, com as dependências instaladas e a chave de API configurada, execute a aplicação com o comando abaixo:

```bash
streamlit run src/app.py
```

A aplicação será iniciada e estará acessível no navegador em `http://localhost:8501`.

### **Exemplo de uso**

- Ao abrir o navegador, você verá a interface do chatbot onde pode enviar mensagens.
- O chatbot responde com base no modelo e armazena informações relevantes para futuras consultas.
- Você pode consultar as informações armazenadas clicando no botão "Consultar informações armazenadas".

---

## **3. Container Docker**

### **Passo 1: Criar a imagem Docker**

Se você preferir rodar a aplicação em um container Docker, basta construir a imagem Docker utilizando o Dockerfile incluído no projeto.

Primeiro, construa a imagem Docker executando o seguinte comando no diretório raiz do projeto:

```bash
docker build -t chatbotitalo .
```

Este comando irá criar uma imagem chamada `chatbotitalo` a partir do Dockerfile.

### **Passo 2: Rodar o container Docker**

Após a construção da imagem, execute a aplicação em um container Docker com o seguinte comando:

```bash
docker run -p 8501:8501 chatbotitalo
```

Isso fará com que a aplicação seja executada e acessível em `http://localhost:8501` no seu navegador.

### **Passo 3: Parar o container**

Se você precisar parar o container Docker, execute:

```bash
docker stop <chatbot-langchain-groq>
```

Você pode obter o nome do container com o comando:

```bash
docker ps
```

---

## **4. Dockerfile**

O **Dockerfile** incluído no projeto é utilizado para criar a imagem Docker e facilitar a execução da aplicação em diferentes ambientes. Aqui está o conteúdo do Dockerfile:

```dockerfile
FROM python:3.13.0

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install langchain_community

COPY src/ .

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
```

Este Dockerfile realiza as seguintes etapas:

1. **FROM python:3.13.0**: Usa a imagem oficial do Python 3.13.0.
2. **WORKDIR /app**: Define o diretório de trabalho dentro do container como `/app`.
3. **COPY requirements.txt requirements.txt**: Copia o arquivo `requirements.txt` para o diretório de trabalho.
4. **RUN pip install -r requirements.txt**: Instala as dependências listadas no `requirements.txt`.
5. **COPY src/ .**: Copia todos os arquivos da pasta `src` para o container.
6. **CMD**: Define o comando para rodar a aplicação com Streamlit.

---

## **5. Considerações Finais**

Agora você tem duas opções para rodar a aplicação: localmente com as dependências instaladas ou em um container Docker. Ambas as opções são viáveis.

Se tiver alguma dúvida ou problema, fique à vontade para consultar a documentação ou abrir uma issue no repositório :).

---
