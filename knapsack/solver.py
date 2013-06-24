#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def optimizer(items, capacity, values, weights):
    # maximize the item value without going over capacity
    sumValue = 0
    sumWeight = 0
    taken = {}

    valueMap = {values[i] : (weights[i], i) for i in range(items)}
    sortedValues = sorted(valueMap, reverse=True)

    for value in sortedValues:
        (weight, idx) = valueMap[value]

        if weight + sumWeight > capacity:
            continue

        sumWeight += weight
        sumValue += value
        taken[idx] = True

        #print sumWeight, sumValue, taken

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
    (value, weight, taken) = optimizer(items, capacity, values, weights)

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

