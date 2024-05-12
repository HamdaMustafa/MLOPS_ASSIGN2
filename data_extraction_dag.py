# data_extraction_dag.py
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from data_extraction import extract_links, extract_article_data
from data_transformation import preprocess_text
from data_storage_version_control import store_data_locally, version_data_with_dvc

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

extract_data_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_links,  # Use the appropriate function from data_extraction.py
    op_args=['https://www.dawn.com/'],  # Pass URL as argument
    dag=dag,
)

transform_data_task = PythonOperator(
    task_id='transform_data',
    python_callable=preprocess_text,  # Use the appropriate function from data_transformation.py
    dag=dag,
)

store_data_task = PythonOperator(
    task_id='store_data',
    python_callable=store_data_locally,  # Use the appropriate function from data_storage_version_control.py
    op_args=['data_to_store.txt'],  # Pass filename as argument
    dag=dag,
)

version_data_task = PythonOperator(
    task_id='version_data',
    python_callable=version_data_with_dvc,  # Use the appropriate function from data_storage_version_control.py
    op_args=['C://Users//Dell//Documents//materials//version.txt'],  # Pass file path as argument
    dag=dag,
)

extract_data_task >> transform_data_task >> store_data_task >> version_data_task
