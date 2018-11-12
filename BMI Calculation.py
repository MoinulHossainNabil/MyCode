def bmi(name,weight,height):
    
    result=float(weight)/(float(height*0.3048)*float(height*0.3048))
    if(result<18.5):
        print(name,"BMI=",result,": Underweight")
    if(result>18.5 and result<25):
        print(name,"BMI=",result,": Ideal")
    if(result>25 and result<30):
        print(name,"BMI=",result,": Overweight")
    if(result>30):
        print(name,"BMI=",result,": Obese")
    
person1=['Arya',60,5.6]
person2=['Snasa',70,5.5]
person3=['Khalessi',60,6.0]
person4=['Mergery',75,5.6]
person5=['Cersy',70,5.7]
bmi(*person1)
bmi(*person2)
bmi(*person3)
bmi(*person4)
bmi(*person5)
