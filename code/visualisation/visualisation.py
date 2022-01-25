

def visualisation(solution, grid_size):

    # Go trough every state/move in the archive
    for i in range(len(solution.states)):

        print(solution.moves_made[i])
        print('------------')

        j = 0
        while j < len(solution.states[i]):
            for k in range(grid_size):
                print(solution.states[i][j + k], end = ' ')
            print()
            j += grid_size
        print('\n')

    print(f'It took {solution.count} steps.', end = '\n\n')