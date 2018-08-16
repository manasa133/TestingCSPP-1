'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
def four_of_a_kind(hand):
     return len(set(i for i,v in hand)) == 2

def three_of_a_kind(hand):
  return len(set(i for i,v in hand)) == 3

def two_pair(hand):
    return len(set(i for i,v in hand)) == 3

def one_pair(hand):
     return len(set(i for i,v in hand)) == 4





def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    # new_hand_digit=[]
    # new_hand_char=[]
    # for i in hand:
    # 	if(i[0].isdigit()):
    # 		new_hand_digit.append(int(i[0]))
    # 	else:
    # 		new_hand_char.append(i[0])
    # new_hand_char.sort()
    # new_hand_digit.sort()


    # print(new_hand_digit)
    # isDigit = True
    # for i in range(len(new_hand_digit)-1):
    # 	if(new_hand_digit[i+1] != new_hand_digit[i]+1):
    # 		isDigit = False
    # 		break
    # print(isDigit)


    # print(new_hand_char)
    # isChar = True
    # for i in range(len(new_hand_char)-1):
    # 	if(new_hand_char[i]>new_hand_char[i+1]):
    # 		isChar = False
    # 		break

    # if isDigit and isChar:
    # 	# print("true")
    # 	return True
    # else:
    # 	# print("False")
    # 	return False
    # 2,5,6,7,8
    #<testcases/input
    ###################################### sir code############
    if all([True if c in "A2345" else False for c,s in hand]):
    	return True
    card_values=set(['--23456789TJQKA'.index(c) for c,s in hand])
    return (len(card_values)==5 and max(card_values)-min(card_values)==4)



def  all_same(items):
	 return len( set( items ) ) == 1 

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    new_hand = []
    for i in hand:
    	new_hand.append(i[1])
    # print("newHAnd",new_hand)
    if all_same(new_hand):
    	# print("True")
    	return True
    return False

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    # print(four_of_a_kind(hand))
    if(is_straight(hand) and is_flush(hand)):
    	return 8
    elif(four_of_a_kind(hand)):
        return 7
    elif(three_of_a_kind(hand) and one_pair(hand)):
         return 6
    elif(is_flush(hand)):
    	return 5
    elif(is_straight(hand)):
    	return 4
    elif(three_of_a_kind(hand)):
        return 3
    elif(two_pair(hand)):
        return 2
    elif(one_pair(hand)):
        return 1
    else:
    	return 0

def poker(hands):

    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    temp=max(hands, key=hand_rank)
    print(temp)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = raw_input()
        ha = line.split(" ")
        HANDS.append(ha)
    # print("HANDS" ,HANDS)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
