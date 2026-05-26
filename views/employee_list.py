import streamlit as st
from helper import load_data
import pandas as pd
from io import BytesIO

def show_employee_list(db_file):
    st.header("Employee List")
    employees = load_data(db_file)
    
    if not employees:
        st.info("No employees found. Please add employees first.")
        return
    
    name = st.text_input("Search by Name")
    phone = st.text_input("Search by Phone")
    email = st.text_input("Search by Email")
    department = st.text_input("Search by Department")
    age_range = st.slider("Search by Age Range", 18, 65, (18, 65))
    
    filtered_employees = [emp for emp in employees if
                          (name.lower() in emp['name'].lower() if name else True) and
                          (department.lower() in emp['department'].lower() if department else True) and
                          (phone in emp['phone'] if phone else True) and
                          (email in emp['email'] if email else True) and
                          age_range[0] <= emp['age'] <= age_range[1]]

    if filtered_employees:
        st.table(filtered_employees)
    else:
        st.warning("No employees match the search criteria.")
        
    df = pd.DataFrame(filtered_employees)
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(
            writer,
            index=False,
            sheet_name='Employee List'
        )

        worksheet = writer.sheets['Employee List']

        for column in worksheet.columns:
            max_length = max(
                len(str(cell.value if cell.value else ""))
                for cell in column
            )

            worksheet.column_dimensions[
                column[0].column_letter
            ].width = max_length + 2
    excel_data = buffer.getvalue()
    st.download_button(
        label="Download Employee List as Excel",
        data=excel_data,
        file_name="employee_list.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )