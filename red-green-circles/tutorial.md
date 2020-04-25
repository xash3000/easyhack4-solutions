It is easy to think when one operation is considered as a set.

Among N circles, the number of operations that is completely included in is floor(N / (A+B)).

The number of operations that is included halfway is at most one, but the remainder of N divided by A+B is only important.

let R be the remainder of A+B divided by N, then there are min(R, A) red balls included in a halfway operation.

total number of red circles is floor(N / (A+B)) * A + min(R, A)
