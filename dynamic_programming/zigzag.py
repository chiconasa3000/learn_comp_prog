from tabulate import tabulate

# # first testing with tabulation
def zig_zag_tabulation(seq, idx_a,idx_b, prev_sign):
    
    dic = [[None]*(idx_a+1) for i in range(idx_b+1)]

    for i in range(idx_a+1):
        for j in range(idx_b+1):
            
            # base state
            out_of_range = (idx_a==0 or idx_b==0)
            no_decreasing = (idx_a > idx_b)
            equal_indices = idx_a == idx_b

            # first state
            dif = seq[idx_b-1] - seq[idx_a-1]

            if(out_of_range or no_decreasing or equal_indices):
                dic[idx_a][idx_b] = 0

            elif(dif != 0):
                # update prev_sign
                if((prev_sign == '*') or (prev_sign == "+" and dif < 0) or (prev_sign == "-" and dif > 0)):
                    prev_sign = '-' if (dif < 0) else '+'
                    dic[idx_a][idx_b] = dic[idx_a -1][idx_a] + 1
                else:
                    # keep previous sign idx_b with the previous call
                    dic[idx_a][idx_b] = max( dic[idx_a-1][idx_b], dic[idx_a][idx_b-1] )

            else:
                # keep previous sign idx_b with the previous call
                dic[idx_a][idx_b] = max( dic[idx_a-1][idx_b], dic[idx_a][idx_b-1] )
    
    return dic[idx_a][idx_b], dic

# second testing with memoization
def zig_zag_memoization(seq, idx_a,idx_b, prev_sign,dic):
    # base state
    out_of_range = (idx_a==0 or idx_b==0)
    no_decreasing = (idx_a > idx_b)
    
    # first state
    dif = seq[idx_b-1] - seq[idx_a-1]

    if(out_of_range or no_decreasing):
        return 0

    # reuse state
    if(dic[idx_a][idx_b] != -1):
        return dic[idx_a][idx_b]
    
    if(dif != 0):        
        if((prev_sign == '*') or (prev_sign == "+" and dif < 0) or (prev_sign == "-" and dif > 0)):
            # update prev_sign
            prev_sign = '-' if (dif < 0) else '+'
            dic[idx_a][idx_b] = zig_zag_memoization(seq,idx_a -1,idx_a,prev_sign,dic) + 1
        else:
            # keep previous sign idx_b with the previous call
            dic[idx_a][idx_b] = max( zig_zag_memoization(seq, idx_a-1, idx_b,prev_sign,dic), zig_zag_memoization(seq, idx_a, idx_b-1,prev_sign,dic) )
    
    else:
        # keep previous sign idx_b with the previous call
        dic[idx_a][idx_b] = max( zig_zag_memoization(seq, idx_a-1, idx_b,prev_sign,dic), zig_zag_memoization(seq, idx_a, idx_b-1,prev_sign,dic) )
    
    return dic[idx_a][idx_b]

if __name__  == '__main__':
    sequence = [374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 
600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 
67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 
477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 
249, 22, 176, 279, 23, 22, 617, 462, 459, 244]
    lenseq = len(sequence)
    headers = list(range(1,lenseq+1))
    print("using memoization")
    
    dic = [[-1 for i in range(lenseq+1)] for j in range(lenseq+1)]
    print("Length of zigzag seq: ", zig_zag_memoization(sequence, lenseq,lenseq,"*",dic)+1)
    print(tabulate(dic,headers=["#"] + headers, showindex=["#"]+headers))
    print()

    # print("using tabulation")
    # lenseq = len(sequence)
    # res, dic = zig_zag_tabulation(sequence, lenseq-1,lenseq,"*")
    # print("Length of zigzag seq: ", res)
    # print(tabulate(dic,headers=["#"] + sequence, showindex=["#"]+sequence))
    # print()
    