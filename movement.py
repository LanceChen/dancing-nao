#!/usr/bin/env python

import rospy
from nao_dance.srv import *
from naoqi import ALProxy
from motion import left, right, leftFootBack, leftFootForward, rightFootBack, rightFootForward


class MoveMaker:
    def __init__(self):
        rospy.init_node("movement", anonymous=True)
        self.move_service = rospy.Service("make_move", MakeMove, self.handle_make_move)
        self.nextForward = "right"
        self.nextBackward = "right"
        self.motion = ALProxy("ALMotion", rospy.get_param('nao_ip'), 9559)
        rospy.loginfo("Movement node started")

    def handle_make_move(self, request):
        """
        :type request MakeMoveRequest
        """
        direction = request.direction
        move = ''
        if direction == "forward":
            if self.nextForward == "right":
                move = "rightFootForward"
                self.execute_move(rightFootForward.names, rightFootForward.times, rightFootForward.keys)
                self.nextForward = "left"
            else:
                move = "leftFootForward"
                self.execute_move(leftFootForward.names, leftFootForward.times, leftFootForward.keys)
                self.nextForward = "right"
        elif direction == "backward":
            if self.nextBackward == "right":
                move = "rightFootBack"
                self.execute_move(rightFootBack.names, rightFootBack.times, rightFootBack.keys)
                self.nextBackward = "left"
            else:
                move = "leftFootBack"
                self.execute_move(leftFootBack.names, leftFootBack.times, leftFootBack.keys)
                self.nextBackward = "right"
        elif direction == "right":
            move = "right"
            self.execute_move(right.names, right.times, right.keys)
        elif direction == "left":
            move = "left"
            self.execute_move(left.names, left.times, left.keys)
        rospy.loginfo("Move published %s" % move)
        return MakeMoveResponse()

    def execute_move(self, names, times, keys):
        try:
            self.motion.angleInterpolationBezier(names, times, keys)
        except BaseException, err:
            print err


def main():
    MoveMaker()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down"

if __name__ == '__main__':
    main()
