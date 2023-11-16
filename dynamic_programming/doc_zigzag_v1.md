'''
sample:
[a=7,b=8,c=6] some subsequence 
1 1 1 7 1 1 1 1 8 1 1 1 1 6 1 1 1

difference != 0
'''

'''
base state
add 2 items more at the beginnig
# if indices are not in ascending order

[abc]
no more decompose
if(a_i > b_i or b_i > c_i or a_i > c_i ):
    return 0
'''

'''
first state
difference have equal signs in current idxs

(depends previous sign before to c)

dif_1 = dic[c_i] - dic[b_i]
dif_2 = dic[b_i] - dic[a_i]

if(prev_sign == "+"):    
    cond_dif_1 =  dif_1 < 0
    cond_dif_2 =  dif_2 > 0
elif(prev_sign == "-"):
    cond_dif_1 = dif_1 > 0
    cond_dif_2 = dif_2 < 0

different_signs = cond_dif_1 and cond_dif_2

complying zigzag condition
if(different_signs == true):
    # decompose in next subtree following 
    # the previous solution
    prev_sign = (dif_1 < 0) ? '-', '+'
    return zig_zag(a_i-1,a_i,b_i,prev_sign) + 1
'''

'''
dependency
if signs are equal testing other possible options
decomposing

decompose step
elif(different_signs == false):
    # equal signs 
    # decompose in three possible options

    # conditions
    00 equal to prev_sign and dif2 sign equal to dif1 sign
    
    # different to prev_sign
    cond_dif_1 == false
    # dif2 sign different to dif1 sign
    cond_dif_2 == true
    a b c d
     - + + 
    change (c and a) or (b and a)
    
    # equal to prev_sign
    cond_dif_1 == true
    # dif2 sign equal to dif1 sign
    cond_dif_2 == false
    a b c d
     + + - 
    change a or b

    # equal to prev_sign
    cond_dif_1 == false
    # dif2 sign equal to dif1 sign
    cond_dif_2 == false
    a b c d
     + + + 
    change c or b

    return max( [zig_zag(a_i-1, b_i, c_i), zig_zag(a_i, b_i-1, c_i), zig_zag(a_i, b_i, c_i-1)] )
'''