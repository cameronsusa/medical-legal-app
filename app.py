import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Medical Records Organizer", layout="wide")

# Authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("Secure Login")
    password = st.text_input("Enter password", type="password")
    if password == "demo123":
        st.session_state.authenticated = True
        st.rerun()
    else:
        st.warning("Enter password to continue")
    st.stop()

# Main App
st.title("Medical Records Organizer")
st.caption("Attorney-Client Privileged Workspace")

tabs = st.tabs(["Upload", "Chronology", "Duplicates", "Trends", "Summary", "Preferences", "Audit Log", "Export"])

if "records" not in st.session_state:
    st.session_state.records = []

if "audit_log" not in st.session_state:
    st.session_state.audit_log = []

def log_action(action):
    st.session_state.audit_log.append(f"{datetime.now()} — {action}")

with tabs[0]:
    st.header("Upload Medical Records")
    uploaded_files = st.file_uploader("Upload PDFs or images", accept_multiple_files=True)
    if uploaded_files:
        for file in uploaded_files:
            st.session_state.records.append(file)
            log_action(f"Uploaded file: {file.name}")
        st.success("Files uploaded successfully.")

with tabs[1]:
    st.header("Chronology")
    if st.session_state.records:
        for file in st.session_state.records:
            st.write(file.name)
    else:
        st.info("No files uploaded yet.")

with tabs[2]:
    st.header("Duplicate Detection")
    st.write("Duplicate detection placeholder — will flag similar filenames or content.")

with tabs[3]:
    st.header("Trends & Graphs")
    st.write("Graphs will appear here once lab/vital data is added.")

with tabs[4]:
    st.header("AI Summary")
    st.text_area("Editable Case Summary", height=300)

with tabs[5]:
    st.header("Customization Preferences")
    st.checkbox("Automatically group records by discipline")
    st.checkbox("Move duplicates to separate section instead of deleting")
    st.checkbox("Normalize date formats")
    st.checkbox("Flag low-confidence OCR sections")

with tabs[6]:
    st.header("Audit Log")
    for entry in st.session_state.audit_log:
        st.write(entry)

with tabs[7]:
    st.header("Export")
    st.button("Export Chronology as PDF")
