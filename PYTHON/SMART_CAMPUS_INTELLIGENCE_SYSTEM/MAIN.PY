# ==========================================
# SMART CAMPUS INTELLIGENCE SYSTEM
# MAIN PYTHON FILE
# ==========================================

import pandas as pd

# Import project modules
from ACADEMICS import analyze_academics
from ATTENDANCE import analyze_attendance
from LIFESTYLE import analyze_lifestyle
from VISUALIZATION import show_visualizations


# ==========================================
# 1. LOAD STUDENT DATASET
# ==========================================

df = pd.read_csv("STUDENTS.CSV")


# ==========================================
# 2. PROJECT HEADING
# ==========================================

print("========================================")
print("     SMART CAMPUS INTELLIGENCE SYSTEM")
print("========================================")

print("\nStudent Academic Performance and")
print("Lifestyle Analysis System")


# ==========================================
# 3. DISPLAY STUDENT RECORDS
# ==========================================

print("\n========================================")
print("           STUDENT RECORDS")
print("========================================")

print(df)


# ==========================================
# 4. TOTAL NUMBER OF STUDENTS
# ==========================================

print("\nTotal Students:", len(df))


# ==========================================
# 5. DISPLAY FIRST FIVE STUDENTS
# ==========================================

print("\n========================================")
print("          FIRST FIVE STUDENTS")
print("========================================")

print(df.head())


# ==========================================
# 6. ACADEMIC PERFORMANCE ANALYSIS
# ==========================================

analyze_academics(df)


# ==========================================
# 7. ATTENDANCE ANALYSIS
# ==========================================

analyze_attendance(df)


# ==========================================
# 8. LIFESTYLE ANALYSIS
# ==========================================

analyze_lifestyle(df)


# ==========================================
# 9. STUDENT DATA VISUALIZATION
# ==========================================

show_visualizations(df)


# ==========================================
# 10. PROJECT COMPLETION MESSAGE
# ==========================================

print("\n========================================")
print(" PROJECT COMPLETED SUCCESSFULLY!")
print("========================================")