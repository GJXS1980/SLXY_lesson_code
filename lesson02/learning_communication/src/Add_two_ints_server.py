#!/usr/bin/env python
#coding:utf-8
 
from learning_communication.srv import *
import rospy

def handle_add_two_ints(req):
    print "Returning [%s + %s = %s]" % (req.a, req.b, (req.a + req.b))
    return AddTwoIntsResponse(req.a + req.b) #AddTwoIntsResponse由服务生成的返回函数

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')  #创建名为add_two_ints_server的节点
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints) #定义服务节点名称，服务的类型，处理函数
    print "Ready to add two ints."
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
