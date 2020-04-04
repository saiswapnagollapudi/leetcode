Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

The simple way to solve this problem in linear time is to intialize new variables sum(to zero) and max(to first element of array).

lopping over elements of array compute the sum+a[i] if this new sum is greater than max then replace max. Also max value will be increased if sum is greater than zero only. If sum is less than we can replace it with zero.
