import streamlit as st

def instructor_interface():
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
    st.title("Instructor Dashboard")

    # Section 1: Dummy Data
    st.header("Dashboard Overview")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Number of Courses")
        st.info("12")  # Dummy data

    with col2:
        st.subheader("Number of Students Signed Up")
        st.info("450")  # Dummy data

    st.markdown("---")

    # Section 2: File Upload
    st.header("Upload Course Material")
    uploaded_file = st.file_uploader("Upload your file (PDF, DOCX, XLSX, etc.)", type=["pdf", "docx", "xlsx", "csv"])

    if uploaded_file:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")

    st.markdown("---")

    # Section 3: Generate Course with AI
    st.header("Generate Course with AI")
    if st.button("Generate"):
        st.warning("This feature is under development. Stay tuned for updates!")

    if st.button("Publish Course"):
        if uploaded_file:
            st.write("Course published")
        else:
            st.write("Upload the Course first")
