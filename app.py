import streamlit as st
import datetime
import dateformat
import automatelogin
import getdf

marks_list = []
login_form = st.form("login_form")

usn = login_form.text_input("enter your USN")
usn = usn.upper()

dob = login_form.date_input("enter your DOB", value=datetime.date(2004, 1, 1))
day, month, year = dateformat.getpass(dob)
submit_btn = login_form.form_submit_button("submit")


if submit_btn:
    st.markdown("---")
    marks_list = automatelogin.fetch_marks(usn, day, month, year)
    df = getdf.get_df(marks_list)
    st.bar_chart(data=df, x='Subject', y='Marks')
