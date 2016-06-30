Title: timeit module python
Date: 2016-06-30
Category: Python
Author:kaustuv deolal
Summary: Measure the running time of your loops and compare various functions

*timeit*  is a usefule python module , that helps you see the running time of various statements in python

###Example

 ```python
 import timeit 
 timeit.timeit("map(str,range(1000)",number=10000)
 timeit.timeit("[str(i) for i in range(1000)]",number=10000)
 ```

 ###The output would be:

 ![alt text](https://raw.githubusercontent.com/Vutsuak16/Vutsuak16.github.io/master/content/images/timeit.PNG )

 

