#include "ros/ros.h"

int main(int argc, char *argv[])
{
    // 解决乱码方案1
    setlocale(LC_ALL, "");
    // 方案2
    // setlocale(LC_CTYPE, "zh_CN.utf8");
    ros::init(argc, argv, "hello_c");
    ROS_INFO("hello world!哈哈哈");

    return 0;
}
