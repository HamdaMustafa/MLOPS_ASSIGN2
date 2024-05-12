from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import requests
from bs4 import BeautifulSoup
import os
import re
# Importing DVC API
import dvc.api

# Define the directory for storing data on Google Drive
GOOGLE_DRIVE_STORAGE_DIR = 'gdrive:///1ny6_GVEwwvwlPrR2TbyAvmjBmnvIAnbl/data'

def extract_links(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a')]
    return links

def extract_article_data(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    titles = [title.text for title in soup.find_all('h2')]
    descriptions = [desc.text for desc in soup.find_all('p')]
    return titles, descriptions

def preprocess_text(text):
    """
    Preprocesses the extracted text data.
    """
    # Example of text preprocessing:
    # 1. Convert text to lowercase
    preprocessed_text = text.lower()
    
    # 2. Remove special characters, punctuation, and digits
    preprocessed_text = re.sub(r'[^a-zA-Z\s]', '', preprocessed_text)

    # 3. Remove extra whitespace
    preprocessed_text = re.sub(r'\s+', ' ', preprocessed_text).strip()

    # Add more preprocessing steps as needed

    return preprocessed_text

def store_data_on_google_drive(data, filename):
    """
    Stores the processed data on Google Drive using DVC.
    """
    file_path = os.path.join(GOOGLE_DRIVE_STORAGE_DIR, filename)
    with dvc.api.open(file_path, 'w') as file:
        file.write(data)
    return file_path

def run_pipeline():
    url = 'https://www.dawn.com/'  # Example URL
    links = extract_links(url)
    titles, descriptions = extract_article_data(url)
    preprocessed_text = preprocess_text(' '.join(titles + descriptions))
    file_path = store_data_on_google_drive(preprocessed_text, 'data_to_store.txt')

# Define the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 12),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'data_extraction_transformation_storage',
    default_args=default_args,
    description='Automated data extraction, transformation, and storage',
    schedule_interval=timedelta(days=1),
)

run_pipeline_task = PythonOperator(
    task_id='run_pipeline',
    python_callable=run_pipeline,
    dag=dag,
)

run_pipeline_task