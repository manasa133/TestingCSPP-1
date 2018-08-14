# s="helloworld"
# list(s)
# lst =[]
# for i in s:
# 	lst.append(i)

# print("for loop", lst)
lst=["AD","2S", "7S", "4C" ,"5D"]

# lst1 = set(["--23456789TJQKA".index(i) for i,v in lst])


if all(True if i in "A2345" else False for i,v in lst ):
	print("True")
else:
	print("False")



# if(len(lst1)==5 and max(lst1)-min(lst1)==4))

# print("list comprehension ",lst1)