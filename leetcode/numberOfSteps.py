def numberOfSteps(num: int):
    steps = 0
    while(num!=0):
        # number is even
        if(num%2==0):
            num = int(num / 2)
        else:
            num -= 1
        steps+=1
    return steps



if __name__ == "__main__":
    print(numberOfSteps(123))