---
layout: post
title: "A random sorting algorithm"
description: "Introduces a random sorting technique, that dawned upon me. It would be already present,but still is worth sharing"
comments: true
keywords: "sorting, simple, python"
---

### What is this post about.?

One day I was pouring myself over a few sorting algorithms like quicksort,mergesort etc. The in an instant a sorting idea dawned upon me.
The idea by no means is unique, it in all probability would have been in existence, but it was random for me.

### How it works 

The algorithm uses basic iteration to sort elements in a list or an array. The loop ranges from the minimum element in the array to the max element.
In the process all the intermediate elements are covered. It the checks if the iterating element is present in the array, if True it simply prints it or 
adds it to a new list

### Code

It is a one line code, where l is the list of elements:

        k=[i for i in range(min(l),max(l)+1) if i in l]


### Output
        
![simple-sort]( {{'/assets/images/simple_sort.PNG' | prepend: site.baseurl }})


