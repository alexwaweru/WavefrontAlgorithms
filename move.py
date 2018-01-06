#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from multiprocessing import Process
import time as t
import math

left_motor = ev3.LargeMotor('outC')
right_motor = ev3.LargeMotor('outB')


def drive_straight(distance):
    radius = 2.8#take measurement
    pi = math.pi
    circumference = 2*pi*radius
    angle = (distance*360)/circumference
    left_motor.run_to_rel_pos(position_sp=angle, speed_sp=200 )
    right_motor.run_to_rel_pos(position_sp=angle, speed_sp=200)
    right_motor.wait_while('running')
    left_motor.wait_while('running')


def turn_right(angle):
    #Left motor takes the turnLeft
    width = 12.3 #measure width of the robot
    circumference = 2*(math.pi)*width
    distance = (angle/360)*circumference
    wheel_radius = 2.8 #measure radius of wheel_radius
    turn_angle = (distance*360)/(2*(math.pi)*wheel_radius)
    left_motor.run_to_rel_pos(position_sp=turn_angle, speed_sp=200)
    left_motor.wait_while('running')
