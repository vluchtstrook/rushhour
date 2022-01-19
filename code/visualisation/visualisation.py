

def visualisation(archive, moves_made, count, size):

    # Go trough every state/move in the archive
    for i in range(len(archive)):

        print(moves_made[i])
        print('------------')

        j = 0
        while j < len(archive[i]):
            for k in range(size):
                print(archive[i][j + k], end = ' ')
            print()
            j += size
        print('\n')

    print(f'It took {count} random steps.', end = '\n\n')