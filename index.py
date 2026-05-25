import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from views.home import show_home_page
from views.add_employee import show_add_employee
from views.employee_list import show_employee_list
from views.edit_delete import show_edit_delete
from views.statistics import show_statistics

st.set_page_config(page_title="Employee Management", page_icon=":briefcase:", layout="wide")
st.title("Employee Management Dashboard", text_alignment="center")

menu = st.sidebar.selectbox("Select Page", [
    "📊 Dashboard",
    "👥 Employee List",
    "➕ Add Employee",
    "📥 Edit & Delete",
    "📈 Statistics"])
DATABASE_FILE = './database.json'
if menu == '📊 Dashboard':
    show_home_page(db_file= DATABASE_FILE)
elif menu == '👥 Employee List':
    show_employee_list(db_file= DATABASE_FILE)
elif menu == '➕ Add Employee':
    show_add_employee(db_file= DATABASE_FILE)
elif menu == '📥 Edit & Delete':
    show_edit_delete(db_file= DATABASE_FILE)
elif menu == '📈 Statistics':
    show_statistics(db_file= DATABASE_FILE)
