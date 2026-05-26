from openpyxl import Workbook, load_workbook # openpyxl: thư viện làm việc với file excel trong Python
import os # operating system
from datetime import date, datetime 
import re # Python Regex 
import pandas as pd
import json

def calculate_age(birth_date):
    if isinstance(birth_date, str):
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()

    today = date.today()

    age = today.year - birth_date.year - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )

    return age

# Agentic (RAG chatbot) => AI Agent
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' # Python Regular Expression (Base để các bạn học NLP - Natural Language Processing) Python Regex => LLM => Generative AI => AI Agent
    return bool(re.match(pattern, email)) # True: no    # Tokenize
    
def validate_phone(phone):
    pattern = r"^(0|\+84|84)([3|5|7|8|9])([0-9]{8})$"
    return bool(re.match(pattern, phone))

def load_data(db_file):
    try:
        with open(db_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_data(db_file, data):
    with open(db_file, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4,
            default=int
        )
        
def generate_id(name, dob, department, salary, day_worked):
    return int(
        pd.util.hash_pandas_object(
            pd.Series([name, dob, department, salary, day_worked])
        ).sum()
    )