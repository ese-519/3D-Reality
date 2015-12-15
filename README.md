#System overview

There should be a minimum of:

At least one Raspberry pi with a camera. This node will also be responsible for running stepper motor.

At least one Raspberry Pi at the recieving end. This node processes the images and renders them to a VR headset or a screen.

At least one VR headset to be connected to the client Raspberry Pi node to view the images.

One Raspberry Pi as a WiFi AP. This AP will connect all the nodes and will run roscore.


#Guide:

The guide will go over how to setup each component.

##Raspberry Pi (Camera nodes):

main.cpp

##Raspberry Pi (Client nodes):

my_subscriber.cpp

##Raspberry Pi (WiFi AP):

Follow the directions

VR headset

Plug and play


#Notes:

hostnames

dependencies

#Further improvements

