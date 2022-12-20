# Graph G
# G' is a copy of graph G
# Apply color refinement to disjoint union of G and G'
# D = [x_1,...,x_l] and I = [y_1,...,y_l] which are sequences of vertices of G
# (D, I) is a prescribed mapping
# f : V(G) -> V(G) follows (D, I) if for all i element of {1,...,l}, f(x_i) = y_i holds
# if color refinement + branching of (D, I)
    # bijection - there is unique automorphism that follows (D, I)
    # unbalanced - exists no automorphism that follows (D, I)
    # otherwise - undecided
        # choose color class of size >= 4
        # vertex x element of V(G) in that class
        # for all y in branching cell C := vertices V(G') of that color recursively check the mapping (D + x, I + y)
        # Call x and C the branching vertex resp. branching cell/color