import numpy as np
import matplotlib.pyplot as mp

# program for Linear Regression

# define the data lists and their lengths
xVals = np.array([1, 2, 3, 4, 5, 6])
yVals = np.array([10, 12, 15, 13, 21, 19])


m = xVals.size
n = yVals.size

def format_of_index_vs_value(ls):

    for i in range(n):
        print(i, " for ",ls[i])



print("X values are : ", xVals)
print("Y values are :", yVals)





#define a function to perform linear regression using numpy
def LinReg():
    global xVals, yVals
    global m, n

    sum_x = sum(xVals)
    sum_y = sum(yVals)
    sum_xy = sum(np.multiply(xVals, yVals))
    sum_xx = sum(np.square(xVals))
    sum_yy = sum(np.square(yVals))

    slope = (n*sum_xy-sum_x*sum_y)/(n*sum_xx-sum_x*sum_x)
    y_int = (sum_y*sum_xx-sum_x*sum_xy)/(n*sum_xx-sum_x*sum_x)
    r = (n*sum_xy-sum_x*sum_y)/((n*sum_xx-sum_x**2)*(n*sum_yy-sum_y**2))**0.5
    coef_detm = r**2


    #using numpy’s float printing routines to print the fixed decimal number; it is fast.

    print("\nThe predicted slope is: %0.2f" % slope)
    print("The predicted intercept is: %0.2f" % y_int)

    print("\nlinear model: y = %0.2fx + %0.f" % (slope, y_int))

    print("***********************************************************")

    #perform interpolation and extrapolation here



    #1) interpolation

    print("\nRange of known Xs is ", xVals)

    msg = "\nPlease provide an x-value for interpolation that in the range of x but not the given one >> "

    user_x_int = float(input(msg))
    user_y_int = slope*user_x_int+y_int

    print("\n\nInterpolation results : %0.2f" %user_y_int)
    print("***********************************************************")

    #2) extrapolation
    msg2 = "\nPlease provide an x-value for extrapolation that out of the range of x >> "
    user2_x_int = float(input(msg2))
    user2_y_int = slope*user2_x_int+y_int

    print("\n\nExtrapolation results : %0.2f" %user2_y_int)
    print("***********************************************************")

    print("\n\nThe coefficient of determination r^2 is %0.3f" % coef_detm)
    print("The correlation coefficient r is %0.3f" % r)
    print("\nThe Analysis based on the correlation coefficient is that \n"
          "if r is greater or equal to 0.80 and less than or equal to 1.00 >> it is a strong positive correlation\n"
          "if r is greater or equal to -1.00 and less than or equal to -0.80 >> it is a strong negative correlation\n"
          "if r is greater or equal to -0.80 and less than or equal to 0.80 >> it is a weak correlation\n\n")

    #because we know that r of original is in this range, thus we modidy the code here instead of the second condition
    if (r >= 0.80 and r <= 1.00):
        print("Analysis: strong positive correlation")
        print("\n***********************************************************")

        #while r is strong correlation changes a value of y to make it a weak correlation
        while True:
            format_of_index_vs_value(yVals)
            int_index = int(input(f"Type index as being displayed above accordingly to y value to weaken the correlation>>"))

            newVal = int(input(f"Choose the new value of y you want to modify besides {yVals[int_index]} >>"))
            #copy a value of y from original data
            yValues = yVals.copy()

            #update a value of y based on the user's input
            yValues[int_index] = newVal

            #thus, all data to calculate r will be updated as well

            sum_x = sum(xVals)
            sum_y = sum(yValues)
            sum_xy = sum(np.multiply(xVals, yValues))
            sum_xx = sum(np.square(xVals))
            sum_yy = sum(np.square(yValues))


            r = (n * sum_xy - sum_x * sum_y) / ((n * sum_xx - sum_x ** 2) * (n * sum_yy - sum_y ** 2)) ** 0.5

            #whenever r is in a weak correlation range>> leave the loop otherwise keep running the program

            if r>-0.80 and r < 0.80:
                print("\nYou have successfully changed the new value of y  from ", yVals[int_index],"to ", yVals[newVal], "so that it became the weak correlation.")
                break

    if (r <= -0.80 and r >= -1.00):
        print("Analysis: strong negative correlation")
        print("\n***********************************************************")
    if (r > -0.80 and r < 0.80):
        print("Analysis: weak correlation")
        print("\n***********************************************************")

    print("***********************************************************")

# call the Linear Regression function
LinReg()

#plot the graph

mp.plot(xVals, yVals, "go")
# g = green colored markers
# o = markers without smooth line

# axis titles
mp.xlabel("Month")
mp.ylabel("Number of days")

# horizontal scale: 0 to 10
# vertical scale: 0 to 20
mp.axis([0, 10, 0, 20])
mp.show()


