#!/usr/bin/env python
#coding:utf-8
 
from learning_communication.srv import *
import rospy

def handle_sum_two_ints(req):
	req.a = 0
	req.i = 100
	while req.i > 0:
		req.a = req.a + req.i
		req.i = req.i - 1
	print "sum: %s" % req.a
	return req.a

def sum_two_ints_server():
    rospy.init_node('sum_two_ints_server')  #创建名为add_two_ints_server的节点
    s = rospy.Service('sum_two_ints', SumTwoInts, handle_sum_two_ints) #定义服务节点名称，服务的类型，处理函数
    print "Ready to sum two ints."
    rospy.spin()

if __name__ == "__main__":
    sum_two_ints_server()
