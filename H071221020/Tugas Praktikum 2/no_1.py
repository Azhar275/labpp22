score = float(input('Masukkan nila:'))

if score % 1 == 0:
    score = int(score)
else:
    score = '{0:.2f}'.format(score)
    score = float(score)

if score >100 or score <0:
    print ("Masukkan nilai hanya dalam rentang 0-100")
elif score >= 90:
    print (f"Nilai {score} = 'A'")
elif score >= 80:
    print (f"Nilai {score} = 'B'")
elif score >= 70:
    print (f"Nilai {score} = 'C'")
elif score >= 60:
    print (f"Nilai {score} = 'D'")
elif score >= 40:
    print (f"Nilai {score} = 'E'")
elif score < 40:
    print (f"Nilai {score} = 'F'")
else:
    print ("eror")