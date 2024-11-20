import streamlit as st
from admin_mentor_management import mentor_management_page
from admin_student_tracking import student_tracking_page
from admin_mca_verification import mca_verification_page
from admin_dashboard import admin_dashboard
from admin_communication import discord_communication_page

def admin_interface():
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .center-menu {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: row;
            margin-bottom: 30px; /* Adjust spacing */
        }
        .menu-option {
            font-size: 20px;
            font-weight: bold;
            color: #0078d7;
            margin: 0 10px;
            padding: 10px 20px;
            border: 2px solid #0078d7;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .menu-option:hover {
            background-color: #0078d7;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Header Section
    st.title("Internship Management Dashboard")

    menu_selection = st.radio("Select a Section",
                              ["Dashboard", "Mentor Management", "Student Tracking", "MCA Verification",
                               "Communication"],
                              horizontal=True,  # Display menu options horizontally
                              label_visibility="collapsed"
                              )

    if menu_selection == "Dashboard":
        admin_dashboard()
    elif menu_selection == "Mentor Management":
        mentor_management_page()
    elif menu_selection == "Student Tracking":
        student_tracking_page()
    elif menu_selection == "MCA Verification":
        mca_verification_page()
    elif menu_selection == "Communication":
        discord_communication_page()
