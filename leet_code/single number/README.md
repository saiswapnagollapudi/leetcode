**Given a non-empty array of integers, every element appears twice except for one. Find that single one.**

The best way to solve this problem in O(n) time without using extra memory is using the logic of xor.

For any given number x, x^x = 0 and x^0 = x.

As all the numbers except one appears twice Ex: [2,1,1] if we initialize a variable say a to 0 and then apply xor to each element in the 
input array then the resulting number will be the one which appeared only once. 
