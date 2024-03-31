a=float(input("basic_salary:"))

if a<=10000:
    hra=(a*0.20)
    da=(a*0.80)
    gs_total=(a+hra+da)
    print("gross salary",gs_total)

elif a<=20000:
    hra=(a*0.25)
    da=(a*0.90)
    gs_total=(a+hra+da)
    print("gross salary",gs_total)

elif a>20000:
    hra=(a*0.30)
    da=(a*0.95)
    gs_total=(a+hra+da)
    print("gross salary",gs_total)




