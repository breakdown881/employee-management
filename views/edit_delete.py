import streamlit as st
from helper import load_data
import json
from models.employee import Employee
from models.exceptions import InvalidEmailError, InvalidPhoneError

def show_edit_delete(db_file):
    st.header("Edit & Delete Employee")
    employees = load_data(db_file)
    if not employees:
        st.warning("No employee data available.")
        return
    
    employee_to_modify = st.selectbox("Select Employee to Edit/Delete", [f"{emp['ID']} - {emp['name']}" for emp in employees])
    if employee_to_modify:
        emp_id              = int(employee_to_modify.split(" - ")[0])
        selected_employee   = next((emp for emp in employees if emp['ID'] == emp_id), None)
        
        action = st.radio("Choose Action", ["Edit", "Delete"])
        if action == "Edit":
            new_email       = st.text_input("Email", value=selected_employee['email'])
            new_phone       = st.text_input("Phone", value=selected_employee['phone'])
            new_department  = st.selectbox("Department", options= ['New Department'] + list(set(emp['department'] for emp in employees)), index=list(set(emp['department'] for emp in employees)).index(selected_employee['department']))
            if new_department == 'New Department':
                new_department = st.text_input("Enter New Department")
            new_salary      = st.number_input("Salary", value=int(selected_employee['salary']), step=1000)
            new_day_worked  = st.number_input("Days Worked", value=selected_employee['day_worked'], step=1)
            if st.button("Save Changes"):
                try:
                    employee = Employee(
                        id          = selected_employee['ID'],
                        name        = selected_employee['name'],
                        email       = new_email,
                        phone       = new_phone,
                        dob         = selected_employee['dob'],
                        department  = new_department,
                        salary      = new_salary,
                        day_worked  = new_day_worked
                    )

                    selected_employee['department'] = employee.department
                    selected_employee['email']      = employee.email
                    selected_employee['phone']      = employee.phone
                    selected_employee['salary']     = employee.salary
                    selected_employee['day_worked'] = employee.day_worked
                    selected_employee['bonus']      = employee.bonus
                    with open(db_file, "w", encoding="utf-8") as f:
                        json.dump(employees, f, ensure_ascii=False, indent=4)
                    st.success("Employee updated successfully!")
                    
                except InvalidEmailError as e:
                    st.error(e)
                except InvalidPhoneError as e:
                    st.error(e)
        elif action == "Delete":
            if st.button("Confirm Delete"):
                employees = [emp for emp in employees if emp['ID'] != emp_id]
                with open(db_file, "w", encoding="utf-8") as f:
                    json.dump(employees, f, ensure_ascii=False, indent=4)
                st.success("Employee deleted successfully!")