

def visualisation(random_solution, grid_size):

    # Go trough every state/move in the archive
    for i in range(len(random_solution.states)):

        print(random_solution.moves_made[i])
        print('------------')

        j = 0
        while j < len(random_solution.states[i]):
            for k in range(grid_size):
                print(random_solution.states[i][j + k], end = ' ')
            print()
            j += grid_size
        print('\n')

    print(f'It took {random_solution.count} random steps.', end = '\n\n')