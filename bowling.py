def score(game):
    result = 0
    frame = 1
    last = 0
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last 
        else:
            result += get_value(game[i])
        result = calculate_result(frame, game, i, result)
        last = get_value(game[i])
        if not in_first_half:
            frame += 1
        in_first_half = not in_first_half
        if game[i].lower() == "x":
            in_first_half = True
            frame += 1
    return result

def calculate_result(frame, game, i, result):
    if frame < 10 and get_value(game[i]) == 10:
        result += get_value(game[i+1])    
        if game[i].lower() == "x":
            if game[i+2] == '/':
                result += 10 - get_value(game[i+1])
            else:
                result += get_value(game[i+2])
    return result

def get_value(char): 
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9': # range
        return int(char)
    elif char.lower() == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
