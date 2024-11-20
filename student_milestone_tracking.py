admin_student_tracking.pyimport streamlit as st
import pandas as pd
import plotly.express as px


def student_tracking_page():
    st.header("Student Milestone Tracking")

    # Leaderboard data
    leaderboard_data = pd.DataFrame({
        'Student': ['Omer', 'Mudassir', 'Danish', 'Vahaj', 'Zayab'],
        'Tasks Completed': [8, 6, 5, 7, 4],
        'Progress %': [80, 60, 50, 70, 40],
        'Marks Allocated': [None, None, None, None, None]  # Placeholder for marks
    })

    # Sort by tasks completed
    leaderboard_data = leaderboard_data.sort_values('Tasks Completed', ascending=False)

    # Display leaderboard
    st.subheader("Milestone Leaderboard")
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

    # Section for allocating marks
    st.subheader("Allocate Marks")
    marks_allocation = {}
    for student in leaderboard_data['Student']:
        marks_allocation[student] = st.slider(
            f"Allocate Marks for {student}",
            min_value=0,
            max_value=100,
            value=0,
            key=f"marks_{student}"
        )

    # Display the marks allocation table
    leaderboard_data['Marks Allocated'] = leaderboard_data['Student'].map(marks_allocation)
    st.subheader("Marks Allocation Overview")
    st.dataframe(leaderboard_data)


# Run the student tracking page
if _name_ == "_main_":
    student_tracking_page()
