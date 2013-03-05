def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''

    exposure = 0.0
    while start < stop:
        exposure += step * f(start)
        start += step      
    return exposure 





def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

print(radiationExposure(0, 5, 1))
print('correct output: 39.10318784326239')
