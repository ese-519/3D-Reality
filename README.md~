#System overview

There should be a minimum of:

- At least one Raspberry pi with a camera. This node will also be responsible for running stepper motor.

- At least one Raspberry Pi at the recieving end. This node processes the images and renders them to a VR headset or a screen.

- At least one VR headset to be connected to the client Raspberry Pi node to view the images.

- One Raspberry Pi as a WiFi AP. This AP will connect all the nodes and will run roscore.


#Guide:

The guide will go over how to setup each component.

**Raspberry Pi (Camera nodes):**

There should be at least one Raspberry Pi acting as a Camera node. If multiple camera nodes exist, one of them should be controlling the stepper motor.

The file main.cpp is the ROS node responsible for driving the stepper motor, taking images and sending them over a compressed ROS image topic.

**Raspberry Pi (Client nodes):**

There should be at least one Raspberry Pi acting as a client node. The file my\_subscriber.cpp is the ROS node responsible for listening for images being broadcasted on the compresses images topic. If there are more than one camera, an additional listener shold be activated to listen to the other topic.

The file demo_test.py is responsible for concating the images to create the 3D experience and render the images that can be navigated using Pygame.

**Raspberry Pi (WiFi AP):**

Follow the directions in this website: https://learn.adafruit.com/setting-up-a-raspberry-pi-as-a-wifi-access-point/overview

**VR headset**

The VR headset are simply plug and play.


#Notes:

- The hostnames for all the nodes should be registered in the /etc/hosts file along with the assigned IPs. 

- Make sure the dependecies are fully installed. The dependencies include ROS, Pygame, and OpenCV.


#Further improvements

- Auto-calibration
