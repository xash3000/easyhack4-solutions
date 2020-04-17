It is easy to see that Ashraf can do three type of operations: divide by 2, divide by 3 and divide by 5.

Let’s write both given numbers in the form

a = x * 2^a2 * 3^a3 * 5^a5, b = y * 2^b2 * 3^b3 * 5^b5, where x and y are not dibisible by 2, 3 and 5.

If x ≠ y the fox can’t make numbers equal and program should print -1.

If x = y then soluion exists. The answer equals to |a2 - b2| + |a3 - b3| + |a5 - b5|.

because |a2 - b2| is the minimal number of operations to have 2 in the same power in both numbers, |a 3 - b 3| is the minimal number of operations to have 3 in the same power in both numbers, and |a 5 - b 5| is the same for 5.
