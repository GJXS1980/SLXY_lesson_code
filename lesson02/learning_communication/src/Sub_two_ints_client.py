#!/usr/bin/env python
#coding:utf-8
 
import sys
import rospy
from learning_communication.srv import *

def sub_two_ints_client(x, y):
    rospy.wait_for_service('sub_two_ints')  #等待接入服务节点
    try:
        sub_two_ints = rospy.ServiceProxy('sub_two_ints', SubTwoInts) #创建服务的处理句柄,add_two_ints为服务名,AddTwoInts是服务类型
        resp1 = sub_two_ints(x, y)
        return resp1.re
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def usage():
    return "%s [x y]" % sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s * %s" % (x, y)
    print "%s * %s = %s" % (x, y, sub_two_ints_client(x, y))
