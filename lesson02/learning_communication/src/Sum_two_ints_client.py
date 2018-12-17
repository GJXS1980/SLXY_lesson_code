#!/usr/bin/env python
#coding:utf-8
 
import sys
import rospy
from learning_communication.srv import *

def sum_two_ints_client():
    rospy.wait_for_service('sum_two_ints')  #等待接入服务节点
    try:
        sum_two_ints = rospy.ServiceProxy('sum_two_ints', SumTwoInts) #创建服务的处理句柄,add_two_ints为服务名,AddTwoInts是服务类型
        resp1 = sum_two_ints()
        return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

if __name__ == "__main__":
    print "Requesting " 
    print "sum = %s" % (sum_two_ints_client())
