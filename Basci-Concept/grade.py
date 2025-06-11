mark = float(input("Enter a mark:"))
if mark >= 90:
    grade = "A"
elif mark >= 80:
    grade = "B"
elif mark  >= 70:
    grade = "C"
elif mark  >= 60:
    grade = "D"
else:
    grade = "Fail"
print("Grade:",grade)
    