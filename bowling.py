max_score = 10

def score(game):
    global max_score
    result = 0
    frame = 1
    last = 0
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += max_score - last 
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
    global max_score
    total_frames = 10
    if frame < total_frames and get_value(game[i]) == max_score:
        result += get_value(game[i+1])    
        if game[i].lower() == "x":
            if game[i+2] == '/':
                result += max_score - get_value(game[i+1])
            else:
                result += get_value(game[i+2])
    return result

def get_value(char): 
    global max_score
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9': # range
        return int(char)
    elif char.lower() == 'x' or char == '/':
        return max_score
    elif char == '-':
        return 0
    else:
        raise ValueError()
