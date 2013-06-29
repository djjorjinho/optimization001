#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import collections

def knapsack(itemNum, capacity, values, weights):
    matrix = collections.defaultdict(dict)
    keeper = collections.defaultdict(dict)
    sumValue = 0
    sumWeight = 0
    taken = {}

    for w in range(capacity+1):
        matrix[0][w] = 0

    for i in range(1, itemNum+1):
        for j in range(1, capacity+1):

            leave = matrix[i-1].get(j, 0)
            keep = matrix[i-1].get(j-weights[i-1], 0) + values[i-1]

            if weights[i-1] <= j and keep > leave:
                keeper[i][j] = True
                matrix[i][j] = keep
            else:
                matrix[i][j] = leave
                keeper[i][j] = False

    maxWeight = capacity
    for i in reversed(range(1, itemNum+1)):
        if keeper[i].get(maxWeight, False) == True:
            taken[i-1] = True
            sumValue += values[i-1]
            sumWeight += weights[i-1]
            maxWeight -= weights[i-1]
        else:
            taken[i-1] = False

    return (sumValue, sumWeight, taken)

def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    items = int(firstLine[0])
    capacity = int(firstLine[1])

    values = []
    weights = []

    for i in range(1, items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    items = len(values)

    # the optimizer
    (value, weight, taken) = knapsack(items, capacity, values, weights)

    # prepare the solution in the specified output format
    outputData = str(value) + ' ' + str(0) + '\n'
    outputData += " ".join([("0", "1")[taken.get(i, False) == True] for i in range(items) ])

    return outputData

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

