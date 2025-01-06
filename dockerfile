FROM python:3.13.0

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install langchain_community

COPY src/ .

CMD [ "streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]