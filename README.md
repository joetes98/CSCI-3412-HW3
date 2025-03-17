# CSCI 3412 HW 3
## Question 1
###
1-1 <br/>
**Time for recursive solution:** 0.196580171585083 seconds <br/>
**Time for iterative solution:** 0.1880195140838623 seconds <br/>
The iterative solution is faster.

1-2 <br/>
For each index we need to determine if the element is a plateau or valley. Starting at the 0th index we alternate valley[0], plateau[1], valley[2], plateau[3], valley[4], plateau[5], ...

The pattern for this array is the even numbered indices are valleys, while the odd numbered indices are plateaus.

Algorithm:
Iterate through the array, determine whether the index is even or odd (i % 2 == 0 or i % 2 == 1). If the index is even, check whether array[i] < array[i+1]. If this condition is not met, we swap the elements. If the index is odd, check whether array[i] > array[i+1]. If this condition is not met, we swap the elements. Since we are only iterating through the array once, the time complexity is O(n).


## Question 2
###
2-1 <br/>
Included as 2-1.pdf <br/>
2-2  <br/>
Included as 2-2.pdf

## Question 3
###
3-1 <br/>
Included as 3-1.pdf

###
3-2 <br/>
Below is the results finding the optimal k values. K-Values 2-22 were test. <br/><br/>

**Each K value tested 5 times** <br/>

2. 1.4312759399414063 <br/>
3. 1.6154974937438964 <br/>
4. 1.4112919807434081 <br/>
5. 1.3247796058654786 <br/>
6. 1.5746757507324218 <br/>
7. 1.2898841381072998 <br/>
8. 1.313675308227539 <br/>
9. 1.3294958114624023 <br/>
10. 1.2865690231323241 <br/>
11. **1.2838677406311034** <br/>
12. 1.3163884162902832 <br/>
13. 1.3055459022521974 <br/>
14. 1.3726828575134278 <br/>
15. 1.3350430965423583 <br/>
16. 1.360042428970337 <br/>
17. 1.3559007167816162 <br/>
18. 1.3814701557159423 <br/>
19. 1.3897233486175538 <br/>
20. 1.4259849548339845 <br/>
21. 1.5767258644104003 <br/>
22. 1.7288710594177246 <br/>
<br/>

## Optimal K Value:  11 <br/>
Graph included Optimal_K_Value.png <br/>
![image info](Optimal_K_Value.png) <br/><br/>

##

**Each K value tested 20 times** <br/>

2. 1.2618485689163208 <br/>
3. 1.2137242197990417 <br/>
4. 1.2142524719238281 <br/>
5. 1.220571756362915 <br/>
6. 1.2336604952812196 <br/>
7. 1.2185327768325807 <br/>
8. 1.2306268215179443 <br/>
9. 1.2274431347846986 <br/>
10. **1.2101097583770752** <br/>
11. 1.2969412088394165 <br/>
12. 1.3622915744781494 <br/>
13. 1.3954447031021118 <br/>
14. 1.3582767128944397 <br/>
15. 1.3177013635635375 <br/>
16. 1.2682873845100402 <br/>
17. 1.2840245127677918 <br/>
18. 1.2898702144622802 <br/>
19. 1.301029086112976 <br/>
20. 1.3140926361083984 <br/>
21. 1.343756866455078 <br/>
22. 1.3554450154304505 <br/>
<br/>

## Optimal K Value: 10 <br/>
Graph included Optimal_K_Value2.png <br/>
![image info](Optimal_K_Value2.png)



