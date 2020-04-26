From the problem statement, we make two observations:

1. The more flowers a customer has already bought, the more dollars one needs to pay. We want to minimize the maximum number of flowers any friend buys, so the purchases will be as evenly distributed as possible.

2. We also need to optimize the order in which we purchase these flowers. The amount of additional money we need to pay later is linear in c[i]. We want to buy the most expensive flowers first, at the lower multiple.

Based on these observations, we know that we first need to sort the price of flowers in decreasing order, and then distribute these flowers evenly amongst our friends buying the most expensive first.
