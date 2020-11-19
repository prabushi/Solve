for a in range(-70, 70):
    for b in range(-70, 70):
        for c in range(-70, 70): #a
            for d in range(-70, 70): #b
                if (39*b*d + 16*a*c == 70 and 18*b*d + 37*a*c == 50):
                    print(a, ' a- ', b, ' b- ', c, ' c- ', d, ' d-')
                    if (a > 0 and b > 0 and c > 0 and d > 0):
                        print("================")

print("end")

#39*b*d + 16*a*c
#13*b*d + 42*a*c
#28*b*d + 27*a*c
#18*b*d + 37*a*c
