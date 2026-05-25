import streamlit as st
from helper import load_data
import json

def show_edit_delete(db_file):
    st.header("Edit & Delete Employee")
    employees = load_data(db_file)
    if not employees:
        st.warning("No employee data available.")
        return
    
    employee_to_modify = st.selectbox("Select Employee to Edit/Delete", [f"{emp['ID']} - {emp['name']}" for emp in employees])
    if employee_to_modify:
        emp_id = int(employee_to_modify.split(" - ")[0])
        print(emp_id)
        selected_employee = next((emp for emp in employees if emp['ID'] == emp_id), None)
        
        action = st.radio("Choose Action", ["Edit", "Delete"])
        if action == "Edit":
            new_department = st.selectbox("Department", options= ['New Department'] + list(set(emp['department'] for emp in employees)), index=list(set(emp['department'] for emp in employees)).index(selected_employee['department']))
            if new_department == 'New Department':
                new_department = st.text_input("Enter New Department")
            new_salary = st.number_input("Salary", value=selected_employee['salary'], step=1000)
            new_day_worked = st.number_input("Days Worked", value=selected_employee['day_worked'], step=1)
            if st.button("Save Changes"):
                selected_employee['department'] = new_department
                selected_employee['salary'] = new_salary
                selected_employee['day_worked'] = new_day_worked
                with open(db_file, "w", encoding="utf-8") as f:
                    json.dump(employees, f, ensure_ascii=False, indent=4)
                st.success("Employee updated successfully!")
        elif action == "Delete":
            if st.button("Confirm Delete"):
                employees = [emp for emp in employees if emp['ID'] != emp_id]
                with open(db_file, "w", encoding="utf-8") as f:
                    json.dump(employees, f, ensure_ascii=False, indent=4)
                st.success("Employee deleted successfully!")