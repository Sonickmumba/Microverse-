score = [10,5,20,20,4,5,2]

highest = score[0]
lowest = score[0]

for i in range(1, len(score) -1):
    if score[i] > highest:
        highest = score[i]
        if score[i] < lowest:
            lowest = score[i]

    elif score[i] < highest


print(highest)
print(lowest)