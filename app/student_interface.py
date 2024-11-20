import streamlit as st
import plotly.graph_objects as go
from datetime import date, timedelta
import time
import matplotlib.pyplot as plt

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

    # Display Recommended Course (from session state)
    if "recommended_course" in st.session_state:
        course = st.session_state.recommended_course
        st.subheader("Recommended Course")
        st.write(f"- [{course['name']}]({course['link']})")
        st.write(f"- [{course['name1']}]({course['link1']})")

    # Menu Options (Centered and Horizontal)
    menu = st.radio(
        "Select a Section",
        ["Home Page", "Assignment Tracking", "Report", "Reverse Timer Clock", "Milestone"],
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
