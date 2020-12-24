with open('day11.txt') as f:
    lines = f.read().split('\n')
def sp(s):
    return [char for char in s]
current_map = [sp(s) for s in lines]
