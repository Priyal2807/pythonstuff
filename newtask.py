print ("Body Mass Index Calculator")

weight=float(input("Please Enter yor weight in kgs"))
height=float(input("Please Enter your height in metres"))
bmi=weight/(height**2)
print (bmi)
if bmi>11.00 and bmi<19.00:
    print ("You are underweight")
    print("Take proper diet")
elif bmi>19.00 and bmi<25.00:
    print("Congrats You are healthy;)")
elif bmi>25.00 and bmi<30.00:
    print("You are overweight")
    print("You gotta hit the gym")
elif bmi>30.00 and bmi<40.00:
    print("You are obese")
    print("Start thinking seriously and please hit the gym")
else:
    print("You are extremely obese")
    
