numbers = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 10, 10, 1, 5, 2]
print(f'Original list of numbers:\n{numbers}\n')

# creating an empty dictionary
keyOccurrences = {}

for num in numbers:
    if num in keyOccurrences:
        keyOccurrences[num] += 1
    else:
        keyOccurrences[num] = 1

# Converting dictionary to list of dictionary
keyOccurrencesList = [{key: value} for key, value in keyOccurrences.items()]
print('Unsorted list of number with it\'s occurrence in the original list.')
print(f'The number as key and value as number of times it occurred in that list:\n{keyOccurrencesList}\n')

# sorting list of dict according to it's value from high to low using nested for loop
for i in range(len(keyOccurrencesList)):
    for j in range(i+1, len(keyOccurrencesList)):
        # retrieving value from dictionary
        # print(keyOccurrencesList[i].values()) # output: returns keys values as 'dict_values([2])'
        # print(list(keyOccurrencesList[i].values())) # output: returns key's value as a list with only one value as '[2]'
        # print(list(keyOccurrencesList[i].values())[0]) # output: accessing value at 0th index of that list which returns 2
        value_i = list(keyOccurrencesList[i].values())[0]
        value_j = list(keyOccurrencesList[j].values())[0]

        # swapping value using temporary variable
        if value_i < value_j:
            # suppose if keyOccurrencesList[i = 0] = 2 and keyOccurrencesList[j = 1] = 3
            # then it will spaw the dict at index 0 with 1 and 1 with 0
            temp = keyOccurrencesList[i]
            keyOccurrencesList[i] = keyOccurrencesList[j]
            keyOccurrencesList[j] = temp
print(f'Sorted list from key with high ot low occurrences:\n{keyOccurrencesList}')