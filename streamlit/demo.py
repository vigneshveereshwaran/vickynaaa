import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Manager",
    layout="centered"
)

st.title("Student Management System")

if "students" not in st.session_state:
    st.session_state.students = []

students = st.session_state.students

st.divider()

st.subheader("1.Add Student")
name = st.text_input("Student Name")
roll = st.text_input("Roll Number")
dept = st.text_input("Department ")

if st.button("Add"):
    if name and roll and dept:
        students.append({"Name": name, "Roll": roll, "Department": dept})
        st.success("Student added")
    else:
        st.warning("Please fill all of the details...")

st.divider()

st.header("Student List")
if students:
    df = pd.DataFrame(students)
    st.table(df)
else:
    st.info("No students yet. Add one above.")

st.divider()

st.header("Deleting Student")
if students:
    rolls = [s["Roll"] for s in students]
    roll_to_delete = st.selectbox("Select roll to delete", rolls)
    if st.button("Delete"):
        st.session_state.students = [s for s in students if s["Roll"] != roll_to_delete]
        st.success("Deleted")