---
layout: post
title: Magic Commands in Jupyter Notebook
description: "The post outlines some clever shortcuts one can use in a jupyter notebook"
comments: true
keywords: "jupyter, Python,notebook"
---

It has been sometime since I wrote something. Grad school has kept me busy. But I am back now . Here in this short post I would like to outline my favourite **magic commands**. The word may sound misleading but it indeed is no less than magic. These commands are provided by the IPython kernel and come in handly especially when there is plotting and data work involved. They also can help us to get an estimate of the code complexity.

## Magic Commands

### %lsmagic

This is my goto magic function. This command outputs all the available magic functions in the Ipython-Kernel. A very good bet if you have want to find your favourite 
magic command or have a bad memory in general.

![lsmagic]({{'/assets/images/lsmagic.png' | prepend: site.baseurl }})

### %run

A very useful commands when one wants to run and display the output of another Ipython file. This is useful in data analysis work when we would like to display the visualization code written in another file.

![run]({{'/assets/images/run.png' | prepend: site.baseurl }})

### %matplotlib inline

As the name indicates this commands enables matplotlib in our jupyter notebook. It will make your plot outputs appear and be stored within the notebook.

![matplotlib-inline]({{'/assets/images/matplotlib.png' | prepend: site.baseurl }})











