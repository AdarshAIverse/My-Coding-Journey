import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------------------
# 1. PAGE CONFIGURATION
# -----------------------------------------

st.set_page_config(
    page_title="Smart Campus Intelligence System",
    page_icon="🎓",
    layout="wide"
)


# -----------------------------------------
# 2. LOAD DATA
# -----------------------------------------

st.sidebar.title("Dashboard Controls")

uploaded_file = st.sidebar.file_uploader(
    "Upload Student CSV",
    type=["csv"]
)

try:
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_csv("STUDENTS.CSV")

except Exception as e:
    st.error(f"Unable to load CSV file: {e}")
    st.stop()


# -----------------------------------------
# 3. VALIDATE DATA
# -----------------------------------------

required_columns = ["Name", "Marks"]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    st.error(
        "Missing required columns: "
        + ", ".join(missing_columns)
    )
    st.stop()


numeric_columns = [
    "Attendance",
    "Study_Hours",
    "Marks",
    "Sleep_Hours",
    "Screen_Time",
    "Assignments"
]
for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )
# DATA VALIDATION

# Check required columns
required_columns = ["Name", "Marks"]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    st.error(f"Missing required columns: {missing_columns}")
    st.stop()

# Clean student names
df["Name"] = df["Name"].astype("string").str.strip()

# Remove invalid records
df = df.dropna(subset=["Name", "Marks"])
df = df[df["Name"] != ""]

# Check valid records
if df.empty:
    st.error("No valid student records found.")
    st.stop()

# Check marks range
if ((df["Marks"] < 0) | (df["Marks"] > 100)).any():
    st.warning("Some marks are outside the expected 0-100 range.")

st.success("Student data validation completed successfully.")
# -----------------------------------------
# 4. PROJECT HEADING
# -----------------------------------------

st.title("🎓 SMART CAMPUS INTELLIGENCE SYSTEM")

st.write(
    "Student Academic Performance and "
    "Lifestyle Analysis Dashboard"
)

st.caption(
    "A data-driven approach to understanding "
    "student performance beyond grades."
)

st.divider()


# -----------------------------------------
# 5. SIDEBAR FILTERS
# -----------------------------------------

st.sidebar.subheader("Student Filters")

min_marks = float(df["Marks"].min())
max_marks = float(df["Marks"].max())

if min_marks < max_marks:
    selected_marks = st.sidebar.slider(
        "Select Marks Range",
        min_value=min_marks,
        max_value=max_marks,
        value=(min_marks, max_marks)
    )

    filtered_df = df[
        df["Marks"].between(
            selected_marks[0],
            selected_marks[1]
        )
    ].copy()

else:
    filtered_df = df.copy()
    st.sidebar.info("All students have the same marks.")

search_name = st.sidebar.text_input(
    "Search Student Name"
)

if search_name:
    filtered_df = filtered_df[
        filtered_df["Name"].str.contains(
            search_name,
            case=False,
            na=False
        )
    ]


# -----------------------------------------
# 6. ACADEMIC CALCULATIONS
# -----------------------------------------

total_students = len(filtered_df)

if total_students == 0:
    st.warning("No students match the selected filters.")
    st.stop()

average_marks = filtered_df["Marks"].mean()
highest_marks = filtered_df["Marks"].max()
lowest_marks = filtered_df["Marks"].min()

topper = filtered_df.loc[
    filtered_df["Marks"].idxmax()
]

passed = len(
    filtered_df[filtered_df["Marks"] >= 40]
)

failed = len(
    filtered_df[filtered_df["Marks"] < 40]
)


# -----------------------------------------
# 7. ACADEMIC OVERVIEW
# -----------------------------------------

st.subheader("📊 Academic Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Students",
    total_students
)

col2.metric(
    "Average Marks",
    round(average_marks, 2)
)

col3.metric(
    "Highest Marks",
    round(highest_marks, 2)
)

col4.metric(
    "Lowest Marks",
    round(lowest_marks, 2)
)

col5, col6 = st.columns(2)

col5.metric(
    "Class Topper",
    str(topper["Name"])
)

col6.metric(
    "Pass Percentage",
    f"{passed / total_students * 100:.1f}%"
)


# -----------------------------------------
# 8. ATTENDANCE OVERVIEW
# -----------------------------------------

if "Attendance" in filtered_df.columns:

    st.divider()
    st.subheader("📅 Attendance Overview")

    average_attendance = filtered_df["Attendance"].mean()

    st.metric(
        "Average Attendance",
        f"{average_attendance:.2f}%"
    )


# -----------------------------------------
# 9. PASS AND FAIL ANALYSIS
# -----------------------------------------

st.divider()
st.subheader("Pass and Fail Analysis")

