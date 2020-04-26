We have an array of size N, A[i] and an integer G. Robbers can successfully execute the plan if within a time period of G, each one of them is able to visit vault for A[i] time and not more than two robbers are present into vault at any time.

Let us define sum(S) where S is a set as sum of all elements in the S.
So, if we are able to divide array A into two disjoint subsets set1 and set2 such that set1 union set2 = A and set1 intersection set2 = NULL, and sum(set1)<=G and sum(set2)<=G, it's is possible to execute the plan.

Therefore, sum(set1) <= G
sum(set2) <= G
sum(set1) + sum(set2) = sum(A)

From above three equations, if there exists any set X such that
(sum(A) – G) <= sum(X) <= G (obviously (sum(A)-G)<=G holds)
then our solution is possible.

The above condition can be checked by using classic Dynamic programming problem subset sum problem.