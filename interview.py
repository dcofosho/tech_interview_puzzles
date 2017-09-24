def getCharCount(s):
	charCount_s = {}
	for char in s:
		if char not in charCount_s:
			charCount_s[char] = 1
		else:
			charCount_s[char] += 1
	return charCount_s

def anagramTest(s, t):
	if type(s) != str or type(t) != str or len(s) == 0 or len(s) != len(t):
		print('False: input error')
		return False
	else:
		charCount_s = getCharCount(s)
		charCount_t = getCharCount(t)
		if charCount_s == charCount_t:
			print('True: '+s+" is an anagram of "+t)
			return True
		print('False:'+s+" is not an anagram of "+t)
		return False
# print("Test1: Expected outcome True")
# anagramTest("made", "mead")

# print("Test2: different length strings. Expected outcome False1")
# anagramTest("mader", "mead")

# print("Test3: non-string input. Expected outcome False1")
# anagramTest(523, "made")

# print("Test4: non-anagram strings of equal length. Expected outcome False2")
# anagramTest("made", "male")


# print("palindromeTest1: expected outcome true")
# palindromeTest("racecar")

## QUESTION1: given 2 strings s and t, is some anagram of t a substring of s?
def question1(s, t):
	#check that s and t are strings, and s is longer than t
	if type(s) != str or type(t) != str or len(s) < len(t):
		print('False1')
		return False
	else:
		#check if t contains letters not found in s
		for char in t:
			if char not in s:
				print('t contains letters not in s')
				return False
		#if all above tests pass, get char counts for both strings
		# charCount_s = getCharCount(s)
		# charCount_t = getCharCount(t)
		#for each len(t) long substring of s, run anagram test
		for i in range(0, len(s)):
			if anagramTest(t, s[i:i+len(t)]):
				print("True: "+s[i:i+len(t)]+" is an anagram of "+t)
				return True
		print("False, no anagrams found")
		#if all anagram tests fail, return false
		return False

# print("Q1 Test1: expected outcome true")
# question1("udacity", "ad")
#s = s[ beginning : beginning + LENGTH]

def isPalindrome(s):
	if s[::-1] == s:
		print("True "+s+" is a palindrome")
	else:
		print("False "+s+" is not a palindrome")
	return s[::-1] == s




### QUESTION2: give a string s, what is the longest panindromic substring (lps) of s?
def question2(s):
	lps = ""
	#check if s is a string
	if type(s) != str:
		print("Error: non-string input")
		return "Error: non-string input"
	elif len(s)<2:
		print("True: input length is 1 or 0")
		return s
	else:
		length = len(s)
		substrings = []
		for x in range(0, length):
			for y in range(x, length):
				if isPalindrome(s[x:y + 1]) and len(s[x:y + 1]) > len(lps):
					lps = s[x:y + 1]
				# print("adding "+s[x:y + 1]+" to substring array")
				# substrings.append(s[x:y + 1])
		print("lps is "+lps)
		return lps

#test 1, should return and print "racecar"
question2("driver racecarsdsadasgfdhgfsdsadsfgfdgjhgkguliuseweadsdadfghf")


## QUESTION 3: Find minimum spanning tree of a graph
graph = {
	
}



		

