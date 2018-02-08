
import matplotlib.pyplot as plt
import random

#=================================================================================================================
def predict(x,theta0,theta1):
    return (theta0 + (theta1 * x)) 

#---------------------------------------


def findGradient(area,price,theta0,theta1,check):
    
    grad = 0
    x = 0
    for i in range(len(area)):
        
        H0 = predict(area[i],theta0,theta1)
        
        if check:
            x = 1
        else:
            x = area[i]
            
        grad = grad + (H0 - price[i]) * x
    
    grad = grad / len(area)
    return grad    


#----------------------------------------


def MSE(prediction,actualPrice,theta0,theta1):
    
    sum = 0
    squaredDifference = 0
    for i in range(len(prediction)):
        squaredDifference = (prediction[i] - actualPrice[i])
        squaredDifference = squaredDifference * squaredDifference
        sum = sum + squaredDifference
    
    
    return (sum / len(prediction))
    
    
#----------------------------------------


def AdjstTheta(area,price,theta0,theta1,alpha,check):
    
    #if check is True then adjust theta0
    theta = 0
    newTheta = 0
    
    
    if check:
        theta = theta0
        newTheta = theta0
        print("Adjusting theta 0")
    else:
        
        theta = theta1
        newTheta = theta1
        print("Adjusting theta 1")
        
    thetaValues = [theta]
    
    gradient = 100
 
    while gradient > 0.01:
    
        theta=newTheta
        
        if check:
            theta0 = theta
        
        else:
            theta1 = theta
            
        
        gradient = findGradient(area,price,theta0,theta1,check)
        print("gradient at theta: " + str(theta) + " is :" + str(gradient))
        newTheta = theta - (alpha * gradient)    
        thetaValues.append(newTheta)
        
    return thetaValues


#===================================================================================================================


price=[48349,50184,51026,51127,50606,53493,52757,53492,54720,53951,59752,59510,59504,65842,70928,75657,81226,87082,93334,98448,108255,115790,121378,120859,122827,125374,124488,118357,123483,126609,125495,128510,129378,134523,134534,133202,132349,129700,123019,118525,112986,112348,116051,116154,115545,119057,117234,116836,113863,117691,116610,115716,114828,114882,116624,114264,112989,115763,116909,116417,119702,125106,121990,121486,125299,125189,124345,124167,123864,123914,124074,124284,123397,125237,127213,124535,54523,56103,56824,57863,57669,60754,58942,61037,62725,64894,65754,67591,70166,76498,82357,91480,90877,100625,106016,110961,116673,129018,133494,133494,134728,139688,139585,140549,142424,146209,148585,150785,151530,155159,156429,154695,151764,146074,140634,133632,127412,131675,134584,137275,136208,141093,136906,132302,134967,138228,137340,134467,132128,134362,134633,131046,131470,133283,137634,140684,139775,142661,145265,142816,141647,147387,145673,143390,144361,148587,150823,149124,147983,151947,151482,151747]
area = [105.8,109.8,111.7,111.9,110.8,117.1,115.5,117.1,119.8,118.1,130.8,130.3,130.2,144.1,155.3,165.6,177.8,190.6,204.3,215.5,237.0,253.4,265.7,264.5,268.8,274.4,272.5,259.1,270.3,277.1,274.7,281.3,283.2,294.4,294.5,291.6,289.7,283.9,269.3,259.4,247.3,245.9,254.0,254.2,252.9,260.6,256.6,255.7,249.2,257.6,255.2,253.3,251.3,251.5,255.3,250.1,247.3,253.4,255.9,254.8,262.0,273.8,267.0,265.9,274.1,274.0,272.2,271.8,271.1,271.2,271.6,272.0,270.1,274.1,278.4,272.6,111.1,114.3,115.7,117.9,117.5,123.7,120.1,124.3,127.8,132.2,133.9,137.7,142.9,155.8,167.7,186.3,185.1,205.0,215.9,226.0,237.6,262.8,271.9,271.9,274.4,284.5,284.3,286.3,290.1,297.8,302.6,307.1,308.6,316.0,318.6,315.1,309.1,297.5,286.5,272.2,259.5,268.2,274.1,279.6,277.4,287.4,278.9,269.5,274.9,281.5,279.7,273.9,269.1,273.7,274.2,266.9,267.8,271.5,280.3,286.6,284.7,290.6,295.9,290.9,288.5,300.2,296.7,292.1,294.1,302.7,307.2,303.7,301.4,309.5,308.5,309.1]


theta0 = random.randrange(0,5,1)
theta1 = random.randrange(500,600,1)


print("theta 1 : " + str(theta1) + " Theta 0 : " + str(theta0))
print("Enter some value for alpha: '('make sure its around 0.0000something')'")
alpha = float(input())

check = True

#Adjusting theta1 value unless gradient/slope is not less then 0.01

theta0Values = AdjstTheta(area,price,theta0,theta1,alpha,check)
theta0 = theta0Values[len(theta0Values)-1]


check = False
theta1Values = AdjstTheta(area,price,theta0,theta1,alpha,check)
theta1 = theta1Values[len(theta1Values)-1]

#Adjusted value of theta1    
print("Values for fitting parameters Theta0: " + str(theta0) + "   Theta1: " + str(theta1))    

plt.subplot(2, 1, 1)
plt.plot(theta0Values,'o-')
plt.legend(loc = 'best')
plt.title('Visualization of changing theta0 values')
plt.ylabel('theta0')


plt.subplot(2, 1, 2)
plt.plot(theta1Values,'o-')
plt.legend(loc = 'best')
plt.title('Visualization of changing theta1 values')
plt.ylabel('theta1')

#predicting values based on our hypothesis and calculated theta values

prediction = []
for x in area:
    prediction.append(predict(x,theta0,theta1))
    

#calculating Mean Squared Error

print("Mean Squared Error: " + str(MSE(prediction,price,theta0,theta1)))


