import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime
import pandas as pd

# pip install streamlit 
# pip install streamlit-option-menu
# streamlit run app/main.py --server.port 8501 --server.address 0.0.0.0
# run tasks



st.set_page_config(layout="wide")

# --- CSS Styling ---
st.markdown("""
<style>
.card {
    display: flex;
    align-items: center;
    background: #1F1F26;
    border-radius: 18px;
    padding: 14px 18px;
    margin-bottom: 0px;  
    font-family: Arial, sans-serif;
    gap: 20px;
    color: white;
}

.courseID { background: #FF4D4F; border-radius: 14px; padding: 10px; text-align: center; width: 100px; font-weight: bold; }
.courseName { width: 200px; }
.courseInstructor { width: 180px; }
.date { width: 150px; }
.Time { width: 150px; }
.status { width: 120px; }
.Attendance { width: 150px; }

.header { font-weight: bold; color: #999; text-align: left; padding-left: 10px; }
.separator { border-top: 1px solid #555; margin: 6px 0; }
</style>
""", unsafe_allow_html=True)

# --- Function to render a module ---
def module_line(courseID, courseName, instructor, date, Time, status, current, total):

    # Columns for module content
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1,2,2,1.5,1.5,1.5,2])

    col1.markdown(f'<div class="courseID">{courseID}</div>', unsafe_allow_html=True)
    col2.markdown(f'<div class="courseName">{courseName}</div>', unsafe_allow_html=True)
    col3.markdown(f'<div class="courseInstructor">{instructor}</div>', unsafe_allow_html=True)
    col4.markdown(f'<div class="date">{date}</div>', unsafe_allow_html=True)
    col5.markdown(f'<div class="Time">{Time}</div>', unsafe_allow_html=True)
    col6.markdown(f'<div class="status">{status}</div>', unsafe_allow_html=True)
    col7.markdown(f'<div class="Attendance"><b>Here:</b> {current} &nbsp; | &nbsp; <b>Total:</b> {total}</div>', unsafe_allow_html=True)
    # Add a thin line separator below each module
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)


