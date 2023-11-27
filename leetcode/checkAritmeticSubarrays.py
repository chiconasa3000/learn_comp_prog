def rear(pdif,sub,min,cseq,dic,store):
    if(sub == 0 or min==len(cseq)):
        print(f"outlim en: {min},{sub}")

    if(dic[min] == 1 or dic[sub]==1):
        print(f"indice ya encontrada saltar:{min},{sub}")

    cdif = cseq[min] - cseq[sub]

    if(cdif == pdif):
        store.append()
        dic[min],dic[sub] = [1,1]
        rear(cdif,min,min-1,cseq,dic,store) 
        rear(cdif,min,min+1,cseq,dic,store)
    else:
        store = []
        print(f"dif no igual entre: {min},{sub},{cdif},{pdif}")



if __name__ == "__main__":
    sample_sarray = [5,9,3,7]
            



