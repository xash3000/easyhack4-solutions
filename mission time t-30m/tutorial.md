During each move, a player chooses one prime number and removes it (as well as its multiples) from the set. Because a player cannot move unless there is at least one prime number in the set and a single prime number is removed during each turn, we simply need to count the number of primes in the inclusive range [1,n] . If the number of primes is odd, Alice will remove the last prime number and win the game; otherwise, this number is even and Bob will choose the last prime number, winning the game.

You can get a 50% score if you generate prime numbers using a naive method. For a full score, you should use a Sieve of Eratosthenes algorithm.