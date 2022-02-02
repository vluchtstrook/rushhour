import pandas as pd

df = pd.read_csv('first_400000_win_states_9x9_4.csv')

# print(df)
# print(df['path'])

print(df['path'].count())