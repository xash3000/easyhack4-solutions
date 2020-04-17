If A and B have the same parity (that's they're both even or both odd), the  first player should lose all matches and the second player should win all matches. In this case, they will meet after (B - A)/2 rounds.

Suppose that A and B have different parity. If the players just move towards each other, they can get very close (to neighboring tables), but they can't meet. The only way to change parity is winning at table 1 or losing at table N.

We need to consider only two cases:

- The first player moves to table 1, wins an additional game there, and moves towards the second player, who just moves towards table 1 for the whole time, until they meet.

- Similarly, the second player moves to table N, loses an additional game there, and moves towards the first player, who just moves towards table N for the whole time, until they meet.

The smallest number of rounds is then min(A - 1, N - B) + 1 + (B - A - 1)/2

Here min(A - 1, N - B) stands for the number of rounds needed to reach table 1 or table N. the (+ 1) term is for additional round to change parity and (B - A - 1)/2 stands for the number of rounds before the friends meet after changing parity (which is half the distance between them)
