---
layout: post
title: Binary Insertion Sort 
description: "An interesting adjustment in insertion sort that changes its complexity to O(n*logn) for best cases"
comments: true
keywords: "searching, sorting, python, algorithms"
---

Recently I was brushing through some core algorithms concept particularly sorting. One resource which I would recommend everyone is the [MIT open courseware](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/ ) lectures on algorithms. These lectures are the source of this blog. 
All of us know insertion sort . It is a basic **inplace** sorting algorithm with a standard O(n^2) complexity. But with a little tweak, for some cases we come up with a simple O(nlogn) algorithm. This little tweak comes in form of **Binary Search**. 
The crux is we do away with the comparison portion of the insertion sort algorithm. Instead we find the optimal index to fit in our Key. That index is calculated by using **Binary Search**. We simple traceback to the index and adjust the array/list accordingly. We used the simple knowledge that all elements before the key are sorted and henceforth binary search can be applied. Since **binary search** is a O(logn) time complexity algorithm we are left with a simple yet efficient O(nlogn) insertion sort

### Binary Search that returns the best position

```python
def binary_search(val,l):

	start=0
	end=len(l)-1
	mid=(start+end/2)

	while start<=end:

		if val==l[mid]:
			return mid
			break
		elif val<l[mid]:
			end=mid-1
		else:
			start=mid+1

		mid= (start+end)/2

	return mid+1
```


### The insertion sort algorithm sans the comparisons

```python
def binary_insertion_sort(l):

	for i in range(1,len(l)):

		key=l[i]
		insert_pos=binary_search(key,l[:i])
		
		for j in range(i,insert_pos,-1):
			l[j],l[j-1]=l[j-1],l[j]
```



