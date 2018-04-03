from __future__ import print_function
from data_loader import read_data
import math


header, training_data = read_data("DTree.csv")
totalEntropy = 0;

#def Class Node:
 #   def __init__(self,attribute)

#returns unique values for a col
def giveUnique(rows, col):
    return list(set(row[col] for row in rows))

#returns counts of class labels for each value of a column
def getCounts(rows, col):
    counts = {}
    for row in rows:
        if row[col] not in counts:
            counts[row[col]] = [0,0]
        if row[-1] == 'yes':
            counts[row[col]][0] += 1
        else:
            counts[row[col]][1] += 1
    return counts

def fullEntropy(rows):
    counts = {}
    labels = giveUnique(rows, -1)
    for label in labels:
        counts[label] = 0

    for row in rows:
        counts[row[-1]] += 1

    negfrac = float(counts['yes'])/len(rows)
    posfrac = float(counts['no'])/len(rows)
    entropy = (-1)*((posfrac * math.log(posfrac,2)) + (negfrac * math.log(negfrac,2)))
    return entropy

#used to find entropy of data
def entropy(rows, col):
    entr = 0.0;
    rcounts = getCounts(rows, col)
    for attr in rcounts:
        attrtotal = float(rcounts[attr][0]) + rcounts[attr][1]
        posfrac = float(rcounts[attr][0])/attrtotal
        negfrac = float(rcounts[attr][1])/attrtotal
        print("posfrac: ", posfrac)
        print("negfrac: ", negfrac)
        if(posfrac != 0 and negfrac != 0):
            entr += (attrtotal/len(rows)) * ((posfrac * math.log(posfrac,2)) + (negfrac * math.log(negfrac,2)))
    print("Entropy for ", header[col], entr)
    return entr


def getHighestInfoGain(rows):
    col = 0
    entropies = []
    info = []
    for attr in header:
        if(attr == header[-1]):
            break
        entropies.append(entropy(rows, col))
        info.append(totalEntropy + entropies[col])
        col += 1
    return (max(info), header[info.index(max(info))])

#def getPartition(rows, col):
 #   attrvalues = giveUnique(rows, col)
  #  partition = {}
   # for value in attrvalues:
    #    subset = []
     #   for row in rows:
      #      if row[col] == value:
       #         subset.append(row)
        #partition[value] = subset
    #return partition
totalEntropy = fullEntropy(training_data) 
print(totalEntropy)
gain, attribute = getHighestInfoGain(training_data)
print("Root attribute: ", attribute)
print("Gain: ",gain)
answer = []
answer.append(attribute)
#partitions = getPartition(training_data, header.index(attribute))
