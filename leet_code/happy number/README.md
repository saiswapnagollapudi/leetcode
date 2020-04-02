Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

A number continues to loop if a sum of squared value appears again in the loop. Here two variables fast and slow are created. Fast computes the sum of squares of given number twice and slow computes only one. Either if there is an infinite loop or if the numbers form infinte loop there will be a point where fast and slow are equal.

At that point we will return 1 if slow is 1(meaning happy number) else 0(meaning not a happy number).
