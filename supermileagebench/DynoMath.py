from __future__ import division
from scipy import *
from numpy import *

def derivate(time, data, epsilon):
    index = _findIndexOfPointInTime(time, epsilon)
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
        
