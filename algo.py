
def resolve(sud):
    look_up = find_empty_box(sud)  # check if any empty boxes remain

    if look_up == None:
        # the puzzle has been solved
        return True
    else:
        r, c = look_up

    # try inserting no.s and see if a solution exists
    for num in range(1, 10):
        # check if number is valid
        if is_correct_num(sud, num, (r, c)):
            sud[r][c] = num

            # backtrack and solve
            if resolve(sud):
                return True

            # reset last pos if unable to solve
            sud[r][c] = 0

    return False


def is_correct_num(sud, num, loc):
    # Check if no. does not exist in column
    for col in range(len(sud[0])):
        if sud[loc[0]][col] == num and loc[1] != col:
            return False

    # Check if no. does not exist in row
    for row in range(len(sud)):
        if sud[row][loc[1]] == num and loc[0] != row:
            return False

    # Check individual boxes i.e 1 of 9 cubes on the board
    box_pos_x = loc[1] // 3
    box_pos_y = loc[0] // 3

    for row in range(box_pos_y*3, box_pos_y*3 + 3):
        for col in range(box_pos_x * 3, box_pos_x*3 + 3):
            # Check if no. already exists
            if sud[row][col] == num and (row, col) != loc:
                return False

    return True


def find_empty_box(sud):
    for row in range(len(sud)):
        for col in range(len(sud[0])):  # length of each row
            if sud[row][col] == 0:
                return (row, col)  # this is for the row and column

    return None
