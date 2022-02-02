
def visualisation(solution, grid_size):

    # Go trough every state/move in the archive
    # for i in range(len(solution.path)):

    #     print('------------')

    #     for j in range(0, len(solution.path[i]), grid_size):
    #         for k in range(grid_size):
    #             print(solution.path[i][j + k], end = ' ')
    #         print()
    #     print()

    print(f'The solutions path length is {len(solution.path)}.')
    print(f'{solution.count_states} states were created, of which {solution.count_unique_states} unique.', end='\n\n')