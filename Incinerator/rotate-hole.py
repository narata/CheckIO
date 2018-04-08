def rotate(state, pipe_numbers):
    pipe_numbers = set(pipe_numbers)
    state_num = 0
    state_list = []
    if judge_state(state, pipe_numbers):
        state_list.append(state_num)
    for i in range(1, len(state)):
        rotate_one(state)
        state_num += 1
        if judge_state(state, pipe_numbers):
            state_list.append(state_num)
    return state_list
    


def rotate_one(state):
    end = state[-1]
    for i in range(len(state)-1, 0, -1):
        state[i] = state[i-1]
    state[0] = end
    
    
def judge_state(state, pipe_numbers):
    for i in pipe_numbers:
        if state[i] != 1:
            return False
    return True


if __name__ == '__main__':
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"
