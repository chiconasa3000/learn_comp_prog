from tabulate import tabulate
import graphviz

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
def zig_zag_memoization(seq, idx_a,idx_b, prev_sign,dic,tree):

    # base state
    out_of_range = (idx_a==0 or idx_b==0)
    no_decreasing = (idx_a > idx_b)
    
    # first state
    dif = seq[idx_b-1] - seq[idx_a-1]

    # draw current node
    #tree.node(f'{idx_a:d},{idx_b:d}',f'Dic:{dic[idx_a][idx_b]:d}-[{idx_a:d},{idx_b:d}]')
    if((idx_a==0 and idx_b!=0) or (idx_b==0 and idx_a!=0) or no_decreasing):
        return 0
    if(out_of_range):
        return 0
    
    
    # reuse state
    if(dic[idx_a][idx_b] != -1):
        return dic[idx_a][idx_b]
    
    #if(dif != 0):        
    if((prev_sign == '*') or (prev_sign == "+" and dif < 0) or (prev_sign == "-" and dif > 0)):
        # update prev_sign
        prev_sign = '-' if (dif < 0) else '+'
        dic[idx_a][idx_b] = zig_zag_memoization(seq,idx_a-1,idx_a,prev_sign,dic,tree) + 1
        # draw next edge
        #tree.edge(f'{idx_a:d},{idx_b:d}',f'{idx_a-1:d},{idx_a:d}',label=f'{dic[idx_a][idx_b]:d}')
    else:
        # keep previous sign idx_b with the previous call
        dic[idx_a][idx_b] = max( zig_zag_memoization(seq, idx_a-1, idx_b,prev_sign,dic,tree), zig_zag_memoization(seq, idx_a, idx_b-1,prev_sign,dic,tree) )
        # draw next edges
        #tree.edge(f'{idx_a:d},{idx_b:d}',f'{idx_a-1:d},{idx_b:d}',label=f'{dic[idx_a][idx_b]:d}')
        #tree.edge(f'{idx_a:d},{idx_b:d}',f'{idx_a:d},{idx_b-1:d}',label=f'{dic[idx_a][idx_b]:d}')
    
    #else:
        # keep previous sign idx_b with the previous call
        
        #dic[idx_a][idx_b] = max( zig_zag_memoization(seq, idx_a-1, idx_b,prev_sign,dic,tree), zig_zag_memoization(seq, idx_a, idx_b-1,prev_sign,dic,tree))
        # draw next edges
        #tree.edge(f'{idx_a:d},{idx_b:d}',f'{idx_a-1:d},{idx_b:d}',label=f'{dic[idx_a][idx_b]:d}')
        #tree.edge(f'{idx_a:d},{idx_b:d}',f'{idx_a:d},{idx_b-1:d}',label=f'{dic[idx_a][idx_b]:d}')
    
    return dic[idx_a][idx_b]

if __name__  == '__main__':
    #sequence = [1, 7, 4, 9, 2, 5] #6
    #sequence = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8] #7
    sequence = [44] #1
    #sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9] #2
    #sequence =  [70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32] #8
    #sequence = [374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 249, 22, 176, 279, 23, 22, 617, 462, 459, 244]
    #36
    #sequence = [5,5,5,5] 
    
    
    
    lenseq = len(sequence)
    headerss = list(map(lambda x:str(x), list(range(1,lenseq+1))))
    

    print("using memoization")
    tree = graphviz.Digraph('Dp_ZigZag', filename='zigzag',format='png')
    
    dic = [[-1 for i in range(lenseq+1)] for j in range(lenseq+1)]
    result_count = zig_zag_memoization(sequence, lenseq,lenseq,"*",dic,tree)
    print("Length of zigzag seq: ", result_count)
    #print(tabulate(dic,headers = ["#"] + headerss, showindex=["#"]+headerss))
    print()

    # print("using tabulation")
    # lenseq = len(sequence)
    # res, dic = zig_zag_tabulation(sequence, lenseq-1,lenseq,"*")
    # print("Length of zigzag seq: ", res)
    # print(tabulate(dic,headers=["#"] + sequence, showindex=["#"]+sequence))
    # print()
    #tree.render(directory='doctest-output').replace('\\','/')