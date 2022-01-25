
def visualisation(solution, grid_size):

    # Go trough every state/move in the archive
    for i in range(len(solution.states)):

        print(solution.moves_made[i])
        print('------------')

        for j in range(0, len(solution.states[i]), grid_size):
            for k in range(grid_size):
                print(solution.states[i][j + k], end = ' ')
            print()
        print('\n')

    print(f'It took {solution.count} steps.', end = '\n\n')