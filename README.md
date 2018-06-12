# compute_posteriori

[![Build Status](https://travis-ci.org/SanyTiger/compute_posteriori.svg?branch=master)](https://travis-ci.org/SanyTiger/compute_posteriori)

Source [Wikipedia](https://en.wikipedia.org/wiki/Posterior_probability)
>
Posterior probability of a random event or an uncertain proposition is the conditional probability that is assigned after the relevant evidence or background is taken into account. Similarly, the posterior probability distribution is the probability distribution of an unknown quantity, treated as a random variable, conditional on the evidence obtained from an experiment or survey. "Posterior", in this context, means after taking into account the relevant evidence related to the particular case being examined. 


### This project is aimed at computing the posterior probability for any given sequence of candy and lime.
```
View learning as Bayesian updating of a probability distribution over the hypothesis space.
H is the hypothesis variable, values h1, h2, . . ., prior P(H)
ith observation xi gives the outcome of random variable Xi
training data X=x1, . . . , xN
```

> Five kinds of bags of candies.
```
–10% are h1: 100% cherry candies
–20% are h2: 75% cherry candies + 25% lime candies
–40% are h3: 50% cherry candies + 50% lime candies
–20% are h4: 25% cherry candies + 75% lime candies
–10% are h5: 100% lime candies
```


> Each bag has an infinite number of candies.–This way, the ratio of candy types inside a bag does not change as we pick candies out of the bag.


> We have a bag, and we are picking candies out of it.


> Based on the types of candies we are picking, we want to figure out what type of bag we have.

