import os
def display_menu():
    os.system("cls")
    print("================================")
    print("       Attendance manager       ")
    print("================================")
    print(
"""1. Mark Today's Attendance
2. Add Today's Attendance
3. View Attendance by Subject
4. View Overall Attendance Percentage
5. View Present/Absent Count
6. Display Complete Attendance Record
7. Save Attendance to CSV
8. Load Previous Attendance
9. Delete Today's Record
10. Exit"""
        )
    print("================================")
    print("Choice : ",end='')

def viewBySubject():
    print("""================================
   View Attendance by Subject
================================\n
1. Math
2. DSA
3. OOPS
4. D.E.

Select Subject : _""")
    
if __name__ == "__main__":
    viewBySubject()
