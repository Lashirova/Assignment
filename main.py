 
myToDoList=[]
for i in range(3):
    list = input("Enter your chores: ")
    myToDoList.append(list)
print("There are my list:", myToDoList)


brandOfCars = ["Ford","Toyota","Tesla","Ferrari","Toyota","Mitsubishi","Honda","Hyundai","Tesla","Nissan","Ford"]
myListOfBrands=[]
for i in brandOfCars:
    if i not in myListOfBrands:
        myListOfBrands.append(i)
print(myListOfBrands)



NO_OF_CHARS = 256

def toList(string1): 
	temp = [] 
	for x in string1: 
		temp.append(x) 
	return temp 

# Utility function to convert from list to string 
def toString(List): 
	return ''.join(List) 

# Returns an array of size 256 containing count of characters 
# in the passed char array 
def getCharCountArray(string1): 
	count = [0] * NO_OF_CHARS 
	for i in string: 
		count[ord(i)] += 1
	return count 


def removeDirtyChars(string1, string2): 
    count = getCharCountArray(string2) 
    ip_ind = 0
    res_ind = 0
    temp = '' 
    str_list = toList(string1) 
  
    while ip_ind != len(str_list): 
        temp = str_list[ip_ind] 
        if count[ord(temp)] == 0: 
            str_list[res_ind] = str_list[ip_ind] 
            res_ind += 1
        ip_ind+=1
  
    return toString(str_list[0:res_ind]) 
  
string1='heyhowareyou'
string2='hurray'
print (removeDirtyChars("Output: " + string1, string2))


def printValues():
	l = list()
	for i in range(10,31):
		l.append(i**2)
	print(l)
		
printValues()
