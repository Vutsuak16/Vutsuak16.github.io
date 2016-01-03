---
layout: post
title:  "desktop to arduino"
date:   2016-1-2 19:26:45
categories: script
---


This script sends text filr data from desktop to arduino, via serial communication
{% highlight python %}

__author__ = 'kaustuv'

import serial
import time
f = open("/home/kaustuv/Desktop/text", "r") # change the path here and install pyserial module of python
string = (f.readline()).strip()
arduino1 = serial.Serial(port="/dev/ttyUSB1", baudrate=9600)
for i in string:
        #time.sleep(2)
        print i
        arduino1.write(i)

{% endhighlight %}

Checkout the rest of the project at [desktop-arduino][github]. This also includes the SQL and GUI part  

[github]:    https://github.com/Vutsuak16/Braille/blob/master/Arduino.py