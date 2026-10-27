import streamlit as st
from roast import indexpdf

# Page configuration
st.set_page_config(
    page_title="Savage Resume Roaster",
    page_icon="🔥",
    layout="centered",
)

# App title
st.title("🔥 Savage Resume Roaster")
st.write(
    "Upload your resume and let AI roast it. "
    "Brutally honest feedback, with a recruiter's eye."
)

st.divider()

# PDF upload
uploaded_file = st.file_uploader(
    "📄 Upload your resume (PDF)",
    type=["pdf"],
    help="Upload a PDF containing selectable text.",
)

# Roast button
if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")

    if st.button("🔥 Roast My Resume", type="primary"):
        try:
            with st.spinner(
                "Analyzing your resume... sharpening the roast 🔥"
            ):
                # Call the function from roast.py
                result = indexpdf(uploaded_file)

            st.subheader("💀 Your Resume Roast")
            st.markdown(result)

        except Exception as e:
            st.error(f"Something went wrong: {e}")

else:
    st.info("Upload a PDF resume to get started.")

st.divider()

