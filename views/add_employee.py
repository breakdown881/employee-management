import streamlit as st
import pandas as pd
from helper import load_data, save_data, generate_id, calculate_age
from models.employee import Employee
from models.exceptions import InvalidEmailError, InvalidPhoneError

def show_add_employee(db_file):
    st.header("Add Employee")
    
    with st.container(border= True):
        st.subheader("Employee Information")
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        dob = st.date_input("Date of Birth", min_value=pd.Timestamp('1900-01-01'), max_value=pd.Timestamp.now())
        department = st.selectbox("Department", ["HR", "Engineering", "Sales", "Marketing"])
        salary = st.number_input("Salary", min_value=0.0, step=1000.0)
        day_worked = st.number_input("Days Worked", min_value=0, step=1)
        
        if st.button("Add Employee"):
            if name and department:
                try:
                    employees = load_data(db_file)
                    existing_ids = [emp["ID"] for emp in employees]
                    new_employee = Employee(
                        id=generate_id(name, dob, department, salary, day_worked),
                        name=name,
                        email=email,
                        phone=phone,
                        dob=dob,
                        department=department,
                        salary=salary,
                        day_worked=day_worked
                    )
                    
                    if new_employee.id not in existing_ids:
                        employees.append(new_employee.to_dict())
                    
                    save_data(db_file, employees)
                    
                    st.success(f"Employee '{name}' added successfully!")
                
                except InvalidEmailError as e:
                    st.error(e)
                except InvalidPhoneError as e:
                    st.error(e)
            else:
                st.error("Please fill in all required fields.")
                
        uploaded_file = st.file_uploader("Upload Employee Data (XLS)", type=["xls", "xlsx"])
        if uploaded_file:
            try:
                df = pd.read_excel(uploaded_file)
                required_columns = {"name", "email", "phone", "dob", "department", "salary", "day_worked"}
                if required_columns.issubset(df.columns):
                    try:
                        employees = load_data(db_file)
                        existing_ids = [emp["ID"] for emp in employees]
                        df['age'] = df['dob'].apply(calculate_age)
                        df['ID'] = df.apply(lambda row: generate_id(row['name'], row['dob'], row['department'], row['salary'], row['day_worked']), axis=1)
                        df['bonus'] = df.apply(lambda row: row['salary'] * 0.5 if row['day_worked'] > 20 else row['salary'] * 0.2, axis=1)
                        new_employees = [Employee(**emp) for emp in df[["ID", "name", "email", "phone", "dob", "age", "department", "salary", "day_worked", "bonus"]].to_dict(orient='records')]
                        
                        for item in new_employees:
                            if item.id not in existing_ids:
                                employees.append(item.to_dict())
                        
                        save_data(db_file, employees)
                        
                        st.success(f"{len(new_employees)} employees added successfully from the uploaded file!")
                    
                    except InvalidEmailError as e:
                        st.error(e)
                    except InvalidPhoneError as e:
                        st.error(e)
                else:
                    st.error("Uploaded file is missing required columns. Please ensure it contains: name, dob, department, salary, day_worked.")
            except Exception as e:
                st.error(f"Error processing uploaded file: {e}")