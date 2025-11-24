# airflow/dags/scrape_dag.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from app.scraper import download_pdf
from app.extractor import pdf_to_text
from app.ingest import add_documents

default_args = {'owner':'me','retries':1,'retry_delay':timedelta(minutes=5)}

dag = DAG('scrape_ingest', start_date=datetime(2025,1,1), schedule_interval='@daily', default_args=default_args)

urls = ['https://arxiv.org/pdf/2306.03672.pdf']

def run_once():
    for url in urls:
        path = download_pdf(url)
        text = pdf_to_text(path)
        chunks = [c for c in text.split('\n\n') if len(c) > 50][:10]
        ids = [path + f"::chunk{i}" for i in range(len(chunks))]
        add_documents(chunks, ids)

task = PythonOperator(task_id='scrape_ingest', python_callable=run_once, dag=dag)
