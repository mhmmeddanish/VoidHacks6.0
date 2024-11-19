import streamlit as st
import requests

# Base API URL
BASE_URL = "http://localhost:3000/api"

# Authentication
def login(email, password):
    response = requests.post(f"{BASE_URL}/auth/signin", json={"email": email, "password": password})
    return response.json()

# Role-Based Dashboards
def admin_dashboard():
    st.title("Admin Dashboard")
    st.write("Manage internships, reports, and users.")
    # Add admin-specific features here

def mentor_dashboard():
    st.title("Mentor Dashboard")
    st.write("Track assigned students and evaluate reports.")
    # Add mentor-specific features here

def student_dashboard():
    st.title("Student Dashboard")
    st.write("View and submit internship reports.")
    # Add student-specific features here

# Main Streamlit App
def main():
    st.sidebar.title("Navigation")
    menu = st.sidebar.radio("Menu", ["Login", "Admin", "Mentor", "Student"])

    if menu == "Login":
        st.title("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            user = login(email, password)
            if user.get("error"):
                st.error(user["error"])
            else:
                st.success(f"Welcome, {user['name']}!")
                if user["role"] == "ADMIN":
                    admin_dashboard()
                elif user["role"] == "MENTOR":
                    mentor_dashboard()
                elif user["role"] == "STUDENT":
                    student_dashboard()

    elif menu == "Admin":
        admin_dashboard()

    elif menu == "Mentor":
        mentor_dashboard()

    elif menu == "Student":
        student_dashboard()

if __name__ == "__main__":
    main()