# Mock sessions data
sessions_data = {
    "SC1001": [
        ["Physics 101", "Dr Tan", "01-02-2026", "10:00 AM", "Completed", 28, 30],
        ["Physics 101", "Dr Tan", "02-02-2026", "2:00 PM", "Active", 15, 30]
    ],
    "SC1002": [
        ["Math 101", "Dr Lim", "01-02-2026", "11:00 AM", "Active", 20, 30],
        ["Math 101", "Dr Lim", "02-02-2026", "3:00 PM", "Completed", 30, 30]
    ],
    "SC1003": [
        ["Biology 101", "Dr Loh", "03-02-2026", "10:00 AM", "Active", 12, 30],
        ["Biology 101", "Dr Loh", "04-02-2026", "2:00 PM", "Completed", 29, 30]
    ],
    "SC1004": [
        ["Chemistry 101", "Dr Tan", "03-02-2026", "11:00 AM", "Active", 20, 30],
        ["Chemistry 101", "Dr Tan", "04-02-2026", "3:00 PM", "Completed", 28, 30]
    ],
    "SC1005": [
        ["Science 101", "Dr Ng", "05-02-2026", "10:00 AM", "Active", 14, 30],
        ["Science 101", "Dr Ng", "06-02-2026", "2:00 PM", "Active", 10, 30]
    ],
    "SC1006": [
        ["History 101", "Dr Lim", "05-02-2026", "11:00 AM", "Completed", 27, 30],
        ["History 101", "Dr Lim", "06-02-2026", "3:00 PM", "Active", 15, 30]
    ],
    "SC1007": [
        ["Geography 101", "Dr Loh", "07-02-2026", "10:00 AM", "Active", 8, 30],
        ["Geography 101", "Dr Loh", "08-02-2026", "2:00 PM", "Completed", 29, 30]
    ],
    "SC1008": [
        ["English 101", "Dr Tan", "07-02-2026", "11:00 AM", "Active", 12, 30],
        ["English 101", "Dr Tan", "08-02-2026", "3:00 PM", "Completed", 30, 30]
    ],
    "SC1009": [
        ["Economics 101", "Dr Ng", "09-02-2026", "10:00 AM", "Active", 18, 30],
        ["Economics 101", "Dr Ng", "10-02-2026", "2:00 PM", "Active", 8, 30]
    ],
    "SC1010": [
        ["Art 101", "Dr Loh", "09-02-2026", "11:00 AM", "Completed", 30, 30],
        ["Art 101", "Dr Loh", "10-02-2026", "3:00 PM", "Active", 12, 30]
    ],
    "SC1011": [
        ["Music 101", "Dr Tan", "11-02-2026", "10:00 AM", "Active", 15, 30],
        ["Music 101", "Dr Tan", "12-02-2026", "2:00 PM", "Completed", 30, 30]
    ],
    "SC1012": [
        ["Drama 101", "Dr Ng", "11-02-2026", "11:00 AM", "Active", 10, 30],
        ["Drama 101", "Dr Ng", "12-02-2026", "3:00 PM", "Completed", 25, 30]
    ],
    "SC1013": [
        ["PE 101", "Dr Lim", "13-02-2026", "10:00 AM", "Active", 18, 30],
        ["PE 101", "Dr Lim", "14-02-2026", "2:00 PM", "Completed", 30, 30]
    ],
    "SC1014": [
        ["Computer 101", "Dr Loh", "13-02-2026", "11:00 AM", "Active", 20, 30],
        ["Computer 101", "Dr Loh", "14-02-2026", "3:00 PM", "Completed", 28, 30]
    ],
    "SC1015": [
        ["Philosophy 101", "Dr Tan", "15-02-2026", "10:00 AM", "Active", 12, 30],
        ["Philosophy 101", "Dr Tan", "16-02-2026", "2:00 PM", "Completed", 30, 30]
    ],
    "SC1016": [
        ["Psychology 101", "Dr Ng", "15-02-2026", "11:00 AM", "Active", 18, 30],
        ["Psychology 101", "Dr Ng", "16-02-2026", "3:00 PM", "Completed", 22, 30]
    ],
    "SC1017": [
        ["Sociology 101", "Dr Lim", "17-02-2026", "10:00 AM", "Active", 12, 30],
        ["Sociology 101", "Dr Lim", "18-02-2026", "2:00 PM", "Completed", 29, 30]
    ],
    "SC1018": [
        ["Anthropology 101", "Dr Loh", "17-02-2026", "11:00 AM", "Active", 15, 30],
        ["Anthropology 101", "Dr Loh", "18-02-2026", "3:00 PM", "Completed", 30, 30]
    ],
    "SC1019": [
        ["Geology 101", "Dr Tan", "19-02-2026", "10:00 AM", "Active", 20, 30],
        ["Geology 101", "Dr Tan", "20-02-2026", "2:00 PM", "Completed", 30, 30]
    ],
    "SC1020": [
        ["Astronomy 101", "Dr Ng", "19-02-2026", "11:00 AM", "Active", 12, 30],
        ["Astronomy 101", "Dr Ng", "20-02-2026", "3:00 PM", "Completed", 28, 30]
    ],
    "SC1021": [
        ["Environmental 101", "Dr Lim", "21-02-2026", "10:00 AM", "Active", 15, 30],
        ["Environmental 101", "Dr Lim", "22-02-2026", "2:00 PM", "Completed", 30, 30]
    ],
    "SC1022": [
        ["Engineering 101", "Dr Loh", "21-02-2026", "11:00 AM", "Active", 10, 30],
        ["Engineering 101", "Dr Loh", "22-02-2026", "3:00 PM", "Completed", 28, 30]
    ],
    "SC1023": [
        ["Robotics 101", "Dr Tan", "23-02-2026", "10:00 AM", "Active", 18, 30],
        ["Robotics 101", "Dr Tan", "24-02-2026", "2:00 PM", "Completed", 30, 30]
    ],
    "SC1024": [
        ["AI 101", "Dr Ng", "23-02-2026", "11:00 AM", "Active", 12, 30],
        ["AI 101", "Dr Ng", "24-02-2026", "3:00 PM", "Completed", 30, 30]
    ],
    "SC1025": [
        ["Statistics 101", "Dr Lim", "25-02-2026", "10:00 AM", "Active", 15, 30],
        ["Statistics 101", "Dr Lim", "26-02-2026", "2:00 PM", "Completed", 30, 30]
    ],
    "SC1026": [
        ["Calculus 101", "Dr Loh", "25-02-2026", "11:00 AM", "Active", 10, 30],
        ["Calculus 101", "Dr Loh", "26-02-2026", "3:00 PM", "Completed", 28, 30]
    ],
    "SC1027": [
        ["Literature 101", "Dr Tan", "27-02-2026", "10:00 AM", "Active", 18, 30],
        ["Literature 101", "Dr Tan", "28-02-2026", "2:00 PM", "Completed", 30, 30]
    ],
    "SC1028": [
        ["Language 101", "Dr Ng", "27-02-2026", "11:00 AM", "Active", 12, 30],
        ["Language 101", "Dr Ng", "28-02-2026", "3:00 PM", "Completed", 30, 30]
    ],
}

