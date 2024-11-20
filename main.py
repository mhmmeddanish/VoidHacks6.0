import streamlit as st
from PIL import Image
from student_interface import student_interface
from instructor_interface import instructor_interface
from mentor_interface import mentor_interface
from admin_interface import admin_interface

# Dummy user credentials (hard-coded for simplicity)
users = [
    {"email": "student@example.com", "password": "123", "role": "Student"},
    {"email": "instructor@example.com", "password": "123", "role": "Instructor"},
    {"email": "mentor@example.com", "password": "123", "role": "Mentor"},
    {"email": "admin@example.com", "password": "123", "role": "Admin"},
]

# Page configuration
st.set_page_config(
    page_title="Role-Based Dashboard",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Login page with two-column layout
def login():
    st.title("Welcome to Internship Management System")

    # Divide the screen into two columns
    col1, col2 = st.columns([1, 2])  # Adjust column widths as needed

    # Left column: Display an image
    with col1:
        image = Image.open("login_image.jpg")  # Replace with your image file path
        st.image(image, caption="Login Page", use_container_width=True)  # Updated parameter

    # Right column: Login form
    with col2:
        st.subheader("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        role = st.selectbox("Role", ["Student", "Instructor", "Mentor", "Admin"])
        login_button = st.button("Login")
    return email, password, role, login_button


# Middle page for additional student details
def student_middle_page():
    st.title("Student Details")
    st.write("Please provide additional information to proceed:")

    # Input fields
    name = st.text_input("Name")
    year = st.text_input("Year")
    branch = st.text_input("Branch")
    degree = st.text_input("Degree")
    interested_domain = st.text_input("Interested Domain")
    programming_familiarity = st.text_input("Programming Familiarity")
    coding_skills = st.text_input("Coding Skills")
    additional_info = st.text_input("Additional Info")



    submit_button = st.button("Submit")
    if submit_button:
        if name and year and interested_domain and degree and programming_familiarity and coding_skills and additional_info and branch:
            st.session_state.year = year
            st.session_state.branch = branch
            st.session_state.name = name
            st.session_state.degree = degree
            st.session_state.interested_domain = interested_domain
            st.session_state.programming_familiarity = programming_familiarity
            st.session_state.coding_skills = coding_skills
            st.session_state.additional_info = additional_info
            #st.session_state.areas_of_interest = areas_of_interest

            # Store the recommended course in session state
            st.session_state.recommended_course = {
                "name": "Machine Learning A-Z: AI, Python & R + ChatGPT Prize [2024]",
                "name1": "Python for Data Science and Machine Learning Bootcamp",
                "link": "https://example.com/ml-course",
                "link1": "https://example.com/mlccc-course"
            }
            st.session_state.middle_page_done = True
            st.rerun()  # Redirect to student interface
        else:
            st.error("Please fill in all the fields.")
    return name, year, degree, interested_domain, programming_familiarity, coding_skills, additional_info, branch


# Main app
def main():
    # State management to keep track of login
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.role = None
        st.session_state.middle_page_done = False

    if not st.session_state.authenticated:
        email, password, role, login_button = login()
        if login_button:
            # Authenticate user
            user = next((u for u in users if u["email"] == email and u["password"] == password and u["role"] == role),
                        None)
            if user:
                st.session_state.authenticated = True
                st.session_state.role = user["role"]
                st.success(f"Login successful! Redirecting to {role} interface...")
                st.rerun()
            else:
                st.error("Invalid credentials or role. Please try again.")

    elif st.session_state.role == "Student" and not st.session_state.get("middle_page_done", False):
        student_middle_page()

    else:
        if st.session_state.role == "Student":
            student_interface()
        elif st.session_state.role == "Instructor":
            instructor_interface()
        elif st.session_state.role == "Mentor":
            mentor_interface()
        elif st.session_state.role == "Admin":
            admin_interface()

        # Logout button
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.session_state.role = None
            st.session_state.middle_page_done = False
            st.rerun()


# Run the app
if __name__ == "__main__":
    main()
