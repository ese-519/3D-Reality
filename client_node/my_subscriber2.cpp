#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>
#include <python2.7/Python.h>
void imageCallback(const sensor_msgs::ImageConstPtr& msg)
{
  try
  {
    cv::imshow("view", cv_bridge::toCvShare(msg, "bgr8")->image);
    cv::waitKey(30);
    static int image_count = 1;                                // added this
    if (image_count == 35)
    {
      image_count = 1;
    }
    std::stringstream sstream;                               // added this
    sstream << "my_image" << image_count << ".bmp" ;                  // added this
    ROS_ASSERT( cv::imwrite( sstream.str(),  cv_bridge::toCvShare(msg, "bgr8")->image ) );      // added this
    image_count++;
  }
  catch (cv_bridge::Exception& e)
  {
    ROS_ERROR("Could not convert from '%s' to 'bgr8'.", msg->encoding.c_str());
  }
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "image_listener3");
  ros::NodeHandle nh;
  cv::namedWindow("view");
  cv::startWindowThread();
  image_transport::ImageTransport it(nh);
  image_transport::Subscriber sub = it.subscribe("camera/image2", 1, imageCallback);
  ros::spin();
  cv::destroyWindow("view");
}
