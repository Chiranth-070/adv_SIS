import streamlit as st
import datetime
import dateformat
import automatelogin
import getdf

login_form = st.form("login_form")

usn = login_form.text_input("enter your USN")
usn = usn.upper()
dob = login_form.date_input("enter your DOB", value=datetime.date(2004, 4, 19))
day, month, year = dateformat.getpass(dob)
submit_btn = login_form.form_submit_button("submit")


if submit_btn:
    marks_list, student_name, cgpa, sgpa = automatelogin.fetch_marks(usn, day, month, year)
    df1 = getdf.get_df(marks_list)
    df2 = getdf.get_sgpa(sgpa)
    st.write(f"👋 Hi! {student_name}")
    st.info(f"Current CGPA : {cgpa}")
    st.subheader("CIE marks graph :")
    st.bar_chart(data=df1, x='Subject', y='Marks')
    st.subheader("Sem-wise sgpa :")
    st.bar_chart(data=df2, x='SEM', y='sgpa')
