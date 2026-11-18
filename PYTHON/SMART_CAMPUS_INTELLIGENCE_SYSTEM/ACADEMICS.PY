import numpy as np
import pandas as pd

def analyze_academics(df):

    # Extract marks
    marks = df["Marks"].to_numpy()

    # Calculate statistics
    average = np.mean(marks)
    highest = np.max(marks)
    lowest = np.min(marks)

    # Find topper
    topper = df.loc[df["Marks"].idxmax()]

    # Students below average
    below_average = df[df["Marks"] < average]

    # Student ranking
    result = df.copy()
    result["Rank"] = result["Marks"].rank(
        ascending=False, method="min"
    ).astype(int)

    # Pass and fail analysis
    passed = df[df["Marks"] >= 40]
    failed = df[df["Marks"] < 40]

    # Display academic analysis
    print("\n========== ACADEMIC ANALYSIS ==========")

    print("\nAverage Marks:", average)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)

    print("\nTOPPER NAME:", topper["Name"])
    print("\nTOPPER DETAILS")
    print(topper)

    print("\nSTUDENTS BELOW AVERAGE")
    print(below_average)

    print("\nSTUDENT RANKING")
    print(result.sort_values("Rank"))

    print("\nPASSED STUDENTS")
    print(passed)

    print("\nFAILED STUDENTS")
    print(failed)

    print("\nTotal Passed:", len(passed))
    print("Total Failed:", len(failed))