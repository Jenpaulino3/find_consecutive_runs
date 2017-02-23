array = [1,2,3,5,10,9,8,9,10,11,7]

def findConsecutiveRuns(array):
	matches = []
	for i in range(0, len(array)-2):
		if (array[i] + array[i+1] + array[i+2])/3.0 == array[i+1]:
			matches.append(i)
	return matches

print findConsecutiveRuns(array)