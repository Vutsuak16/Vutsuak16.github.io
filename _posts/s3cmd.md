---
layout: post
title: "s3cmd for Amazon S3"
description: "Introduces s3cmd,a command line tool to manage data in Amazon S3 buckets"
comments: true
keywords: "cloud, S3, AWS, command-line"
---

Amazon S3 is a web service offered by Amazon. It comes under the header of Amazon Web Services(AWS). Amazon S3 has become a widely used Data Storage medium because of its reasonably cost and ease of use. 
It is widely used by corporates and startups. The data is stored in S3 objects called *buckets*. To play around with the contents of S3 buckets, we have *s3cmd*, a very useful command line tool, that allows us to interact directly and securely with the contents in our S3 buckets.
It supports various operations like delete, fetch, upload etc.

### Installation

*s3cmd* requires python 2.6x or newer.It is not compatible with python3.

####For Redhat, CentOs & Fedora systems:

     sudo yum --enablerepo updates-testing install s3cmd

####For Ubuntu & Debian systems:

Import S3tools signing key: 
    wget -O- -q http://s3tools.org/repo/deb-all/stable/s3tools.key | sudo apt-key add -

Add the repo to sources.list:
    sudo wget -O/etc/apt/sources.list.d/s3tools.list http://s3tools.org/repo/deb-all/stable/s3tools.list

Refresh package cache and install the newest s3cmd: 
    sudo apt-get update && sudo apt-get install s3cmd

####For windows:


### A standard example of Usage 

It can be used both as a command line application as well as a module

*command line*
S

![command]( {{'/assets/images/command.PNG' | prepend: site.baseurl }})


*as a module import*



![module]({{'/assets/images/script.PNG' | prepend: site.baseurl }})


### Integration with Jupyter/Ipyhon

 Cool stuff is that timeit is build into both Jupyter and Ipython as a magic function. 
 It can be executed by using the simple *%* operator.


![module]({{'/assets/images/ipython.PNG' | prepend: site.baseurl }})









