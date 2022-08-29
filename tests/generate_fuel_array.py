import random

def generateFuelArray():
    """
    Fuel array is RxC
    r and c
    """
    rows = random.randint(1,10)
    cols = random.randint(1,10)

    int_freq = .5

    fuel_array = []
    fuel_array += generateRow(cols, False, int_freq)
    terminal_prob = .7
    for row_i in range(1, rows):
        is_terminal = random.random() < terminal_prob
        row = generateRow(cols, is_terminal, int_freq)

def generateRow(row_len, is_terminal, int_freq):
    if is_terminal:
        return [0] * row_len
    for col_i in range(row_len):
        pass

def getTerminalRows(rows):
    terminal_rows = [1]
    for i in range(rows-1):
        terminal_rows += random.choice([0,1])
    return terminal_rows

def getInitialState(cols, terminal_rows):
    init_state = [0] * cols
    num_terminal_rows = sum(terminal_rows)

def isTerminalArray():
    #checks to see if path from start to terminal exists
    




'''
determine which rows are terminal
    row 0 is never terminal
    make sure row 0 connects to at least one terminal state

'''