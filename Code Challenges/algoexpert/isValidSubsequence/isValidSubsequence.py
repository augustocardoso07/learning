def isValidSubsequence(array, sequence):
    # Write your code here.
    i = 0
    for e in array:
        if i >= len(sequence):
            break 
        if e == sequence[i]:
            i += 1
			
    return i == len(sequence)
    