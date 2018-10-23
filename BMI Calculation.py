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
    
nabil=['Nabil',60,5.6]
keya=['Keya',70,5.5]
zahid=['Zahid',60,6.0]
zawad=['Zawad',75,5.6]
mahin=['Mahin',70,5.7]
bmi(*nabil)
bmi(*keya)
bmi(*zahid)
bmi(*zawad)
bmi(*mahin)
