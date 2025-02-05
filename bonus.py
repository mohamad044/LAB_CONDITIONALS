wieght = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(m ex:1.70): "))
bmi = round(wieght / height**2,2)
print(f"Your BMI is:{bmi} ")

if(bmi >= 25):
    print("You are overwieght you need to work out more and watch your diet.")
elif(bmi > 18.5):
    print("You are fit & healthy. ")
else:
    print("You are underweight. watch your health. ")
