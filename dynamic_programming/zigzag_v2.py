
def zigzag(sequence):
    # if seq has one item return 1 even if
    # we couldn't apply a difference
    if(len(sequence) == 1):
        return 1
    
    # storage of differences 
    difs = [None for i in range(len(sequence)-1)]

    # compute differences
    for it in range(len(sequence)):
        difs[it-1] = sequence[it] - sequence[it-1]
    
    # achieve id in seq when 
    # difference is different from zero
    ii=0
    while(ii < len(difs) and difs[ii]==0):
        ii+=1
    
    # in case sequence all have equal values
    # all differences are zero return 1
    if(ii == len(difs)):
        return 1
    
    # get the current difference different from zero
    dif = difs[ii]

    # init leni in 2 items because of previous difference
    leni = 2

    # next difference compare with previous in sign
    for ite in range(ii+1, len(difs)):

        # in case are different sign (multiplication rule)
        if(difs[ite] * dif < 0):
            # change always first item the sign
            dif *= -1
            # increase counting
            leni+=1
    return leni

seqi = [374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 249, 22, 176, 279, 23, 22, 617, 462, 459, 244]
print(f"largest len: {zigzag(seqi)}")