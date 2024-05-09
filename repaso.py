#Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

#Return the array in the form [x1,y1,x2,y2,...,xn,yn]
#ex: [2,4,5,3,2,1]
#re: [2,3,4,2,5,1]

test1=[2,4,5,3,2,1]
def test1():
    first_half=test1[:(len(test1)//2)]
    second_half=test1[len(test1)//2:]
    result=[]

    for i in range(len(test1)//2):
        result.append(first_half[i])
        result.append(second_half[i])
    print(first_half)
    print(second_half)
    print(result)



#------------------------------------------------------------------

#Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

#A string is represented by an array if the array elements concatenated in order forms the string

#Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
#Output: true
#Explanation:
#word1 represents string "ab" + "c" -> "abc"
#word2 represents string "a" + "bc" -> "abc"
#The strings are the same, so return true.
def test2():
        word1 = ["ab", "c"]
        word2 = ["a", "bc"]
        word1 = "".join(word1)
        word2 = "".join(word2)

        if word1 == word2: return True
        else: return False

#------------------------------------------------------------------

test2()



#You are given a string s and an integer array indices of the same length. 
#The string s will be shuffled such that the character at the ith position moves to indices[i] in ethe shuffled string.

#Input: s = "linencnotta", indices = [10,4,5,6,7,0,2,1,3,8,9]
#Output: "continental"  "linencnottl"
#Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

s = "linencnotta"
indices = [10,4,5,6,7,0,2,1,3,8,9]
result=[""]*len(s)
for index, letter in enumerate(s):
    #print(index)
    #print(letter)
    print("The index is "+str(index)+" for letter "+letter)

    result[indices[index]]=letter

print(result)



#You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

#Return the number of consistent strings in the array words.

 

#Example 1:

#Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
#Output: 2
#Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
def test3():

    result=0
    match=False
    for word in words:

        for letter in word:
            
            if letter not in allowed:
                match=False
                break
            else:
                match=True
                
        if match==True:
            result+=1
            match=False

    return result








#travels = [["GDL", "CDMX"],["CDMX","TOL"],["TOL", "MTY"],["MTY", "PUE"],["PUE", "SLP"]]

travels = [["CDMX","TOL"],["GDL", "CDMX"],["PUE", "SLP"],["MTY", "PUE"],["TOL", "MTY"]]
# resultado [GDL, CDMX, TOL, MTY, PUE, SLP]

#Method 1
def viajes_Avion(travels):
    first_element = False
    i=0

    while first_element == False:
        first_element=True

        current_salida=travels[i][0]

        for travel in travels:
            current_llegada = travel[1]
            if current_salida == current_llegada:
                first_element = False
        i+=1

    print(current_salida)



    result=[current_salida]

    last_travel = False

    while last_travel == False:
        last_travel=True

        for travel in travels:
            if current_salida == travel[0]:
                last_travel=False
                result.append(travel[1])
                current_salida=travel[1]

        i+=1

    print(result)


#------------------------------------------------------------------
