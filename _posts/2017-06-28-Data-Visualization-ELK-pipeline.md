---
layout: post
title: "Data visualization using Elasticsearch Logstash and Kibana"
description: "Measure execution time of small code"
comments: true
keywords: "python, execution time, alogorithms, Ipython"
---

Elasticsearch Logstash and Kibana popularly abbreviated as ELK is a modern data aggregation, data querying and data visualization tool.
All the compnents of the ELK stack are seamlessly integrated for working coherently. ELK stack is fast gaining popularity and is being adopted by
corporate conglomerates too. It has a simple setting up process and even simpler learning curve. I will introduce in brief the three components of ELK stack.


### Elasticsearch

Elasticsearch is a schema free search engine, based on Lucene. It provides various REST APIs to query across data. It is fast because it queries
data based on Index. It is like searching the contents of book through its index. Data in index is organized on basis of documents.An index can contain
multiple documents. Elasticsearch centrally stores our data.
An example of its REST API is the *GET* API that searches across multiple or unique indexes.
It can executed through the console/command line via *CURL* or one can use [POSTMAN](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en)
CURL syntax is as follows for a simple *GET* query:
    
    `curl -XGET 'localhost:9200/twitter/tweet/0?pretty'`

It returns a json document for the index `twitter` and document id `tweet`




### Logstash


### Kibana







