from openpyxl import Workbook, load_workbook # openpyxl: thư viện làm việc với file excel trong Python
import os # operating system
from datetime import datetime 
import re # Python Regex 
import pandas as pd
import json

def tao_excel(file_excel):
    if os.path.exists(file_excel): #Kiem tra duong link
        #Gọi file excel đã có:
        wb = load_workbook(file_excel) #Load workbook
        ten_sheet = 'Thong tin'
        if ten_sheet in wb.sheetnames:
            ws = wb[ten_sheet]
        else:  
            ws = wb.create_sheet(ten_sheet) #Tao sheet moi
            ten_cac_cot = ["Tên", "Ngày sinh", "Tuổi", "Email", "Số điện thoại", "Công việc", "Tình trạng hôn nhân"]
            ws.append(ten_cac_cot)
    else:
        #Tao file excel moi
        wb = Workbook()
        ws = wb.active
        ws.title = 'Thong tin'
        ten_cac_cot = ["Tên", "Ngày sinh", "Tuổi", "Email", "Số điện thoại", "Công việc", "Tình trạng hôn nhân"]
        ws.append(ten_cac_cot)
    return wb, ws

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Agentic (RAG chatbot) => AI Agent
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' # Python Regular Expression (Base để các bạn học NLP - Natural Language Processing) Python Regex => LLM => Generative AI => AI Agent
    return bool(re.match(pattern, email)) # True: no    # Tokenize

def kiem_tra_mail(email):
    duoi_mail = email[-10:]
    kich_thuoc = len(email)
    if kich_thuoc > 10 and duoi_mail == '@gmail.com':
        return True
    else:
        return False
    
def validate_phone(phone):
    pattern = r'^\d{10,11}$'
    return bool(re.match(pattern, phone))

def kiem_tra_sdt(phone):
    kich_thuoc = len(phone)
    so_dau_tien = phone[0]
    if kich_thuoc == 10 and so_dau_tien == '0':
        return True
    else:
        return False
    
def get_status_code(age, job, is_student):
    if is_student:
        return 1
    if age >= 18:
        return 3 if job else 2
    return None

def data_source(file_name):
    df = pd.read_csv(file_name)
    df['ngay_dat'] = pd.to_datetime(df['ngay_dat'], format='mixed')
    df['thanh_tien'] = df['so_luong'] * df['don_gia']
    return df

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