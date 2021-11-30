# Quality Street Problem

## Introduction
This is inspired by a post I saw on Facebook where people seemed concerned that there was an uneven distribution of sweets in packets of Quality street as in the image below:

<img src="Sweet_selection.jpg" width="200">

I had two questions: Suppose the total number of sweets is N and the number of types is K and the probablity of selecting a given type at each draw is p(i) = 1/K
#### Q1: What is the most likely distribution of numbers of sweets after reordering accorging the number in each category?
#### Q2: What is the probability that a given outcome $Y = (n_1, n_2, \hdots, n_K)$, where the indices specify the original (unordered) categories?


### Theory
What I find both interesting and difficult in statistics is navigating the different types of probability. They can be categorised as follows:
1. Frequentist - The average expected outcome of an infinite number of events
2. Bayesian - The expectation of certain results given a finite set of data and prior expectations

In retrospect Q1 is frequentist and Q2 is Bayesian. In both we assume that the underlying probability distribution is evenly distributed, ie. $p(x_1) = p(x_2) = \hdots = p(x_N)$

