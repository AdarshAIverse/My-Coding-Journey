def analyze_attendance(df):

    print("\n================================")
    print("       ATTENDANCE ANALYSIS")
    print("================================")

    # Check attendance column
    if "Attendance" not in df.columns:
        print("Attendance column not found!")
        return

    # Calculate average attendance
    average_attendance = df["Attendance"].mean()

    print("\nAverage Attendance:",
          round(average_attendance, 2), "%")

    # Highest attendance
    highest = df["Attendance"].max()

    print("Highest Attendance:", highest, "%")

    # Lowest attendance
    lowest = df["Attendance"].min()

    print("Lowest Attendance:", lowest, "%")

    # Students with low attendance
    low_attendance = df[df["Attendance"] < 75]

    print("\nStudents with Attendance Below 75%:")

    if len(low_attendance) > 0:
        print(low_attendance[["Name", "Attendance"]])
    else:
        print("No students have low attendance.")

    # Attendance status
    print("\nIndividual Attendance Status:")

    for index, student in df.iterrows():

        if student["Attendance"] >= 75:
            status = "Eligible"
        else:
            status = "Low Attendance"

        print(student["Name"], ":", status)

    print("\nAttendance Analysis Completed!")