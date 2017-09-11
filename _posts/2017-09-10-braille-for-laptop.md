---
layout: post
title: Braille for Text Document
description: "A hardware setup that lets blind people read those text files"
comments: true
keywords: "arduino, python, embedded, C, braille "
---

This blog post is about an interesting project I did a while ago. The aim for the project was to create a setup that generated braille for text files in our personal computers. This would be of immense help for blind people who struggled to read something on text files. So I teamed up with a friend of mine who was from electronics backgroud to create such a setup. 
The basic setup involved an arduino that read text files character by character. The character was converted to braille using an algorithm written in embedded C. The reaader would just have to have his hand on the setup and read what character was being created as braille. 

### The Word Count

```scala
val inputFile = sc.textFile("/Users/vutsuak/Desktop/Big-Data-withSpark/wordcount/dataset/cucumber.txt")
val counts = inputFile.flatMap(line => line.split(" ")).map(word => (word,1)).reduceByKey(_+_)
counts.saveAsTextFile("/Users/vutsuak/Desktop/Big-Data-withSpark/wordcount/output")
System.exit(0)
```

The code above has two main compnent of spark they are  : _Transformation_ and _Action_

Transformation is basically taking a RDD value and return multiple RDDs or a changed RDD, ```flatMap``` above does that for us. Action is an operation on RDD that produces a non RDD values like the ```saveAsTextFile```
operation above

### The output 

![spark-output]({{'/assets/images/output-spark.png' | prepend: site.baseurl }})

The output is split in multiple files (2 files is the default). This demonstrates parellism employed in Spark









