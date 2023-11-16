'''
sample:
[a=7,b=8,c=6] some subsequence 
1 1 1 7 1 1 1 1 8 1 1 1 1 6 1 1 1
return final answer with 1 more difference
'''

'''
base state
if indices are not in ascending order
no more decompose
if(a_i > b_i):
    dic[a_1][b_i] = 0
'''

'''
first state
dif = s[b_i] - s[a_i]

if(dif == 0):
    accepted_rule == false
elif((prev_sign == "+" and dif < 0) or (prev_sign == "-" and dif > 0)):    
    accepted_rule == true


complying zigzag condition
if(accepted_rule == true):
    # decompose in next subtree following 
    # the previous solution
    prev_sign = (dif < 0) ? '-', '+'
    dic[a_1][b_i] = zig_zag(a_i-1,a_i,prev_sign) + 1
'''

'''
dependency
if signs are equal testing other possible options
decomposing

decompose step
elif(accepted_rule == false):
    # equal signs 
    # decompose in three possible options
    change a or b
    
    dic[a_1][b_i] = max( zig_zag(a_i-1, b_i), zig_zag(a_i, b_i-1) )
'''

## debugging
# 2 sequences because it has a relation between two items (diffeernce between 2 numbers)
seq = 1, 17, 5, 10, 13, 15, 10, 5, 16, 8
idx = 1, 2,  3, 4,  5,  6,  7,  8, 9,  10