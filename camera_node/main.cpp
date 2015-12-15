#include <ros/ros.h>
#include <stdlib.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>
#include <python2.7/Python.h>

using namespace std;

int main(int argc, char** argv)
{
  PyObject *pName, *pModule, *pDict, *pFunc, *pValue;
  Py_Initialize();
 // pName = PyString_FromString("/home/pi/ros_catkin_ws/src/rosberrypi_cam/src/stepper3d.py");
 // pModule = PyImport_Import(pName);
 // pDict = PyModule_GetDict(pModule);
 // pFunc = PyDict_GetItemString(pDict,"forward");
  PyRun_SimpleString("import time\n"
                      "import RPi.GPIO as GPIO\n"
			"GPIO.setmode(GPIO.BCM)\n"
			"GPIO.setup(18, GPIO.OUT)\n"
			"GPIO.setup(27, GPIO.OUT)\n"
			"GPIO.setup(4, GPIO.OUT)\n"
			"GPIO.setup(17, GPIO.OUT)\n"
			"GPIO.setup(23, GPIO.OUT)\n"
			"GPIO.setup(24, GPIO.OUT)\n"
			"GPIO.output(18, 1)\n"
                     	"GPIO.output(27, 1)\n"
                        "print('setup done')\n"
);
  cv::VideoCapture cap(0);
  // Check if video device can be opened with the given index
  if(!cap.isOpened()) return 1;
  cv::Mat frame;
  cap.set(CV_CAP_PROP_FRAME_WIDTH,240);
  cap.set(CV_CAP_PROP_FRAME_HEIGHT,280);
  sensor_msgs::ImagePtr msg;
  ros::init(argc, argv, "image_publisher");
  ros::NodeHandle nh;
  image_transport::ImageTransport it(nh);
  image_transport::Publisher pub = it.advertise("camera/image", 1);

  ros::Rate loop_rate(5);
  while (nh.ok()) {
    cap >> frame;
    PyRun_SimpleString(
  "for i in range(0, 1):\n"
  "  GPIO.output(4, 1)\n"
  "  GPIO.output(17, 0)\n"
  "  GPIO.output(23, 1)\n"
  "  GPIO.output(24, 0)\n"
                  	"  time.sleep(0.7)\n"
  "  GPIO.output(4, 0)\n"
  "  GPIO.output(17, 1)\n"
  "  GPIO.output(23, 1)\n"
  "  GPIO.output(24, 0)\n"
			"  time.sleep(0.7)\n"
  "  GPIO.output(4, 0)\n"
  "  GPIO.output(17, 1)\n"
  "  GPIO.output(23, 0)\n"
  "  GPIO.output(24, 1)\n"
			"  time.sleep(0.7)\n"
  "  GPIO.output(4, 1)\n"
  "  GPIO.output(17, 0)\n"
  "  GPIO.output(23, 0)\n"
  "  GPIO.output(24, 1)\n"
			"  time.sleep(0.7)\n"
                     );
   // PyObject_CallObject(pFunc, NULL);

  //Check if grabbed frame is actually full with some content
    if(!frame.empty()) {
      msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", frame).toImageMsg();
      pub.publish(msg);
      cv::waitKey(2000);
    }

    ros::spinOnce();
    
    loop_rate.sleep();
  }
  Py_DECREF(pModule);
  Py_DECREF(pName);
  Py_Finalize();
}
