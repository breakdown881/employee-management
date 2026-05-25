import streamlit as st
from helper import load_data
import matplotlib.pyplot as plt

def show_statistics(db_file):
    st.header("Employee Statistics")
    employees = load_data(db_file)
    if not employees:
        st.warning("No employee data available to display statistics.")
        return
    
    with st.container(border=True):
        plt.figure(figsize=(10, 6))
        plt.title("Employee Age Distribution")
        plt.xlabel("Age")
        plt.ylabel("Number of Employees")
        ages = [emp['age'] for emp in employees]
        plt.hist(ages, bins=20, edgecolor='black')
        st.pyplot(plt)
        
    with st.container(border=True):
        plt.figure(figsize=(10, 6))
        plt.title("Employee Department Distribution")
        departments = [emp['department'] for emp in employees]
        plt.pie([departments.count(dept) for dept in set(departments)], labels=set(departments), autopct='%1.1f%%')
        st.pyplot(plt)
        
    with st.container(border=True):
        plt.figure(figsize=(10, 6))
        plt.title("Department Total Bonus Distribution")
        bonus_data = {}
        for emp in employees:
            dept = emp['department']
            bonus = emp['bonus']
            bonus_data[dept] = bonus_data.get(dept, 0) + bonus
        plt.barh(bonus_data.keys(), bonus_data.values(), color='lightcoral')
        plt.xlabel("Total Bonus")
        plt.ylabel("Department")
        st.pyplot(plt)