---
layout: post
title: Magic Commands in Jupyter Notebook
description: "The post outlines some clever shortcuts one can use in a jupyter notebook"
comments: true
keywords: "jupyter, Python,notebook"
---

It has been sometime since I wrote something. Grad school has kept me busy. But I am back now . Here in this short post I would like to outline my favourite **magic commands**. The word may sound misleading but it indeed is no less than magic. These commands are provided by the IPython kernel and come in handly especially when there is plotting and data work involved. They also can help us to get an estimate of the code complexity.

### Magic Commands

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









