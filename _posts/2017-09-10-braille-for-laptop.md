---
layout: post
title: Braille Printer for Text Document
description: "A hardware setup that lets blind people read those text files"
comments: true
keywords: "arduino, python, embedded, C, braille"
---

This blog post is about an interesting project I did a while ago. The aim for the project was to create a printer setup that generated braille for text files in our personal computers. This would be of immense help for optically challenged people who struggled to read something on text files. So I teamed up with a friend of mine who was from electronics backgroud to create such a setup. 
The basic setup involved an arduino that read text files character by character. The character was converted to braille using an algorithm written in embedded C. The reaader would just have to have his hand on the setup and read what character was being created as braille. The hardware setup is made by soldering a circuit that was attached to pins. A very basic printer prototype, the pins would print out various manifestations of the braille. The hardware is controlled by arduino.
The printer program had two parts

* Python program that parses that passes data character by character to the Arduino attached  
* An embedded C program that reads the input and controls the pin movement of our rudimentary printer

### Parsing the text and sending it to the Arduino

```python
import serial
import time
f = open("/home/kaustuv/Desktop/text", "r") # change the path here and install pyserial module of python
string = (f.readline()).strip()
arduino1 = serial.Serial(port="/dev/ttyUSB1", baudrate=9600)
for i in string:
        #time.sleep(2)
        print i
        arduino1.write(i)
```

The main python module used is [pyserial](https://pythonhosted.org/pyserial/index.html)

### Program controlling the pin movements

![braille_output]({{'/assets/images/braille-output.png' | prepend: site.baseurl }})

The program above is stored in the microcontroller memory and function with respect to the input

For the complete code here is the link to the [repository](https://github.com/Vutsuak16/Braille)








