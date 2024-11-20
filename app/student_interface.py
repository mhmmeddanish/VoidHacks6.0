import streamlit as st
import plotly.graph_objects as go
from datetime import date, timedelta
import time
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
from AI_help import stream_ollama_response

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
    st.title("Internship Management Dashboard")

    # Display Recommended Course (from session state)
    if "recommended_course" in st.session_state:
        course = st.session_state.recommended_course
        st.subheader("Recommended Course")
        st.write(f"- [{course['name']}]({course['link']})")
        st.write(f"- [{course['name1']}]({course['link1']})")

    # Menu Options (Centered and Horizontal)
    menu = st.radio(
        "Select a Section",
        ["Home Page", "AI Internship Guidance", "Assignment Tracking", "Report", "Reverse Timer Clock", "Milestone"],
        horizontal=True,  # Display menu options horizontally
        label_visibility="collapsed"
    )

    # Render Content Based on Selection
    if menu == "Home Page":
        st.header("Home Page")

        # Create two columns for the layout
        col1, col2 = st.columns(2)

        # Left column: Dummy Pie Chart
        with col1:
            st.subheader("Progress Distribution")
            labels = ["Completed Tasks", "Pending Tasks", "In Progress"]
            sizes = [40, 30, 30]  # Percentages
            colors = ["#4CAF50", "#FFC107", "#FF5722"]

            # Create the pie chart
            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
            ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
            st.pyplot(fig)

        # Right column: Progress Bar
        with col2:
            st.subheader("Overall Progress")
            st.progress(0.7)  # 70% progress (constant dummy value)

            # Leaderboard data
            leaderboard_data = pd.DataFrame({
                'Student': ['Omer', 'Mudassir', 'Danish', 'Vahaj', 'Zayab'],
                'Tasks Completed': [8, 6, 5, 7, 4],
                'Progress %': [80, 60, 50, 70, 40]
            })

            # Sort by tasks completed
            leaderboard_data = leaderboard_data.sort_values('Tasks Completed', ascending=False)

            # Display leaderboard
            st.subheader("Leaderboard")
            st.dataframe(leaderboard_data)

            # Progress visualization
            fig = px.bar(
                leaderboard_data,
                x='Student',
                y='Progress %',
                title='Student Progress Overview'
            )
            st.plotly_chart(fig)

            # Individual student details
            st.subheader("Student Task Details")
            selected_student = st.selectbox("Select Student", leaderboard_data['Student'])

            # Placeholder for detailed student task tracking
            task_details = pd.DataFrame({
                'Task Name': ['Project Proposal', 'Initial Research', 'Midterm Report', 'Final Presentation'],
                'Status': ['Completed', 'Completed', 'In Progress', 'Not Started']
            })
            st.dataframe(task_details)

    elif menu == "AI Internship Guidance":
        st.header("AI Internship Guidance")

        # Retrieve data from session state
        name = st.session_state.get("name", "N/A")
        year = st.session_state.get("year", "N/A")
        degree = st.session_state.get("degree", "N/A")
        interested_domain = st.session_state.get("interested_domain", "N/A")
        programming_familiarity = st.session_state.get("programming_familiarity", "N/A")
        coding_skills = st.session_state.get("coding_skills", "N/A")
        additional_info = st.session_state.get("additional_info", "N/A")
        branch = st.session_state.get("branch", "N/A")

        @st.cache_data
        def load_courses():
            return pd.read_csv("courses.csv")

        def generate_internship_prompt(name, degree, branch, year, interested_domain, programming_familiarity,
                                       coding_skills, additional_info):
            courses_df = load_courses()

            # Filter the courses based on the student's interested domain
            relevant_courses = courses_df[
                courses_df['areas_of_interest'].str.contains(interested_domain, case=False, na=False)]

            # Create the prompt with the necessary details
            prompt = f"""
            Hello AI, I am a student seeking guidance on finding suitable internships. Here is my information:

            Name: {name}
            Degree: {degree} (BSc, BE, B-Tech)
            Branch: {branch} (e.g., ECE, IT, CSE)
            Year of Study: {year}
            Interested Domain: {interested_domain} (e.g., Data Science, Web Development)
            Programming Familiarity Level: {programming_familiarity} (Beginner, Intermediate, Advanced)
            Coding Skills: {coding_skills} (e.g., Python, Java, C++)
            Additional Preferences Regarding Internships: {additional_info}

            Based on my profile and interests in {interested_domain}, I would like to know about the following:
            1. Relevant Courses: 
                - {', '.join(relevant_courses['courses_name'].values)} 

            2. Links to Courses:
                - {', '.join(relevant_courses['courses_links'].values)}

            3. Suggested Mentor(s) for these courses:
                - {', '.join(relevant_courses['mentors_name'].values)}

            Please guide me with internship opportunities, tips on applying, and any recommended resources or skills I should focus on to enhance my career prospects in {interested_domain}. Additionally, suggest specific companies or programs that align with my {degree} background and my current skill level. Also, provide any networking or project ideas that would be helpful for my growth.
            """
            return prompt

        prompt = generate_internship_prompt(name, degree, branch, year, interested_domain, programming_familiarity,
                                            coding_skills, additional_info)
        print(prompt)
        response = stream_ollama_response(prompt)
        # print(response)
        st.write(response)


    elif menu == "Assignment Tracking":
        st.header("Assignment Tracking")
        st.progress(0.4)

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

        # Countdown timer starts automatically
        total_seconds = 15 * 24 * 60 * 60  # 15 days * 24 hours * 60 minutes * 60 seconds
        placeholder = st.empty()
        st.write("Countdown Timer Started!")

        while total_seconds:
            days, remainder = divmod(total_seconds, 86400)
            hours, remainder = divmod(remainder, 3600)
            minutes, seconds = divmod(remainder, 60)
            timer = f"{days:02d}d:{hours:02d}h:{minutes:02d}m:{seconds:02d}s"
            placeholder.markdown(f"## {timer}")
            time.sleep(1)
            total_seconds -= 1

        placeholder.markdown("## Time's Up!")
    # Render Content Based on Selection
    elif menu == "Milestone":
        st.header("Milestone Tracker")

        # Dummy milestones
        milestones = {
            "2024-11-10": "Finalize Project Proposal",
            "2024-11-15": "Submit First Draft",
            "2024-11-20": "Complete Prototype",
            "2024-11-30": "Submit Final Report",
        }

        # Plotly-based calendar visualization
        def create_milestone_calendar(milestones):
            dates = list(milestones.keys())
            descriptions = list(milestones.values())

            # Create a scatter plot for milestone dates
            fig = go.Figure(
                data=go.Scatter(
                    x=dates,
                    y=[1] * len(dates),  # Dummy y-axis values
                    mode="markers",
                    marker=dict(size=10, color="blue"),
                    text=descriptions,
                    hoverinfo="text",
                )
            )

            # Customize layout
            fig.update_layout(
                title="Milestones Calendar",
                xaxis=dict(title="Date", tickformat="%Y-%m-%d"),
                yaxis=dict(visible=False),
                showlegend=False,
                margin=dict(l=40, r=40, t=40, b=40),
            )
            return fig

        # Display the calendar
        st.plotly_chart(create_milestone_calendar(milestones), use_container_width=True)

        # Date picker for milestone details
        selected_date = st.date_input("Select a date to view milestone:", min_value=date(2024, 1, 1), max_value=date(2024, 12, 31))

        # Display milestone details for selected date
        selected_date_str = selected_date.strftime("%Y-%m-%d")
        if selected_date_str in milestones:
            st.success(f"Milestone for {selected_date_str}: {milestones[selected_date_str]}")
        else:
            st.info("No milestone for the selected date.")
