from __future__ import division
from supermileagebench.DynoMath import derivate
from supermileagebench.filters import savitzky_golay
from supermileagebench.dropbox_saver import  DropboxSaver
import math
import os
from datetime import datetime
import numpy

class AccelerationDatabase(object):

    def __init__(self, maximumSize, derivativeInterval):

        self.DISC_INERTIA = 60

        self.totalTime = 0
        self.maximumArray = maximumSize
        
        self.positions = []
        self.velocities = []
        self.accelerations = []
        self.torque = []
        self.time = []
        
        self.file_positions = []
        self.file_velocities = []
        self.file_accelerations = []
        self.file_torque = []
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
            self._add_torque_point()
            
            if len(self.positions) > self.maximumArray:
                self.positions.pop(0)
                self.velocities.pop(0)
                self.accelerations.pop(0)
                self.torque.pop(0)
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

    def _add_torque_point(self):
        self.torque = savitzky_golay(numpy.array(self.accelerations), 111, 1, deriv=0)
        self.torque *= self.DISC_INERTIA

        self.file_torque = savitzky_golay(numpy.array(self.file_accelerations), 111, 1, deriv=0)
        self.file_torque *= self.DISC_INERTIA

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
            data_file.write("Time, Positions, Velocities, Accelerations, Torques \n")
            for i in range(len(self.time)):
                data_file.write(str(self.file_time[i]) + ",")
                data_file.write(str(self.file_positions[i]) + ",")
                data_file.write(str(self.file_velocities[i]) + ",")
                data_file.write(str(self.file_accelerations[i]) + ",")
                data_file.write(str(self.file_torque[i]) + "\n")
        return filename

    
        