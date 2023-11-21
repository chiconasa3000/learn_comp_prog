10 1 10 1 10

1 <= A[1] <= 10
1 <= A[2] <= 1
1 <= A[3] <= 10
1 <= A[4] <= 1
1 <= A[5] <= 10

[[1-10],[1],[1-10],[1],[1-10]]
10*10*10 = 100 possible options

check differences where item has a max value and min value

using brute force:
check all possible arrays in A

using other option:
check maximum difference between every pair in A

1	1	1	1	1
100	2	100	2	100
	
without check the correspondence items
get the maximum difference

# 2 possible options in every pair

2[1,100], 100[1,2]	
{2,100}:98 {1,100}:99

100[1,2], 2[1,100]	
{100,1}:99 {100,2}:98

2[1,100], 100[1,2]	
{2,100}:98 {1,100}:99

100[1,100], 2[1,100]	
{100,1}:99 {100,2}:98

select the next pair considering the last item pair
from the last position (descending order)

assuming the second option {1,8}
{1,8} {8,1} {1,10}
A = [10, 1, 8, 1] sum: |1-10| |8-1| |1-8| = 9+7+7=23

assuming the first option {3,8}
{3,8} {8,1} {1,10}
A = [10, 1, 8, 3] sum: |1-10| |8-1| |3-8| = 9+7+5=21

----------------------------------------------------
select the next pair considering the last item pair
from the first position (ascending order)

assuming the second option {12,1}
there is no suboptions: (less option to check)
{12,1} {1,12} {null}
there is no 3th coincidence to complete the entire sequence

assuming the first option {1,10}
first suboption
{1,10} {8,1} {1,8}
A = [10 1 8 1] sum: |1-10| |8-1| |1-8| = 9+7+7=23
second suboption
{1,10} {8,1} {3,8}
A = [10 1 8 1] sum: |1-10| |8-1| |1-8| = 9+7+5=21


# testing with only one order ...

b = [100 2 100 2 100]



