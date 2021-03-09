height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = float(weight) / (float(height) ** 2)
bmi_an_int = float(bmi)
print(bmi_an_int)

if bmi_an_int < 18.5:
    print(str(bmi_an_int) + " is underweight")
elif bmi_an_int > 18.5 and bmi_an_int < 25:
    print(str(bmi_an_int) + " is normal weight")
elif bmi_an_int > 25 and bmi_an_int < 30:
    print(str(bmi_an_int) + " slight overweight")
elif bmi_an_int > 30 and bmi_an_int < 35:
    print(str(bmi_an_int) + " obese")
else:
    print(str(bmi_an_int) + " clnically obese")



