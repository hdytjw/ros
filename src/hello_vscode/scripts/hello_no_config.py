#! /usr/bin/env python
#coding=utf8

import rospy

# 当不配置 CMakeLists.txt 执行 python 文件将抛出如下异常
# /usr/bin/env: "python": 没有那个文件或目录
# 原因是当前 noetic 使用的是 python3
# 解决：1～可以直接声明 python3 （不建议）
#      2～软链接将 python 链接到 python3
# 注：当前版本 ROS 依赖于 python2，应该链接到 python2

if __name__ == "__main__":
    rospy.init_node("hello_p")
    rospy.loginfo("hello vscode! 来自python 22222")