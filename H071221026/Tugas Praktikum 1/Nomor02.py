second_total= int(input("Insert Second : "))

hour= second_total//3600
remaining_second= second_total%3600
minutes= remaining_second//60
seconds= remaining_second%60

print("%02d:%02d:%02d"%(hour,minutes,seconds))


