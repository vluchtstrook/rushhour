

def visualisation(solution, grid_size):

    # Go trough every state/move in the archive
    for i in range(len(solution.path)):

        print('------------')

        j = 0
        while j < len(solution.path[i]):
            for k in range(grid_size):
                print(solution.path[i][j + k], end = ' ')
            print()
            j += grid_size
        print()

    print(f'The solutions path length is {len(solution.path)}.')
    print(f'It took creating {solution.count_states} states, of which {solution.count_unique_states} unique.', end = '\n\n')