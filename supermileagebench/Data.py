from __future__ import division
from supermileagebench.DynoMath import derivate,  secondOrder, find_first_derivative_five_point, find_second_derivative_five_point
from supermileagebench.dropbox_saver import  DropboxSaver
import math
import os
from datetime import datetime

class PointDatabase(object):
    '''
    Storage for points in time
    '''
    def __init__(self, maximumSize):
        self.totalTime = 0
        self.maximumArray = maximumSize
        
        self.accelerations = []
        self.time = []
        
        self.fileData = []
        self.fileTime = []
        
    def _add_time_point(self, timeAfterLastPoint):
        self.totalTime += (timeAfterLastPoint * 0.001)                
        self.time.append(self.totalTime)            
        self.fileTime.append(float(self.totalTime))
        
class PositionDatabase(PointDatabase):
    '''
    Storage for position points in time
    '''    
    def addPoint(self, position, timeAfterLastPoint):
        self._add_time_point(timeAfterLastPoint)
        
        self.accelerations.append(position)        
        if len(self.accelerations) > self.maximumArray:
            self.accelerations.pop(0)
            self.time.pop(0)            
        self.fileData.append(float(position))
        
class VelocityDatabase(PointDatabase):
    '''
    Storage for velocity points
    '''    
    def __init__(self, maximumSize, derivativeInterval):
        super(VelocityDatabase, self).__init__(maximumSize)
        self.derivativeInterval = derivativeInterval/1000
        self.positions = []
        
        
    def addPoint(self, position, timeAfterLastPoint):
  
        self._add_time_point(timeAfterLastPoint)        
        self.positions.append(position)     
        
#        velocity = self._findVelocity(position)  
        velocity = derivate(self.time, self.positions, self.derivativeInterval)
        self.accelerations.append(velocity)
                   
        if len(self.positions) > self.maximumArray:
            self.positions.pop(0)
            self.accelerations.pop(0)
            self.time.pop(0)
        

    def _findVelocity(self, position):
        positionBefore, time = self._findPositionBeforeInterval()
        time = time if time != 0 else self.derivativeInterval
        return (position - positionBefore) / time
    
    def _findPositionBeforeInterval(self):
        index, time= self._findIndexOfPointInTime()
        return self.positions[index], time
        
    def _findIndexOfPointInTime(self): 
        currentTime = self.totalTime
        #FIXME Not Efficient!
        for index, time in reversed(list(enumerate(self.time))):
            if(currentTime - time >= self.derivativeInterval):
                print index
                print len(self.time)-1
                print currentTime-time
                return index, currentTime - time
        return 0, 0
    
class AccelerationDatabase(PointDatabase):
    
    def __init__(self, maximumSize, derivativeInterval):
        
        self.totalTime = 0
        self.maximumArray = maximumSize
        
        self.positions = []
        self.velocities = []
        self.accelerations = []
        self.time = []
        
        self.file_positions = []
        self.file_velocities = []
        self.file_accelerations = []
        self.file_time = []
        
        self.derivativeInterval = derivativeInterval/1000

        self.numberOfPulsesPerTurn = 1440
        self.started = False
    

    
    def addPoint(self, position, timeAfterLastPoint):  
        if timeAfterLastPoint < 2147483647 and self.started == True: #To eliminate the first point
            self._add_time_point(timeAfterLastPoint)
            self._add_position_point(position)
            self._add_velocity_point()
            self._add_acceleration_point()
            
            if len(self.positions) > self.maximumArray:
                self.positions.pop(0)
                self.velocities.pop(0)
                self.accelerations.pop(0)
                self.time.pop(0)
          
    def _add_time_point(self, timeAfterLastPoint):
        self.totalTime += (timeAfterLastPoint * 0.001)                
        self.time.append(self.totalTime)            
        self.file_time.append(self.totalTime)
    
    def _add_position_point(self, position):
        position_in_radians = self._convert_pulses_to_radians(position)
        self.positions.append(position_in_radians)
        self.file_positions.append(position_in_radians)
    
    def _add_velocity_point(self):
        velocity = derivate(self.time, self.positions, self.derivativeInterval)
        self.velocities.append(velocity)
        self.file_velocities.append(velocity)
        
    def _add_acceleration_point(self):
        acceleration = derivate(self.time, self.velocities, self.derivativeInterval)
        self.accelerations.append(acceleration)
        self.file_accelerations.append(acceleration)
              
    def _convert_pulses_to_radians(self, position):
        return (position/self.numberOfPulsesPerTurn)*(2*math.pi)
    
    def startDataAquisition(self):
        self.started = True
    
    def stopDataAquisition(self, save):
        self.started = False
        if save:
            self._save_data_to_dropbox()
        self.deleteData()
        
    def _save_data_to_dropbox(self):
        filename = self._save_to_csv()
        saver = DropboxSaver()
        saver.save_data_to_dropbox(filename)       
        os.remove(filename)
    
    def deleteData(self):
        self.positions[:] = []
        self.velocities[:] = []
        self.accelerations[:] = []
        self.time[:] = []
        
        self.file_positions[:] = []
        self.file_velocities[:] = []
        self.file_accelerations[:] = []
        self.file_time[:] = []
    
    def _save_to_csv(self):
        filename = ("%s.csv" % str(datetime.now().replace(microsecond=0))) 
        with open(filename, 'w') as data_file:
            data_file.write("Time, Positions, Velocities, Accelerations \n")
            for i in range(len(self.time)):
                data_file.write(str(self.file_time[i]) + ",")
                data_file.write(str(self.file_positions[i]) + ",")
                data_file.write(str(self.file_velocities[i]) + ",")
                data_file.write(str(self.file_accelerations[i]) + "\n")
        return filename

    
        