
import numpy as np

def twoPtForwardDiff(x,y):
    """
    Returns the derivative of y with respect to x using the forward 
    differentiation method
    """
    dydx = np.zeros(y.shape,float) 
    dydx[0:-1] = np.diff(y)/np.diff(x)
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx
    
def twoPtCenteredDiff(x,y):
    """
    Returns the derivative of y with respect to x using the center 
    differentiation method
    """
    dydx = np.zeros(y.shape,float)
    dydx[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2])
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx
   
def fourPtCenteredDiff(x,y):
    """
    Returns the derivative of y with respect to x using the center 
    differentiation method
    """
    dydx = np.zeros(y.shape,float)
    dydx[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx[1] = (y[2]-y[1])/(x[2]-x[1])
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    dydx[-2] = (y[-2] - y[-3])/(x[-2] - x[-3])
    h = 0.1
    for i in range(2,np.size(y)-2):
        dydx[i] = ((y[i-2] - 8*y[i-1]) + 8*y[i+1] - y[i+2])/(12*h)

    return dydx    