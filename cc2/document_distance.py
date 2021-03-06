import math
'''
    Document Distance - A detailed description is given in the PDF
'''

def wordFrequncy():
    pass

def commonWords(word1,word2):
    common=set()
    for each in word1:
        if each in word2:
            common.add(each)
    return common

def R_stop_words(commonwrds,stopwrds):
    newSet = commonwrds.copy()
    for i in stopwrds:
        if i in newSet:
            newSet.remove(i)
    return newSet



def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    # print(dict1)
    # print(dict2)
    dict1.lower()
    dict2.lower()
    # words_1 = dict1.split(" ")
    words_1 = [x.strip() for x in dict1.lower().split(' ')]
    words_2 = [x.strip() for x in dict2.lower().split(' ')]
    Common_wrds = commonWords(words_1,words_2)
    RemoveStopWords =  R_stop_words(Common_wrds,load_stopwords("stopwords.txt"))

    freqDictionary = {}

    for i in RemoveStopWords :
        freqDictionary[i] = []
        freqDictionary[i].append(words_1.count(i))
        freqDictionary[i].append(words_2.count(i))

    numerator = 0

    for k,v in freqDictionary.iteritems():
        numerator+= (v[0]*v[1])

    print("count",len(freqDictionary))

    den1 = math.sqrt(sum([v[0]**2 for k,v in freqDictionary.iteritems()]))
    den2 = math.sqrt(sum([v[1]**2 for k,v in freqDictionary.iteritems()]))
    # print(den1)
    # print(den2)


    if(den1 == 0.0 or den2 ==0.0):
        return 0.0

    res = numerator/(den1*den2)
    # print(res)
    return res


def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = raw_input()
    input2 = raw_input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