attendance_data = {
    "SC1001": {
        "Week 1": ["Alice Tan", "Brian Lim", "Cheryl Wong"],
        "Week 2": ["Alice Tan", "Daniel Koh"],
        "Week 3": ["Brian Lim", "Cheryl Wong"],
        "Week 4": ["Alice Tan", "Brian Lim", "Daniel Koh"]
    }
}


#For CSV Export
# sessions_dict = { "SC1001": [ [...], [...]], "SC1002": [ [...], [...]] ... }
# Flatten the dictionary into a list of rows
flattened_data = []
for module_code, sessions in sessions_data.items():
    for session in sessions:
        # session = [Module Name, Instructor, Date, Time, Status, Current, Total]
        flattened_data.append([module_code] + session)  # prepend module code

# Create DataFrame
df = pd.DataFrame(
    flattened_data,
    columns=["Module Code", "Module Name", "Instructor", "Date", "Time", "Status", "Current", "Total"]
)

# Convert to CSV
csv_data = df.to_csv(index=False).encode('utf-8')  # ready for download

if "filter_applied" not in st.session_state:
    st.session_state.filter_applied = False

st.title("📚 Sessions Dashboard")
st.markdown("---")

# Place this at the top of your main page (not inside the sidebar)
selected = option_menu(
menu_title=None, # Usually better to keep it None for horizontal bars
options=["View Sessions", "Create Sessions", "Session Details"], 
icons=["graph-up", "patch-check", "clock-history", "file-earmark-text"], 
menu_icon="cast", 
default_index=0,
orientation="horizontal",
)


if selected == "View Sessions":
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        status_filter = st.selectbox("Filter by Status:", ["All", "Active", "Completed", "Cancelled"])
    with col2:
        course_filter = st.multiselect("Filter by module code:",options=list(sessions_data.keys()))
    with col3:
        date_range = st.date_input("Select Start and End Date (Y-M-D):", [])
        if len(date_range) == 2:
            start_date, end_date = date_range
        else:
            start_date = end_date = None
    with col4:     
        filter_button = st.button("Filter", use_container_width=True)
        if st.button("Export to CSV", use_container_width=True):
            # Use download_button with `key` and `on_click` trick
            st.download_button(
                label="Click to Download",   # temporary label
                data=csv_data,
                file_name="Sessions.csv",
                mime="text/csv",
                key="download_now",
                help="Automatically downloads CSV",
                use_container_width=True
            )
    
        # --- Example modules ---
    # --- Header row (aligned left) ---
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1,2,2,1.5,1.5,1.5,2])
    col1.markdown('<div class="header">Course ID</div>', unsafe_allow_html=True)
    col2.markdown('<div class="header">Course Name</div>', unsafe_allow_html=True)
    col3.markdown('<div class="header">Instructor</div>', unsafe_allow_html=True)
    col4.markdown('<div class="header">Date</div>', unsafe_allow_html=True)
    col5.markdown('<div class="header">Time</div>', unsafe_allow_html=True)
    col6.markdown('<div class="header">Status</div>', unsafe_allow_html=True)
    col7.markdown('<div class="header">Attendance</div>', unsafe_allow_html=True)
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    if filter_button:
        st.session_state.filter_applied = True            

    if st.session_state.filter_applied:
        filtered_modules = []
        st.session_state.filter_applied = True      #T/F State remembered

        for module_code, sessions in sessions_data.items():  # iterate over module codes
            for session in sessions:
                # session = [Module Name, Instructor, Date, Time, Status, Current, Total]
                courseName, instructor, date_str, Time, status, current, total = session

                # Convert date string to datetime.date
                module_date = datetime.strptime(date_str, "%d-%m-%Y").date()

                # Apply filters
                status_match = (status_filter == "All") or (status == status_filter)
                course_match = (not course_filter) or (module_code in course_filter)
                
                if start_date is not None and end_date is not None:
                    date_match = start_date <= module_date <= end_date
                else:
                    date_match = True

                if status_match and course_match and date_match:
                    filtered_modules.append([module_code, courseName, instructor, date_str, Time, status, current, total])

        if filtered_modules:
            st.write("Showing filtered modules:")
            for module in filtered_modules:
                module_line(
                    module[0],  # module_code
                    module[1],  # courseName
                    module[2],  # instructor
                    module[3],  # date
                    module[4],  # Time
                    module[5],  # status
                    module[6],  # current
                    module[7]   # total
                )
        else:
            st.info("No modules match your filters.")
            















