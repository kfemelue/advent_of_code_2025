import pandas as pd 

sequence = pd.read_csv('day1/sequence_document.csv')
moves = sequence['Sequence'].tolist()
current = int(50)
decoded = 0

for i in range(0, len(moves)):
    number_of_clicks = int(moves[i][1:])
    direction = moves[i][0]
    if direction == "L":
        if current - number_of_clicks  == 0:
            decoded += 1
            current = 0
        elif current - number_of_clicks  < 0:
            current = 99 + (current - number_of_clicks) - 1
    if direction == "R":
        if current + number_of_clicks  == 100:
            decoded += 1
            current = 0
        elif current + number_of_clicks  >  99:
            current = 0 + ( (current+number_of_clicks) - 100  )

print(decoded)
