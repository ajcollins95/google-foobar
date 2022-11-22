def solution(M, F):
    solution_data = {
        "M": int(M),
        "F": int(F),
        "generations_count": 0,
        "is_end_state": False,
    }

    while(True):
        if solution_data["M"] == 1 and solution_data["F"] == 1:
            return solution_data["generations_count"]
        solution_data = update_solution_data(solution_data)
        
def update_solution_data(data):
    """
    Updates the solution data object based on the newest iteration of the while loop
    """
    #Creates variables for which bomb type is greater than the other
    bomb_types = ["M", "F"] 
    max_bomb_type = "M" if data["M"] > data["F"] else "F"
    bomb_types.remove(max_bomb_type)
    min_bomb_type = bomb_types[0]

    #control block paramters
    max_count = data[max_bomb_type]
    min_count = data[min_bomb_type]

    #control block to address when max_bomb_type_count >> min_bomb_type_count
    if max_count > min_count * 2:
        max_over_min = (data[max_bomb_type] / data[min_bomb_type])
        data[max_bomb_type] = data[max_bomb_type] - data[min_bomb_type] * max_over_min
        data["generations_count"] += max_over_min
        pass
    elif max_count > min_count:
        #data[max_bomb_type] = data[max_bomb_type] - data[min_bomb_type]
        data[max_bomb_type] -= data[min_bomb_type]
        data["generations_count"] += 1
        pass
    else: 
        #only possible if something is in end state I think
        print "You done messed up A-A-Ron!"
    print data
    return data

solution("2", "9")
