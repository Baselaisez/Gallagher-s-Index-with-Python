# Gallagher-s-Index-with-Python
 Gallagher's Index for multi-party and two-party tendencies
Here's a suggested "README" content for your GitHub repository:

---

# Gallagher's Index Calculator

## Overview

This repository provides a Python implementation to calculate Gallagher's index, which measures the disproportionality in electoral systems. Gallagher's index is a statistical tool used to determine the extent to which the distribution of seats in a legislature differs from the distribution of votes among the political parties.

## What is Gallagher's Index?

Gallagher's index, developed by Michael Gallagher, is widely used in political science to evaluate how proportional an electoral system is. The index is particularly relevant in assessing the fairness of electoral outcomes in various democracies. A lower Gallagher index indicates a more proportional electoral system, where the share of seats closely mirrors the share of votes. Conversely, a higher index points to greater disproportionality, often favoring larger parties at the expense of smaller ones.

The formula for calculating the Gallagher index is:

  “G\=21​∑i\=1n​(vi​−si​)2​”

Where:
 vi = percentage of votes received by party(i)
 si = percentage of seats won by party(i)
 n = total number of parties

## Features

- **RAE (Relative Advantage of Electoral Systems)**: A function to calculate the relative advantage of electoral systems.
- **Effective Number of Parties**: A function to determine the effective number of parties using Laakso and Taagepera's method.
- **Gallagher Index Calculation**: A core function to calculate the Gallagher index based on vote and seat distributions.

## Code Implementation

The Python code provided in this repository calculates Gallagher's index using the `gallagher` function. It takes two lists as input: one representing the percentage of votes and the other representing the percentage of seats. The function computes the square root of half the sum of squared differences between these two lists, yielding the Gallagher index.

```python
import numpy as np

import numpy as np

def rae(*args):
    squared = [i**2 for i in args]
    E = 1 - sum(squared)
    return E

def effect(*args):
    squared = [i**2 for i in args]
    E = 1 / sum(squared)
    return E

def taking(*args):
    return args

def gallagher(v1, v2):
    arr = list(np.array(v1) - np.array(v2))
    sqrd_nums = [x**2 for x in arr]
    sm = sum(sqrd_nums)
    res = ((sm) * 0.5)**0.5
    return res

```

### Usage

To use the Gallagher index function, simply pass two lists: the first list for vote percentages and the second list for seat percentages. For example:

```python
votes = [40, 30, 20, 10]  # Vote distribution
seats = [45, 25, 20, 10]  # Seat distribution

gallagher(votes, seats)
```

This will calculate and print the Gallagher index for the provided data.

## Contributions

Feel free to contribute to this project by submitting issues or pull requests. Let's make the tool more versatile and applicable to various electoral systems worldwide.
