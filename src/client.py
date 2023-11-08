#!/usr/bin/env python

import rospy
from minimum.srv import minim, minimRequest
import random 

def clt():
	rospy.init_node("client")
	rate = rospy.Rate(10)
	minim_srv = rospy.ServiceProxy('minim',minim)
	while not rospy.is_shutdown():
		req = minimRequest()		
		req.t1=[random.randint(0, 100) for _ in range(5)]
		print("request", req.t1)
		resp= minim_srv(req.t1)
		print("response", resp)		
		rate.sleep()
		
if __name__ == "__main__":
	clt()
