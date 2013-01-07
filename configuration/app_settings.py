#coding: utf-8
from gui.data_plotting.rpm_wise_plots import TorqueRpmWiseComparablePlot, PowerRpmWiseComparablePlot
from gui.data_plotting.timewise_plots import PositionRadiansTimewisePlot, SpeedRadiansTimewisePlot, AccelerationTimewisePlot, TorqueTimewisePlot, PositionMetersTimewisePlot, SpeedMetersTimewisePlot, PositionRadiansComparableRpmWisePlot

_position_rad_time = u"Position (rad) -> temps"
_position_meters_time = u"Position (m) -> temps"
_speed_rad_time = u"Vitesse (rad/s) -> temps"
_speed_meters_time = u"Vitesse (km/h) -> temps"
_acceleration_rad_time = u"Accélération (rad/s\xb2) -> temps"
_torque_rad_time = u"Torque (Nm) -> temps"

_torque_rad_rpm = u"Torque (Nm) -> RPM"
_power_rad_rpm = u"Puissance (watt) -> RPM"
_position_rad_time_comparable = u"Position (rad) -> temps"

real_time_plot_types = [_position_rad_time, _position_meters_time, _speed_rad_time, _speed_meters_time,
                        _acceleration_rad_time, _torque_rad_time]
real_time_plots_class_dict = {_position_rad_time: PositionRadiansTimewisePlot,
                              _position_meters_time: PositionMetersTimewisePlot,
                              _speed_rad_time: SpeedRadiansTimewisePlot,
                              _speed_meters_time: SpeedMetersTimewisePlot,
                              _acceleration_rad_time: AccelerationTimewisePlot,
                              _torque_rad_time: TorqueTimewisePlot}

post_processing_plot_types = [_torque_rad_rpm, _power_rad_rpm, _position_rad_time_comparable]
post_processing_plots_class_dict = {_torque_rad_rpm: TorqueRpmWiseComparablePlot,
                                    _power_rad_rpm: PowerRpmWiseComparablePlot,
                                    _position_rad_time_comparable: PositionRadiansComparableRpmWisePlot}