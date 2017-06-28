---
layout: post
title: "Data visualization using Elasticsearch Logstash and Kibana"
description: "Measure execution time of small code"
comments: true
keywords: "python, execution time, alogorithms, Ipython"
---

Everyone of us has done alogorithmic design. Many time such situations arise when we have to find execution time of our code snippets.There are instances when we have to compare executions of two different algorithms to find which is more efficient.Such analysis is very handy for research and production purposes, where a small change in time could mean having a significant overall impact.
In such situations we can use the awesome *timeit* library. It is a small and efficient module for finding the execution time of python scripts. It implots the use of a platform-specific time function to provide the most accurate time calculation possible. It reduces the impact of startup or shutdown costs on the time calculation by executing the code repeatedly.

### Installation
Not required!!. It ships in with python installation itself.


### A standard example of Usage 

It can be used both as a command line application as well as a module

*command line*


![command]( {{'/assets/images/command.PNG' | prepend: site.baseurl }})


*as a module import*



![module]({{'/assets/images/script.PNG' | prepend: site.baseurl }})


### Integration with Jupyter/Ipyhon

 Cool stuff is that timeit is build into both Jupyter and Ipython as a magic function. 
 It can be executed by using the simple *%* operator.


![module]({{'/assets/images/ipython.PNG' | prepend: site.baseurl }})









