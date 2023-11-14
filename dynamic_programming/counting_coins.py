

def get_counting_coins(total_sum, coins):
    min_num_coins = [float("inf")] * total_sum
    
    # sum_0 has 0 coins
    min_num_coins[0] = 0

    # iterate on every sum
    for curr_sum in range(1,total_sum):
        # testing on every coin
        # check if difference between value_coin and current_sum (remain_sum)
        # add one coin(testing_coin) to num_of_coins of the remain sum
        # the number of coins of the remain sum should be less than other previous testing coins number
        
        for idx_coin in range(len(coins)):        
            if(coins[idx_coin] <= curr_sum and (min_num_coins[curr_sum - coins[idx_coin]] + 1 < min_num_coins[curr_sum])):
                min_num_coins[curr_sum] = min_num_coins[curr_sum - coins[idx_coin]] + 1
                
       
    return min_num_coins[total_sum-1]

if __name__ == "__main__":
    type_of_coins = [1,3,5]
    required_sum = 11
    min_coins_number = get_counting_coins(required_sum, type_of_coins)
    print(f"Minimum number of coins to get {required_sum} is {min_coins_number} coins between {type_of_coins}")
