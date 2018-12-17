#!/usr/bin/env python
#coding:utf-8
 
from learning_communication.srv import *
import rospy

def handle_sub_two_ints(req):
    print "Returning [%s * %s = %s]" % (req.i, req.j, (req.i * req.j))
    return (req.i * req.j) #AddTwoIntsResponse由服务生成的返回函数

def sub_two_ints_server():
    rospy.init_node('sub_two_ints_server')  #创建名为add_two_ints_server的节点
    s = rospy.Service('sub_two_ints', SubTwoInts, handle_sub_two_ints) #定义服务节点名称，服务的类型，处理函数
    print "Ready to sub two ints."
    rospy.spin()

if __name__ == "__main__":
    sub_two_ints_server()
