'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math

def tokenize(s):
    # regex = re.compile('[^a-z]')
    words = s.lower().split(" ")
    words = [re.sub('[^a-z]',"",w.strip()) for w in words]
    return words

def vectorize(dictionry,words,index):
    stopwords = load_stopwords("stopwords.txt")
    for w in words:
        if w not in stopwords and len(w) > 0 :
            if w not in dictionry:
                dictionry[w]=[0,0]
            dictionry[w][index]+=1
    return dictionry


def compute_distance(dictionry):
    n=sum([v[0]*v[1] for v in dictionry.values()])

    d1 = math.sqrt(sum([v[0]**2 for v in dictionry.values()]))
    d2 = math.sqrt(sum([v[1]**2 for v in dictionry.values()]))
    return n/(d1*d2)



def similarity(d1, d2):
    '''
        Compute the document distance as given in the PDF

    '''
    dictionry = dict()
    dictionry = vectorize(dictionry, tokenize(d1),0)
    dictionry = vectorize(dictionry, tokenize(d2),1)
    return compute_distance(dictionry)


    



    pass

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
