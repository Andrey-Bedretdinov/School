from itertools import combinations_with_replacement


def shot(balls: list, index: int, color: str):
    balls_buffer = balls
    balls_buffer.insert(index, color)
    return balls_buffer


def get_sequence(balls: list, min_len: int):
    k = 0
    start = 0
    sequences = []
    for i in range(len(balls) - 1):
        if k == 0:
            start = i
        if balls[i] == balls[i + 1]:
            if k == 0:
                k = 2
            else:
                k += 1
        else:
            stop = i
            if stop - start + 1 >= min_len:
                sequences.append([start, stop])
            k = 0
    return sequences


def del_sequence(balls: list, index_in: int, index_out: int):
    balls_buffer = balls
    for i in range(index_out - index_in + 1):
        balls_buffer.pop(index_in)
    return balls_buffer


def check_shots(balls: list):
    shots = get_sequence(balls, min_len=2)
    if not shots:
        shots = get_sequence(balls, min_len=1)
    return shots


def main(balls, colors):
    for i in range(len(balls) + 1):
        for color in colors:
            balls = shot(balls, i, color)


balls = input()
colors = list(set(balls))
for color in colors:
    while color*3 in balls:
        balls = balls.replace(color*3, color*2)

moves = []
for i in range(1, 11):
    print(list(combinations_with_replacement(colors, i)))
