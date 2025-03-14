# CSCI 3412 HW 3
## Question 1
###
1-1 <br/>
Time for recursive solution: 7.152557373046875e-07 seconds <br/>
Time for iterative solution: 4.76837158203125e-07 seconds 

1-2 <br/>
For each index we need to determine if the element is a plateau or valley. Starting at the 0th index we alternate valley[0], plateau[1], valley[2], plateau[3], valley[4], plateau[5], ...

The patern for this array is that the even numbered indices are valley, while the odd numbered indices are plateaus.

Algorithm:
Iterate through the array, determine whether the index is even or odd (i % 2 == 0 or i % 2 == 1). If the index is even, check whether array[i] < array[i+1]. If this condition is not met, we swap the elements. If the index is odd, check whether array[i] > array[i+1]. If this condition is not met, we swap the elements. Since we are only iterating through the array once, the time complexity is O(n).


## Question 2
2-1 <br/>