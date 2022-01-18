

def visualisation(archive, moves_made, count):

    # Go trough every state/move in the archive
    for i in range(len(archive)):

        print(moves_made[i])
        print('------------')

        j = 0
        while j < len(archive[i]):
            for k in range(6):
                print(archive[i][j + k], end = ' ')
            print()
            j += 6
        print('\n')

    print(f'It took {count} random steps.', end = '\n\n')