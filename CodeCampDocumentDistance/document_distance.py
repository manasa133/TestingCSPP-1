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
    print("common",common)
    return common


def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    # print(dict1)
    # print(dict2)
    dict1.lower()
    dict2.lower()
    words_1 = dict1.split(" ")
    words_2 = dict2.split(" ")
    Common_wrds = commonWords(words_1,words_2)

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
