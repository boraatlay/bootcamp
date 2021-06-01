#########################

# Simple Linear Model Algorithm for Spiced Academy Assessment
# Author: Naim Bora Atlay
# 29.04.2021

#########################

import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

xydata = pd.read_csv('./datapoints.csv')               ### TASK 1

x = xydata.x
y = xydata.y

plt.scatter(x, y)                                      ### TASK 2
plt.savefig("xy_scatter.png")

def CalcResSq(a, b, x, y):
    
    lm_y      = [1.] * len(x)   ### Predicted y values
    res       = [1.] * len(x)   ### List of esiduals
    res_quad  = [1.] * len(x)   ### List of quadratic residuals
    
    for i in range(len(x)):
        lm_y[i] = a * x[i] + b
        res[i] = (lm_y[i] - y[i])
        res_quad[i] = (lm_y[i] - y[i])**2
    
    return res_quad


print ("Moin! This is a super simple linear model program with some default values of parameters. \n")
print ("However you are free to vary the parameters of the model. Let's start. \n")

ParameterVariation = True
ParameterSelection = True

while ParameterVariation:
    var = input("Do you want to vary any of the parameters? Insert 'yes' or 'no'.")
    if var.lower() == "yes" or var.lower() == "no":
        ParameterVariation = False
    else:
        ParameterVariation = True
        print("Please enter a valid option: yes or no")  

b_var = False
par_a = False
par_b = False

if var.lower() == "yes":
    b_var = True
    
    while ParameterSelection:
        par = input("Which parameter do you want to vary? Insert 'a' or 'b'.")
        if par.lower() == "a" or par.lower() == "b":
            ParameterSelection = False
        else:
            ParameterSelection = True
            print("Please enter a valid option: 'a' or 'b' ")

    if par.lower() == "a":
        print("The slope has chosen to be varied.")
        par_a = True
    if par.lower() == "b":
        print("The offset has chosen to be varied.")
        par_b = True
else:
    b_var = False

a = 10.0                    ### Initial value for the slope            ### TASK 3
b = 0.                      ### Initial value for the offset

var_size  = 0.1             ### Size of the step to vary a and b

tmp_mse, tmp_a, tmp_b = 0.,0.,0.       ### Temporary minimums of MSE, a and b
min_mse, min_a, min_b = 999.,999.,999.    ### Final minimums of MSE, a and b

if b_var == False:
    
    res_quad = CalcResSq(a, b, x, y)

    tmp_mse = sum(res_quad) / len(x)                                   ### TASK 4
    
    if tmp_mse < min_mse:
        min_mse = tmp_mse
        
else:
    
    if par_a == True:
        
        for a in np.arange(10, 0, var_size*(-1)):                       ### TASK 5

            res_quad = CalcResSq(a, b, x, y)
            
            tmp_a = a
            tmp_mse = sum(res_quad) / len(x)
            
            if tmp_mse < min_mse:
                
                min_mse = tmp_mse
                min_a = tmp_a      
                
    if par_b == True:

        for b in np.arange(0, 10, var_size):                             ### TASK 6
     
            res_quad = CalcResSq(a, b, x, y)
            
            tmp_b = b
            tmp_mse = sum(res_quad) / len(x)
            
            if tmp_mse < min_mse:
                
                min_mse = tmp_mse
                min_b = tmp_b
                
if b_var == False:
    print(f"The minimum MSE reached is: {round(min_mse,2)}")
    print("Try varying parameters to see if you can reach a lower MSE.")
if par_a == True:
    print(f"The minimum MSE reached by varying slope is: {round(min_mse,2)} with the slope value of {round(min_a,2)}")
if par_b == True:
    print(f"The minimum MSE reached by varying offset is: {round(min_mse,2)} with the offset value of {round(min_b,2)}")


################## HOW COULD THE ALGORITH BE IMPROVED? ##################                ### TASK 7

### A couple of things can be considered to improve the algorithm:
### - varying a and b simulteanously
### - calculating the root mean square error rather than mean square error
### - last but not least, in the calculation of MSE the denominator can be
###   changed by (n-1)

#########################################################################
