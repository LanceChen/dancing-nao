# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.0333333, 0.5, 1])
keys.append([[-0.17952, [3, -0.0111111, 0], [3, 0.155556, 0]], [-0.17952, [3, -0.155556, 0], [3, 0.166667, 0]], [-0.179519, [3, -0.166667, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.0333333, 0.5, 1])
keys.append([[0.0122299, [3, -0.0111111, 0], [3, 0.155556, 0]], [0.0122299, [3, -0.155556, 0], [3, 0.166667, 0]], [0.0122299, [3, -0.166667, 0], [3, 0, 0]]])

names.append("LAnklePitch")
times.append([0.0333333, 0.5, 1])
keys.append([[0.0889301, [3, -0.0111111, 0], [3, 0.155556, 0]], [0.475498, [3, -0.155556, 0], [3, 0.166667, 0]], [0.0889301, [3, -0.166667, 0], [3, 0, 0]]])

names.append("LAnkleRoll")
times.append([0.0333333, 0.5, 1])
keys.append([[-0.138018, [3, -0.0111111, 0], [3, 0.155556, 0]], [-0.049046, [3, -0.155556, 0], [3, 0.166667, 0]], [-0.138018, [3, -0.166667, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([0.0333333, 0.5, 1])
keys.append([[-0.454022, [3, -0.0111111, 0], [3, 0.155556, 0]], [-1.32533, [3, -0.155556, 0], [3, 0.166667, 0]], [-0.454021, [3, -0.166667, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([0.0333333, 0.5, 1])
keys.append([[-1.17355, [3, -0.0111111, 0], [3, 0.155556, 0]], [-0.880558, [3, -0.155556, 0], [3, 0.166667, 0]], [-1.17355, [3, -0.166667, 0], [3, 0, 0]]])

names.append("LHand")
times.append([0.0333333, 0.5, 1])
keys.append([[0.3028, [3, -0.0111111, 0], [3, 0.155556, 0]], [0.2664, [3, -0.155556, 0], [3, 0.166667, 0]], [0.3028, [3, -0.166667, 0], [3, 0, 0]]])

names.append("LHipPitch")
times.append([0.0333333, 0.5, 1])
keys.append([[0.131966, [3, -0.0111111, 0], [3, 0.155556, 0]], [-0.346642, [3, -0.155556, 0], [3, 0.166667, 0]], [0.131966, [3, -0.166667, 0], [3, 0, 0]]])

names.append("LHipRoll")
times.append([0.0333333, 0.5, 1])
keys.append([[0.136568, [3, -0.0111111, 0], [3, 0.155556, 0]], [0.046062, [3, -0.155556, 0], [3, 0.166667, 0]], [0.136568, [3, -0.166667, 0], [3, 0, 0]]])

names.append("LHipYawPitch")
times.append([0.0333333, 0.5, 1])
keys.append([[-0.177902, [3, -0.0111111, 0], [3, 0.155556, 0]], [-0.141086, [3, -0.155556, 0], [3, 0.166667, 0]], [-0.177901, [3, -0.166667, 0], [3, 0, 0]]])

names.append("LKneePitch")
times.append([0.0333333, 0.5, 1])
keys.append([[-0.092082, [3, -0.0111111, 0], [3, 0.155556, 0]], [-0.067538, [3, -0.155556, 0], [3, 0.166667, 0]], [-0.092082, [3, -0.166667, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.0333333, 0.5, 1])
keys.append([[1.43732, [3, -0.0111111, 0], [3, 0.155556, 0]], [1.32994, [3, -0.155556, 0], [3, 0.166667, 0]], [1.43732, [3, -0.166667, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0.0333333, 0.5, 1])
keys.append([[0.187106, [3, -0.0111111, 0], [3, 0.155556, 0]], [0.029104, [3, -0.155556, 0], [3, 0.166667, 0]], [0.187106, [3, -0.166667, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([0.0333333, 0.5, 1])
keys.append([[0.0413761, [3, -0.0111111, 0], [3, 0.155556, 0]], [-0.561486, [3, -0.155556, 0], [3, 0.166667, 0]], [0.0413762, [3, -0.166667, 0], [3, 0, 0]]])

names.append("RAnklePitch")
times.append([0.0333333, 0.5, 1])
keys.append([[0.0874801, [3, -0.0111111, 0], [3, 0.155556, 0]], [-0.377322, [3, -0.155556, 0], [3, 0.166667, 0]], [0.0874801, [3, -0.166667, 0], [3, 0, 0]]])

names.append("RAnkleRoll")
times.append([0.0333333, 0.5, 1])
keys.append([[0.128898, [3, -0.0111111, 0], [3, 0.155556, 0]], [0.115092, [3, -0.155556, 0], [3, 0.166667, 0]], [0.128898, [3, -0.166667, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([0.0333333, 0.5, 1])
keys.append([[0.38661, [3, -0.0111111, 0], [3, 0.155556, 0]], [0.092082, [3, -0.155556, 0], [3, 0.166667, 0]], [0.38661, [3, -0.166667, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0.0333333, 0.5, 1])
keys.append([[1.23636, [3, -0.0111111, 0], [3, 0.155556, 0]], [1.87757, [3, -0.155556, 0], [3, 0.166667, 0]], [1.23636, [3, -0.166667, 0], [3, 0, 0]]])

names.append("RHand")
times.append([0.0333333, 0.5, 1])
keys.append([[0.3092, [3, -0.0111111, 0], [3, 0.155556, 0]], [0.324, [3, -0.155556, 0], [3, 0.166667, 0]], [0.3092, [3, -0.166667, 0], [3, 0, 0]]])

names.append("RHipPitch")
times.append([0.0333333, 0.5, 1])
keys.append([[0.141086, [3, -0.0111111, 0], [3, 0.155556, 0]], [0.48398, [3, -0.155556, 0], [3, 0.166667, 0]], [0.141086, [3, -0.166667, 0], [3, 0, 0]]])

names.append("RHipRoll")
times.append([0.0333333, 0.5, 1])
keys.append([[-0.125746, [3, -0.0111111, 0], [3, 0.155556, 0]], [-0.0904641, [3, -0.155556, 0], [3, 0.166667, 0]], [-0.125746, [3, -0.166667, 0], [3, 0, 0]]])

names.append("RHipYawPitch")
times.append([0.0333333, 0.5, 1])
keys.append([[-0.177902, [3, -0.0111111, 0], [3, 0.155556, 0]], [-0.141086, [3, -0.155556, 0], [3, 0.166667, 0]], [-0.177901, [3, -0.166667, 0], [3, 0, 0]]])

names.append("RKneePitch")
times.append([0.0333333, 0.5, 1])
keys.append([[-0.0858622, [3, -0.0111111, 0], [3, 0.155556, 0]], [-0.0858622, [3, -0.155556, 0], [3, 0.166667, 0]], [-0.0858622, [3, -0.166667, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.0333333, 0.5, 1])
keys.append([[1.43433, [3, -0.0111111, 0], [3, 0.155556, 0]], [1.87919, [3, -0.155556, 0], [3, 0.166667, 0]], [1.43433, [3, -0.166667, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0.0333333, 0.5, 1])
keys.append([[-0.177986, [3, -0.0111111, 0], [3, 0.155556, 0]], [-0.220938, [3, -0.155556, 0], [3, 0.166667, 0]], [-0.177985, [3, -0.166667, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([0.0333333, 0.5, 1])
keys.append([[0.179436, [3, -0.0111111, 0], [3, 0.155556, 0]], [0.383458, [3, -0.155556, 0], [3, 0.166667, 0]], [0.179436, [3, -0.166667, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err
