

# def create_dynamic_matrix(shape):
#     matrix = None
#     for dim_size in reversed(shape):
#         if matrix is None:
#             matrix = [None] * (dim_size+1)
#         else:
#             matrix = [matrix.copy() for _ in range(dim_size+1)]

#     return matrix

def sherlock_cost(idxs,dic):
    if not idxs:
        return
    result = dic
    # accesing to current difference
    for index in idxs[:-1]:
        result = result[index]
    
    # nuevo item
    # curr_dif = 0
    # for it in range(len(idxs)-1):
    #     curr_dif += abs(idxs[it+1] - idxs[it])
    #     print("curr:",curr_dif)
    
    result[idxs[-1]] = 999

    
    # compute the new ids
    # new_idxs = idxs.copy()
    # for it in range(new_idxs):
    #     new_idxs[it] = new_idxs[it] - 1
    #     sherlock_cost(new_idxs,dic)

def access_and_set_value(nested_list, indices, new_value):
    if not indices:
        return

    # Access the nested list using the indices
    current_list = nested_list
    for index in indices[:-1]:
        current_list = current_list[index]

    # Set the value at the specified location
    current_list[indices[-1]] = new_value



# if __name__ == '__main__':            
#     b = [1,1,2]
#     my_matrix = create_dynamic_matrix(b)
#     #print(my_matrix)
#     #sherlock_cost(b,my_matrix)
#     #print(my_matrix)

#     # Example usage
#     my_list = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
#     indices = [0, 1, 2]
#     new_value = 99

#     #access_and_set_value(my_list, indices, new_value)
#     sherlock_cost(indices,my_matrix)
#     # Print the modified list
#     print(my_matrix)

def create_dynamic_matrix(shape):
    if not shape:
        return None  # Handle an empty shape

    size = 1
    for dim_size in shape:
        size *= dim_size

    matrix = [None] * size

    return matrix

# Example usage
dimensions = [3, 4, 2]
my_matrix = create_dynamic_matrix(dimensions)
print(my_matrix)
        

