import streamlit as st
from PIL import Image
from student_interface import student_interface
from instructor_interface import instructor_interface
from mentor_interface import mentor_interface
from admin_interface import admin_interface
import pandas as pd

# Dummy user credentials (hard-coded for simplicity)
users = [
    {"email": "student@example.com", "password": "123", "role": "Student"},
    {"email": "instructor@example.com", "password": "instructor123", "role": "Instructor"},
    {"email": "mentor@example.com", "password": "mentor123", "role": "Mentor"},
    {"email": "admin@example.com", "password": "admin123", "role": "Admin"},
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
        st.image(image, caption="Login Page", use_column_width=True)

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
    year = st.text_input("Year")
    branch = st.text_input("Branch")
    areas_of_interest = st.multiselect(
        "Areas of Interest",
        ["AI", "Machine Learning", "Data Science", "Web Development", "Cloud Computing", "Cybersecurity"]
    )

    submit_button = st.button("Submit")
    if submit_button:
        if year and branch and areas_of_interest:
            st.session_state.year = year
            st.session_state.branch = branch
            st.session_state.areas_of_interest = areas_of_interest

            # Recommend courses based on the areas of interest
            recommend_courses(areas_of_interest)
            st.session_state.middle_page_done = True
        else:
            st.error("Please fill in all the fields.")


# Function to recommend courses based on areas of interest
def recommend_courses(areas_of_interest):
    try:
        # Load the courses.csv file
        df = pd.read_csv("courses.csv")

        # Filter rows where the areas of interest match the user's input
        matching_courses = df[
            df["areas_of_interest"].apply(lambda x: any(area in x.split(",") for area in areas_of_interest))]

        if not matching_courses.empty:
            st.subheader("Recommended Courses")
            for _, row in matching_courses.iterrows():
                st.write(f"- [{row['course_name']}]({row['course_link']})")
        else:
            st.info("No matching courses found.")
    except Exception as e:
        st.error(f"Error loading courses: {e}")


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
