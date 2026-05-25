import streamlit as st
from helper import load_data

def show_home_page(db_file):
    st.header("Welcome to the Employee Management System!")
    st.write("""
        This dashboard allows you to manage employee records efficiently. 
        You can add new employees, view the employee list, edit or delete existing records, and analyze statistics about your workforce.
        
        Use the sidebar to navigate through different sections of the dashboard.
    """)
    employees = load_data(db_file)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Employees", value=len(employees))
    
    with col2:
        if employees:
            average_age = sum(emp['age'] for emp in employees) / len(employees)
            st.metric(label="Average Age", value=f"{average_age:.1f}")
        else:
            st.metric(label="Average Age", value="N/A")
            
    with col3:
        if employees:
            average_bonus = sum(emp['bonus'] for emp in employees) / len(employees)
            st.metric(label="Average Bonus", value=f"{average_bonus:,.4f} VND")
        else:
            st.metric(label="Average Bonus", value="N/A")