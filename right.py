# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.0416667, 0.625])
keys.append([[-0.150374, [3, -0.0138889, 0], [3, 0.194444, 0]], [-0.360533, [3, -0.194444, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.0416667, 0.625])
keys.append([[0.032172, [3, -0.0138889, 0], [3, 0.194444, 0]], [0.021434, [3, -0.194444, 0], [3, 0, 0]]])

names.append("LAnklePitch")
times.append([0.0416667, 0.625])
keys.append([[0.091998, [3, -0.0138889, 0], [3, 0.194444, 0]], [-0.535408, [3, -0.194444, 0], [3, 0, 0]]])

names.append("LAnkleRoll")
times.append([0.0416667, 0.625])
keys.append([[-0.130348, [3, -0.0138889, 0], [3, 0.194444, 0]], [-0.200912, [3, -0.194444, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([0.0416667, 0.625])
keys.append([[-0.424876, [3, -0.0138889, 0], [3, 0.194444, 0]], [-1.2471, [3, -0.194444, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([0.0416667, 0.625])
keys.append([[-1.17048, [3, -0.0138889, 0], [3, 0.194444, 0]], [-0.951122, [3, -0.194444, 0], [3, 0, 0]]])

names.append("LHand")
times.append([0.0416667, 0.625])
keys.append([[0.2848, [3, -0.0138889, 0], [3, 0.194444, 0]], [0.3344, [3, -0.194444, 0], [3, 0, 0]]])

names.append("LHipPitch")
times.append([0.0416667, 0.625])
keys.append([[0.130432, [3, -0.0138889, 0], [3, 0.194444, 0]], [-0.455555, [3, -0.194444, 0], [3, 0, 0]]])

names.append("LHipRoll")
times.append([0.0416667, 0.625])
keys.append([[0.0982179, [3, -0.0138889, 0], [3, 0.194444, 0]], [0.276162, [3, -0.194444, 0], [3, 0, 0]]])

names.append("LHipYawPitch")
times.append([0.0416667, 0.625])
keys.append([[-0.1733, [3, -0.0138889, 0], [3, 0.194444, 0]], [-0.1733, [3, -0.194444, 0], [3, 0, 0]]])

names.append("LKneePitch")
times.append([0.0416667, 0.625])
keys.append([[-0.090548, [3, -0.0138889, 0], [3, 0.194444, 0]], [1.05382, [3, -0.194444, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.0416667, 0.625])
keys.append([[1.4818, [3, -0.0138889, 0], [3, 0.194444, 0]], [1.20875, [3, -0.194444, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0.0416667, 0.625])
keys.append([[0.161028, [3, -0.0138889, 0], [3, 0.194444, 0]], [-0.131966, [3, -0.194444, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([0.0416667, 0.625])
keys.append([[0.115008, [3, -0.0138889, 0], [3, 0.194444, 0]], [-0.851412, [3, -0.194444, 0], [3, 0, 0]]])

names.append("RAnklePitch")
times.append([0.0416667, 0.625])
keys.append([[0.090548, [3, -0.0138889, 0], [3, 0.194444, 0]], [0.34826, [3, -0.194444, 0], [3, 0, 0]]])

names.append("RAnkleRoll")
times.append([0.0416667, 0.625])
keys.append([[0.128898, [3, -0.0138889, 0], [3, 0.194444, 0]], [0.363599, [3, -0.194444, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([0.0416667, 0.625])
keys.append([[0.414222, [3, -0.0138889, 0], [3, 0.194444, 0]], [0.142704, [3, -0.194444, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0.0416667, 0.625])
keys.append([[1.17193, [3, -0.0138889, 0], [3, 0.194444, 0]], [1.68122, [3, -0.194444, 0], [3, 0, 0]]])

names.append("RHand")
times.append([0.0416667, 0.625])
keys.append([[0.2852, [3, -0.0138889, 0], [3, 0.194444, 0]], [0.3836, [3, -0.194444, 0], [3, 0, 0]]])

names.append("RHipPitch")
times.append([0.0416667, 0.625])
keys.append([[0.128814, [3, -0.0138889, 0], [3, 0.194444, 0]], [-0.300706, [3, -0.194444, 0], [3, 0, 0]]])

names.append("RHipRoll")
times.append([0.0416667, 0.625])
keys.append([[-0.0981341, [3, -0.0138889, 0], [3, 0.194444, 0]], [-0.328234, [3, -0.194444, 0], [3, 0, 0]]])

names.append("RHipYawPitch")
times.append([0.0416667, 0.625])
keys.append([[-0.1733, [3, -0.0138889, 0], [3, 0.194444, 0]], [-0.1733, [3, -0.194444, 0], [3, 0, 0]]])

names.append("RKneePitch")
times.append([0.0416667, 0.625])
keys.append([[-0.0923279, [3, -0.0138889, 0], [3, 0.194444, 0]], [0.0261199, [3, -0.194444, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.0416667, 0.625])
keys.append([[1.46041, [3, -0.0138889, 0], [3, 0.194444, 0]], [0.889762, [3, -0.194444, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0.0416667, 0.625])
keys.append([[-0.15651, [3, -0.0138889, 0], [3, 0.194444, 0]], [-0.77778, [3, -0.194444, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([0.0416667, 0.625])
keys.append([[0.061318, [3, -0.0138889, 0], [3, 0.194444, 0]], [0.835988, [3, -0.194444, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err