col1, col2 = st.columns(2)

col1.metric("Students Passed", passed)
col2.metric("Students Failed", failed)

fig, ax = plt.subplots()

ax.pie(
    [passed, failed],
    labels=["Passed", "Failed"],
    autopct="%1.1f%%",
    startangle=90
)

ax.set_title("Pass and Fail Distribution")

st.pyplot(fig)
plt.close(fig)


# -----------------------------------------
# 10. STUDENT PERFORMANCE GRAPHS
# -----------------------------------------

st.divider()
st.subheader("📈 Student Performance Graphs")

fig, axes = plt.subplots(
    2, 2,
    figsize=(14, 9)
)

axes[0, 0].bar(
    filtered_df["Name"],
    filtered_df["Marks"]
)

axes[0, 0].set_title("Student Marks")
axes[0, 0].tick_params(
    axis="x",
    rotation=45
)

if "Sleep_Hours" in filtered_df.columns:
    axes[0, 1].bar(
        filtered_df["Name"],
        filtered_df["Sleep_Hours"]
    )
    axes[0, 1].set_title("Sleep Hours")
    axes[0, 1].tick_params(
        axis="x",
        rotation=45
    )

if "Study_Hours" in filtered_df.columns:
    axes[1, 0].bar(
        filtered_df["Name"],
        filtered_df["Study_Hours"]
    )
    axes[1, 0].set_title("Study Hours")
    axes[1, 0].tick_params(
        axis="x",
        rotation=45
    )

if "Screen_Time" in filtered_df.columns:
    axes[1, 1].bar(
        filtered_df["Name"],
        filtered_df["Screen_Time"]
    )
    axes[1, 1].set_title("Screen Time")
    axes[1, 1].tick_params(
        axis="x",
        rotation=45
    )

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)


# -----------------------------------------
# 11. ATTENDANCE GRAPH
# -----------------------------------------

if "Attendance" in filtered_df.columns:

    st.subheader("Attendance Analysis")

    st.bar_chart(
        filtered_df.set_index("Name")["Attendance"]
    )


# -----------------------------------------
# 12. LIFESTYLE INSIGHTS
# -----------------------------------------

st.divider()
st.subheader("🌱 Student Lifestyle Insights")

if "Sleep_Hours" in filtered_df.columns:

    low_sleep = filtered_df[
        filtered_df["Sleep_Hours"] < 6
    ]

    st.write(
        f"Students sleeping less than 6 hours: "
        f"**{len(low_sleep)}**"
    )

    if not low_sleep.empty:
        st.dataframe(
            low_sleep[["Name", "Sleep_Hours"]],
            use_container_width=True
        )

if "Screen_Time" in filtered_df.columns:

    high_screen = filtered_df[
        filtered_df["Screen_Time"] > 5
    ]

    st.write(
        f"Students with screen time above 5 hours: "
        f"**{len(high_screen)}**"
    )

    if not high_screen.empty:
        st.dataframe(
            high_screen[["Name", "Screen_Time"]],
            use_container_width=True
        )

if "Attendance" in filtered_df.columns:

    low_attendance = filtered_df[
        filtered_df["Attendance"] < 75
    ]

    st.write(
        f"Students with attendance below 75%: "
        f"**{len(low_attendance)}**"
    )


# -----------------------------------------
# 13. HOLISTIC STUDENT SUCCESS INDEX
# -----------------------------------------

st.divider()
st.subheader("🏆 Holistic Student Success Index")

score_columns = [
    "Marks",
    "Attendance",
    "Sleep_Hours",
    "Study_Hours",
    "Screen_Time"
]

if all(col in filtered_df.columns for col in score_columns):

    index_df = filtered_df.copy()

    index_df["Academic_Score"] = (
        index_df["Marks"].clip(0, 100)
    )

    index_df["Attendance_Score"] = (
        index_df["Attendance"].clip(0, 100)
    )

    index_df["Sleep_Score"] = (
        index_df["Sleep_Hours"].clip(0, 8) / 8 * 100
    )

    index_df["Study_Score"] = (
        index_df["Study_Hours"].clip(0, 4) / 4 * 100
    )

    index_df["Screen_Score"] = (
        100 - index_df["Screen_Time"].clip(0, 10) * 10
    )

    index_df["Success_Index"] = (
        index_df["Academic_Score"] * 0.40
        + index_df["Attendance_Score"] * 0.20
        + index_df["Sleep_Score"] * 0.15
        + index_df["Study_Score"] * 0.15
        + index_df["Screen_Score"] * 0.10
    )

    index_df["Success_Index"] = (
        index_df["Success_Index"].round(2)
    )

    def classify_score(score):
        if score >= 80:
            return "Strong"
        elif score >= 60:
            return "Developing"
        else:
            return "Needs Support"

    index_df["Category"] = (
        index_df["Success_Index"].apply(classify_score)
    )

    st.write(
        "The index is an illustrative weighted score "
        "for this project, not a validated measure "
        "or prediction of student success."
    )

    st.dataframe(
        index_df[
            ["Name", "Success_Index", "Category"]
        ].sort_values(
            "Success_Index",
            ascending=False
        ),
        use_container_width=True
    )

    st.metric(
        "Average Holistic Success Index",
        f"{index_df['Success_Index'].mean():.2f}/100"
    )

