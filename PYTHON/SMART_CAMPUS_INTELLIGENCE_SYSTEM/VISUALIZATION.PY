import pandas as pd
import matplotlib.pyplot as plt


def show_visualizations(df):

    # Create a figure with six graphs
    fig, axes = plt.subplots(2, 3, figsize=(16, 9))

    # 1. Student Marks Graph
    axes[0, 0].bar(df["Name"], df["Marks"])

    axes[0, 0].set_title("Student Academic Performance")
    axes[0, 0].set_xlabel("Student Name")
    axes[0, 0].set_ylabel("Marks")
    axes[0, 0].tick_params(axis="x", rotation=45)

    # 2. Pass and Fail Pie Chart
    passed = len(df[df["Marks"] >= 40])
    failed = len(df[df["Marks"] < 40])

    axes[0, 1].pie(
        [passed, failed],
        labels=["Passed", "Failed"],
        autopct="%1.1f%%",
        startangle=90
    )

    axes[0, 1].set_title("Pass and Fail Analysis")

    # 3. Sleep Hours Graph
    axes[0, 2].bar(df["Name"], df["Sleep_Hours"])

    axes[0, 2].set_title("Student Sleep Analysis")
    axes[0, 2].set_xlabel("Student Name")
    axes[0, 2].set_ylabel("Sleep Hours")
    axes[0, 2].tick_params(axis="x", rotation=45)

    # 4. Study Hours Graph
    axes[1, 0].bar(df["Name"], df["Study_Hours"])

    axes[1, 0].set_title("Student Study Analysis")
    axes[1, 0].set_xlabel("Student Name")
    axes[1, 0].set_ylabel("Study Hours")
    axes[1, 0].tick_params(axis="x", rotation=45)

    # 5. Screen Time Graph
    axes[1, 1].bar(df["Name"], df["Screen_Time"])

    axes[1, 1].set_title("Student Screen Time")
    axes[1, 1].set_xlabel("Student Name")
    axes[1, 1].set_ylabel("Screen Time")
    axes[1, 1].tick_params(axis="x", rotation=45)

    # 6. Attendance Graph
    axes[1, 2].bar(df["Name"], df["Attendance"])

    axes[1, 2].set_title("Student Attendance")
    axes[1, 2].set_xlabel("Student Name")
    axes[1, 2].set_ylabel("Attendance")
    axes[1, 2].tick_params(axis="x", rotation=45)

    # Adjust graph spacing
    plt.tight_layout()

    # Display all graphs
    plt.show()