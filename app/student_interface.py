import streamlit as st
import datetime
import time
import matplotlib.pyplot as plt
import pandas as pd
import os

def student_interface():
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
    st.title("Project Management Dashboard")

    # Menu Options (Centered and Horizontal)
    menu = st.radio(
        "Select a Section",
        ["Home Page", "Progress Update", "Assignment Tracking", "Report", "Reverse Timer Clock", "Milestone"],
        horizontal=True,  # Display menu options horizontally
        label_visibility="collapsed"
    )

    # Render Content Based on Selection
    if menu == "Home Page":
        st.header("Home Page")

        # Dummy data for the pie chart
        labels = ["Completed Tasks", "Pending Tasks", "In Progress"]
        sizes = [40, 30, 30]  # Percentages
        colors = ["#4CAF50", "#FFC107", "#FF5722"]

        # Create the pie chart
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
        ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
        st.pyplot(fig)

    elif menu == "Progress Update":
        st.header("Progress Update")
        st.write("Fill out the form to update your progress.")

        # Input Fields
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        update_description = st.text_area("Update Description")
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        comments = st.text_area("Comments for Instructor/Mentor")

        # Submit button
        if st.button("Submit Progress Update"):
            # Create a DataFrame to store the data
            data = {
                "Name": [name],
                "Email": [email],
                "Phone Number": [phone],
                "Update Description": [update_description],
                "Time": [current_time],
                "Comments": [comments]
            }
            df = pd.DataFrame(data)

            # Check if the CSV file already exists
            csv_file = "Progress_tracking.csv"
            if os.path.exists(csv_file):
                # Append to the existing file
                existing_df = pd.read_csv(csv_file)
                updated_df = pd.concat([existing_df, df], ignore_index=True)
                updated_df.to_csv(csv_file, index=False)
            else:
                # Create a new file
                df.to_csv(csv_file, index=False)

            st.success("Progress update submitted and saved successfully!")

    elif menu == "Tracking and Milestone":
        st.header("Tracking and Milestone")
        st.write("Set and view milestones for your project.")
        milestone_title = st.text_input("Milestone Title")
        milestone_date = st.date_input("Set Milestone Date", datetime.date.today())
        if st.button("Add Milestone"):
            if milestone_title:
                st.success(f"Milestone '{milestone_title}' added for {milestone_date}!")
            else:
                st.warning("Please enter a milestone title.")

    elif menu == "Report":
        st.header("Report")
        st.write("Generate and upload project reports.")
        report_file = st.file_uploader("Upload your report", type=["pdf", "docx", "xlsx"])
        if report_file:
            st.success(f"'{report_file.name}' uploaded successfully!")
        if st.button("Download Sample Report"):
            st.download_button(
                label="Download",
                data="Sample Report Content",
                file_name="sample_report.txt",
                mime="text/plain"
            )

    elif menu == "Reverse Timer Clock":
        st.header("Reverse Timer Clock")
        st.write("Countdown Timer for 15 Days")
        total_seconds = 15 * 24 * 60 * 60  # 15 days * 24 hours * 60 minutes * 60 seconds
        if st.button("Start 15-Day Timer"):
            st.write("Countdown Timer Started!")
            placeholder = st.empty()
            while total_seconds:
                days, remainder = divmod(total_seconds, 86400)
                hours, remainder = divmod(remainder, 3600)
                minutes, seconds = divmod(remainder, 60)
                timer = f"{days:02d}d:{hours:02d}h:{minutes:02d}m:{seconds:02d}s"
                placeholder.markdown(f"## {timer}")
                time.sleep(1)
                total_seconds -= 1
            placeholder.markdown("## Time's Up!")
