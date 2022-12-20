# Graph Isomorphism Project - Team 40
---
### This project explores several algorithms that can solve the graph isomorphism problem.

#### The Algorithms that are implemented so far are:
- Color Refinement
- Individualization Refinement

#### Optimizations:
- Prime coloring for Color Refinement:
> Checking whether two vertices in a graph have identically coloured neighbourhoods can easily be optimized by using prime numbers to color every vertex. Traditionally we would have to sort the neighbours of both vertices and then compare them one by one. This requires O(nlog(n)+n) operations. However, by using prime numbers as colors, we can leverage the fact that every positive integer has a unique prime factorization. This means multiplying all the colors in a neighbourhood will yield a unique product for every possible neighbourhood, i.e. it is an invariant. We can therefore check if two neighbourhoods are identically coloured, by comparing these invariants, which only requires O(n) operations.

> As a bonus, we can also use this invariant to check if a coloring is balanced by comparing the products of all colors of the first graph against the products of all colors of the second graph.

- Color counting for Individualization Refinement:
> Individualization refinement requires us to find duplicate colors in a graph. The theoritically fastest approach is to iteratively store the colors in a hash set. If the color is already present we know we have found a duplicate color. The insertion and look up have constant time complexity, but the spacial complexity is quite bad. Fortunately, there is a better method. During color refinement we are assigning the colors our selves, so we can simply keep track of the counts for virtually no extra cost. This method has the same time complexity as the hash set method, namely O(n), but a much better memory footprint. It is probably quite a bit faster as well, but this depends on the hashing algorithm used in the hash set implementation.