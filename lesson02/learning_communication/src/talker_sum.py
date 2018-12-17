#!/usr/bin/env python
#coding:utf-8
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)   #发布话题名为chatter,包括数据类型和长度
    rospy.init_node('talker', anonymous=True)   #向ROS Master注册节点talker(anonymous=True)
    rate = rospy.Rate(0.5) # 发布频率为10hz
    while not rospy.is_shutdown():
        
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass