---
layout: post
title: Word Count in Spark
description: "The code counts the number of words in a document"
comments: true
keywords: "scala, spark, big-data"
---

I have been doing big data and machine learning for some time now, recently I had gained significant interest in Spark. I would like to share some of my insights here. Spark is an extremely efficient cluster computing framework. It just blows your mind away with it lightening fast "in memory processing". But one thing I would recommend for everyone is to **use spark with Scala** . Scala is a beautiful language and fits perfectly with spark's ecosystem. There are multiple resources avalible online to learn Scala. Personally I began with this amazing course [Functional Programming in Scala](https://www.coursera.org/learn/progfun1). It is taught by the creater of the language - Martin Odersky. 
In the blogspot I would be showing a very small piece of code I have written. It is called the word count a script that counts the words in a particular text file. It is the "Hello World" in the Big Data world. I wanted to try it using scala and spark. The code demonstrates the parellism applied by spark the functional nature of Scala programming laguage.

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









