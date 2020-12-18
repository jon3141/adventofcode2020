with open('day9.txt') as f:
    lines = [int(l) for l in f.read().split('\n')]

def check_num(index):
    if index < 25:
        return True
    relevant_numbers = sorted(lines[index-25:index])
    number_is_good = False
    for i in range(25):
        for j in range(24, i, -1):
            if relevant_numbers[i] + relevant_numbers[j] == lines[index]:
                number_is_good = True
            if number_is_good:
                break
        if number_is_good:
            break
    return number_is_good

invalid_num = 0

for i in range(len(lines)):
    if not check_num(i):
        invalid_num = lines[i]
        print(invalid_num)
        break

si = 0
ei = 1
found = False

while not found:
    current_sum = sum(lines[si:ei+1])
    if current_sum < invalid_num and ei != len(lines):
        ei += 1
    elif current_sum > invalid_num and si != ei - 1:
        si += 1
    else: #if current_sum == invalid_num:
        found = True
        break

print(min(lines[si:ei+1]) + max(lines[si:ei+1]))