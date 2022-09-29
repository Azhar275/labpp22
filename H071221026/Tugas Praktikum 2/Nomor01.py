print("===MENENTUKAN GRADE NILAI===")
student_score= float(input("Insert your score : "))

if student_score>=90 and student_score<=100:
    print(f"Nilai {int(student_score)} = 'A' ")
elif student_score>=80 and student_score<90 :
    print(f"Nilai {int(student_score)} = 'B' ")
elif student_score>=70 and student_score<80 :
    print(f"Nilai {int(student_score)} = 'C' ")
elif student_score>=60 and student_score<70 :
    print(f"Nilai {int(student_score)} = 'D' ") 
elif student_score>=40 and student_score<60 :
    print(f"Nilai {int(student_score)} = 'E' ")
elif student_score<40 :
    print(f"Nilai {int(student_score)} = 'F' ")
else :
    print("niali melewati batasan")