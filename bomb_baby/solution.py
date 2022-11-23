def solution(M, F):
    """
    Determines if a final Mach/Facula bomb configuration is possible and how many generations it takes to get there.

    Write a function solution(M, F) where M and F are the number of Mach and Facula bombs needed. Return the 
    fewest number of generations (as a string) that need to pass before you'll have the exact number of bombs 
    necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M and F will be string
    representations of positive integers no larger than 10^50. This solution attempts to backtrack from the final 
    state, and if it ends up at (1, 1) then assumes that the final configuration is possible. Each backtrack is
    counted in the solution data dictionary. There are a few cases where the backtrack proves to be impossible,
    and this loop accounts for them.

    Args
    M - Number of Mach bombs in final state (string)
    F - Number of Facula bombs in final state (string)

    Returns
    Either the string 'impossible' if the final state cannot be reached, or the string number of generations it takes
    to reach the final state.
    """
    solution_data = {
        "M": int(M), #Number of Mach bombs
        "F": int(F), #Number of Facula bombs
        "generations_count": 0, 
    }

    while(True):
        if solution_data["M"] == 0 or solution_data["F"] == 0:
            #If the update ends up with none of a bomb type, the final configuration is impossible
            return "impossible"
        elif solution_data["M"] == solution_data["F"] and solution_data["M"] > 1:
            #If the update ever has the bomb types equal each other (after first gen), final configuration is impossible
            return "impossible"
        elif solution_data["M"] == 1 and solution_data["F"] == 1:
            #If the update gets us back to original start state, return number of generations!
            return str(solution_data["generations_count"])
        solution_data = update_solution_data(solution_data)
        
def update_solution_data(data):
    """
    Updates the solution data object based on the newest iteration of the while loop

    Updates the state of the data object. If the bomb type that has a greater number of bombs
    is much larger than the other bomb type, rapidly calculate how many generations it takes to even
    out the bomb types. If the bomb types are close enough in number, iterate backward 1 generation,
    based on whichever bomb type is greater.

    Args 
    data - a dictionary with a mach bomb count, facula bomb count, and generation count

    Returns
    Updated data dictionary
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
    if max_count > min_count * 2 and min_count > 1:
        max_over_min = (data[max_bomb_type] / data[min_bomb_type])
        data[max_bomb_type] -= data[min_bomb_type] * max_over_min
        data["generations_count"] += max_over_min
    elif max_count > min_count:
        #data[max_bomb_type] = data[max_bomb_type] - data[min_bomb_type]
        data[max_bomb_type] -= data[min_bomb_type]
        data["generations_count"] += 1
    return data

