name= input("Input your name : ")
salary= float(input("input your basic salary : "))
sale= float(input("input your total sales : "))

addtional_salary= sale*15/100
total_salary= salary+addtional_salary

print("TOTAL = $ %.2f"%total_salary)