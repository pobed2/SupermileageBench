from __future__ import division
from scipy import *
from numpy import *


def find_first_derivative_five_point(data, deltaX):
    return (data[0] - 8*data[1] + 8*data[3] - data[4])/(12*deltaX)

def find_second_derivative_five_point(data, deltaX):
    return (-data[0] + 16*data[1] - 30*data[2] + 16*data[3] - data[4])/(12*deltaX*deltaX)

def secondOrder(time, data, epsilon):
    index = _findIndexOfPointInTime(time, epsilon)
    timeDelta = _findTimeDifference(time, index, epsilon)
#    print data[-1] - data[index]
#    print epsilon*epsilon
    now = (len(time) + index)//2
    return (data[-1] - 2*data[now] + data[index])/(timeDelta*timeDelta)
      
      
def derivate(time, data, epsilon):
    index = _findIndexOfPointInTime(time, epsilon)
#    t = array(time[index:])
#    d = array(data[index:])
#    slope, b_s,r,tt,stderr = stats.linregress(t,d)
#    return slope
    timeDelta = _findTimeDifference(time, index, epsilon)
    dataDelta = _findDataDifference(data, index)  
    time = time if time != 0 else epsilon
    return dataDelta / timeDelta
 
def _findIndexOfPointInTime(time, epsilon): 
    currentTime = time[-1]
    index = len(time)-1
    
    for timeBefore in reversed(time):
        if(currentTime - timeBefore >= epsilon):
            return index
        index-=1
    return 0
   
def _findTimeDifference(time, index, epsilon):
    timeDelta = time[-1] - time[index]
    return timeDelta if timeDelta != 0 else epsilon

def _findDataDifference(data, index):
    return data[-1] - data[index]
        