else:

    st.info(
        "Add Marks, Attendance, Sleep_Hours, "
        "Study_Hours and Screen_Time columns "
        "to calculate the holistic index."
    )


# -----------------------------------------
# 14. STUDENT RANKING
# -----------------------------------------

st.divider()
st.subheader("🥇 Student Ranking")

ranking = filtered_df.copy()

ranking["Rank"] = ranking["Marks"].rank(
    ascending=False,
    method="min"
).astype(int)

ranking = ranking.sort_values(
    ["Rank", "Name"]
)

st.dataframe(
    ranking[["Rank", "Name", "Marks"]],
    use_container_width=True
)


# -----------------------------------------
# 15. COMPLETE STUDENT RECORDS
# -----------------------------------------

st.divider()
st.subheader("📋 Complete Student Records")

st.dataframe(
    filtered_df,
    use_container_width=True
)


# -----------------------------------------
# 16. DOWNLOAD REPORT
# -----------------------------------------

csv_data = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇️ Download Student Report",
    data=csv_data,
    file_name="student_analysis_report.csv",
    mime="text/csv"
)


# -----------------------------------------
# 17. FOOTER
# -----------------------------------------

st.divider()

st.caption(
    "Smart Campus Intelligence System | "
    "Student Data Analytics Project"
)
# ==========================================
# ADVANCED STUDENT DATA ANALYSIS
# ==========================================

st.divider()
st.title("Advanced Student Data Analysis")

# 1. Top 3 Students
st.subheader("Top 3 Performing Students")

top_students = filtered_df.nlargest(3, "Marks")

st.dataframe(
    top_students[["Name", "Marks"]],
    use_container_width=True
)

# 2. Students Requiring Academic Support
st.subheader("Students Requiring Academic Support")

if "Attendance" in filtered_df.columns:

    support_students = filtered_df[
        (filtered_df["Marks"] < 40) |
        (filtered_df["Attendance"] < 75)
    ]

else:

    support_students = filtered_df[
        filtered_df["Marks"] < 40
    ]

if len(support_students) > 0:

    st.warning(
        "These students may require additional academic support."
    )

    st.dataframe(
        support_students,
        use_container_width=True
    )

else:

    st.success(
        "No students meet the current support criteria."
    )


# 3. Relationship Between Attendance and Marks
st.subheader("Attendance vs Academic Performance")

if "Attendance" in filtered_df.columns:

    attendance_data = filtered_df.dropna(
        subset=["Attendance", "Marks"]
    )

    if len(attendance_data) >= 2:

        fig, ax = plt.subplots(figsize=(8, 5))

        ax.scatter(
            attendance_data["Attendance"],
            attendance_data["Marks"]
        )

        ax.set_xlabel("Attendance (%)")
        ax.set_ylabel("Marks")
        ax.set_title("Attendance vs Marks")

        st.pyplot(fig)
        plt.close(fig)

        correlation = attendance_data[
            ["Attendance", "Marks"]
        ].corr().iloc[0, 1]

        if pd.notna(correlation):

            st.write(
                "Correlation:",
                round(correlation, 2)
            )

    else:

        st.info("Not enough attendance data for comparison.")


# 4. Relationship Between Sleep and Marks
st.subheader("Sleep Hours vs Academic Performance")

if "Sleep_Hours" in filtered_df.columns:

    sleep_data = filtered_df.dropna(
        subset=["Sleep_Hours", "Marks"]
    )

    if len(sleep_data) >= 2:

        fig, ax = plt.subplots(figsize=(8, 5))

        ax.scatter(
            sleep_data["Sleep_Hours"],
            sleep_data["Marks"]
        )

        ax.set_xlabel("Sleep Hours")
        ax.set_ylabel("Marks")
        ax.set_title("Sleep Hours vs Marks")

        st.pyplot(fig)
        plt.close(fig)

        correlation = sleep_data[
            ["Sleep_Hours", "Marks"]
        ].corr().iloc[0, 1]

        if pd.notna(correlation):

            st.write(
                "Correlation:",
                round(correlation, 2)
            )

    else:

        st.info("Not enough sleep data for comparison.")