elif selected == "Create Sessions":
    with st.form("create_session_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            course_code = st.text_input("Course Code", placeholder="e.g., SC1001")
            course_coordinator = st.text_input("Prof. in Charge", placeholder="e.g., Dr Lim")
        with col2:
            course_name = st.text_input("Course Code", placeholder="e.g., Linear Algebra")
            course_students = st.number_input("Max Students", placeholder="e.g., 50", min_value=1,step=1)
        with col3:
            date_range = st.date_input("Select Date (Y-M-D):")
            course_time = st.time_input("Select Time")

        course_submitted = st.form_submit_button("Create Session", use_container_width=True)
                
        if course_submitted:
            # TODO: Send to backend API
            st.info(f" Session '{course_name}' created successfully!")









elif selected == "Session Details":
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        course_filter = st.selectbox("Filter by module code:",options=list(sessions_data.keys()))
    with col2:
        session_filter = st.multiselect("Filter by sessions code:",options=list(sessions_data.keys()))
    with col3:
        date_range = st.date_input("Select Start and End Date (Y-M-D):", [])
        if len(date_range) == 2:
            start_date, end_date = date_range
        else:
            start_date = end_date = None
    with col4:     
        if st.button("Export to CSV", use_container_width=True):
            # Use download_button with `key` and `on_click` trick
            st.download_button(
                label="Click to Download",   # temporary label
                data=csv_data,
                file_name="Sessions.csv",
                mime="text/csv",
                key="download_now",
                help="Automatically downloads CSV",
                use_container_width=True
            )
    
        # --- Example modules ---
    # --- Header row (aligned left) ---
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1,2,2,1.5,1.5,1.5,2])
    col1.markdown('<div class="header">Course ID</div>', unsafe_allow_html=True)
    col2.markdown('<div class="header">Course Name</div>', unsafe_allow_html=True)
    col3.markdown('<div class="header">Instructor</div>', unsafe_allow_html=True)
    col4.markdown('<div class="header">Date</div>', unsafe_allow_html=True)
    col5.markdown('<div class="header">Time</div>', unsafe_allow_html=True)
    col6.markdown('<div class="header">Status</div>', unsafe_allow_html=True)
    col7.markdown('<div class="header">Attendance</div>', unsafe_allow_html=True)
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    filtered_modules = []

    for module_code, sessions in sessions_data.items():  # iterate over module codes
        for session in sessions:
            # session = [Module Name, Instructor, Date, Time, Status, Current, Total]
            courseName, instructor, date_str, Time, status, current, total = session

            # Convert date string to datetime.date
            module_date = datetime.strptime(date_str, "%d-%m-%Y").date()

            # Apply filters
            course_match = (not course_filter) or (module_code in course_filter)
            
            if start_date is not None and end_date is not None:
                date_match = start_date <= module_date <= end_date
            else:
                date_match = True

            if course_match and date_match:
                filtered_modules.append([module_code, courseName, instructor, date_str, Time, status, current, total])

    if filtered_modules:
        st.write("Showing filtered modules:")
        for module in filtered_modules:
            module_line(
                module[0],  # module_code
                module[1],  # courseName
                module[2],  # instructor
                module[3],  # date
                module[4],  # Time
                module[5],  # status
                module[6],  # current
                module[7]   # total
            )
    else:
        st.info("No modules match your filters.")