import numpy as np
import pandas as pd


def analyze_lifestyle(df):

    sleep = df["Sleep_Hours"]
    study = df["Study_Hours"]
    screen = df["Screen_Time"]

    # Calculate averages
    avg_sleep = np.mean(sleep)
    avg_study = np.mean(study)
    avg_screen = np.mean(screen)

    print("\n========== LIFESTYLE ANALYSIS ==========")

    print("\nAverage Sleep Hours:", avg_sleep)
    print("Average Study Hours:", avg_study)
    print("Average Screen Time:", avg_screen)

    # Students with low sleep
    print("\nSTUDENTS WITH LOW SLEEP")
    print(df[df["Sleep_Hours"] < 6])

    # Students with high screen time
    print("\nSTUDENTS WITH HIGH SCREEN TIME")
    print(df[df["Screen_Time"] > 5])

    # Students with high study hours
    print("\nSTUDENTS WITH HIGH STUDY HOURS")
    print(df[df["Study_Hours"] >= 5])

    print("\nLIFESTYLE ANALYSIS COMPLETED")