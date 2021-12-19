# Quality Street Problem

## Introduction
This is inspired by a post I saw on Facebook where people seemed concerned that there was an uneven distribution of sweets in packets of Quality street as in the image below:

<img src="Sweet_selection.jpg" width="400">

This is quite interesting, since you might expect an equal number of each, right?

However, it's obvious that if you select at random from an equal probability, it is highly unlikely that the outcome is equal. Why? Because there are many more ways to select for an uneven distribution than for an even one. Okay, that is easy enough, but what should you expect and how would you check if the distribution is really random or not?  Lets formalize these questions more clearly:

Suppose the total number of sweets is N, the number of types is K, and the probablity of selecting a given type at each draw is $$p^{(i)} = 1/K$$

#### Q1: What is the most likely distribution of numbers of sweets after re-ordering accorging the number in each category?
#### Q2: What is the probability that a given outcome $Y = (n_1, n_2, \hdots, n_K)$, where the indices specify the original (unordered) categories?


### Theory
What I find both interesting and difficult in statistics is navigating the different types of probability. They can be categorised as follows:
1. Frequentist - The average expected outcome of an infinite number of events
2. Bayesian - The probability of a certain result given a finite set of data and prior expectations

In retrospect Q1 is frequentist and Q2 is Bayesian. In both cases we assume that the underlying probability distribution is evenly distributed, ie. $p(x_1) = p(x_2) = \hdots = p(x_N)$. 
#### A:Q1 is frequentist
ie., given 
$$p(x_i)=1/K$$  and   
$$\sum_i p(x_i) = 1$$   
then $$<p(y_j)> = \sum_{j=1}^m sort(p(x))^{(j)}/m$$
The probablitily distribution p(x) is a multinomial distribution and can be simulated by a random variable.

r draws from 