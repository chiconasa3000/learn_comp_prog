'''
first state
1 difference  catching two 2 numbers
save current sign
could be (+) or (-)
test next difference (close to or far to)
if they have similar signs add zero
'''

'''
second state
2 difference  catching two 3 numbers
could be (+)(-)
could be (-)(+)
adding one 
possible structure
'''

'''
saving a dictionary
2 differences
c-b , b-a
dic[a_i, b_i, c_i] = [0,1]
'''

'''
dependency
if signs are different (sucesful state) (dep)
decomposing

decompose step

dic[a_i-1, b_i, c_i] + 1 or 
dic[a_i, b_i-1, c_i] + 1 or 
dic[a_i, b_i, c_i-1] + 1

'''

'''
possible states
and none index should be equal
(a_i, b_i, c_i) should be ascending order
a_i < b_i < c_i

choose maximum possible state
max(dic[a_i - 1, b_i, c_i],dic[a_i, b_i-1, c_i],dic[a_i, b_i, c_i-1])
'''