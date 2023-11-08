#!/usr/bin/env python

import rospy
from minimum.srv import minim, minimResponse

def callback(request):
    minimum_table = min(request.t1)
    return minimResponse(minimum_table)
def minimum():
    rospy.init_node("server")
    s = rospy.Service('minim', minim, callback)
    rospy.loginfo("le tableau est pret")
    rospy.spin()

if __name__ == "__main__":
     minimum()
        
        
