def calculate_tape_needed(n, first_row, second_row):
    tape_needed = 0
    for i in range(n):
        # Count tape needed for boundaries between adjacent tiles
        if first_row[i] != second_row[i]:
            tape_needed += 1

    # Count tape needed for boundaries with walls
    if first_row[0] != 0:
        tape_needed += 1
    if first_row[-1] != 0:
        tape_needed += 1

    return tape_needed

# Sample Input
n = int(input().strip())
first_row = list(map(int, input().strip().split()))
second_row = list(map(int, input().strip().split()))

tape_needed = calculate_tape_needed(n, first_row, second_row)
print(tape_needed)
