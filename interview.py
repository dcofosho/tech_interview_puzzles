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
		print('False1')
		return False
	else:
		charCount_s = getCharCount(s)
		charCount_t = getCharCount(t)
		if charCount_s == charCount_t:
			print('True')
			return True
		print('False2')
		return False

# print("Test1: Expected outcome True")
# anagramTest("made", "mead")

# print("Test2: different length strings. Expected outcome False1")
# anagramTest("mader", "mead")

# print("Test3: non-string input. Expected outcome False1")
# anagramTest(523, "made")

# print("Test4: non-anagram strings of equal length. Expected outcome False2")
# anagramTest("made", "male")

def question1(s, t):
	if type(s) != str or type(t) != str or len(s) < len(t):
		print('False1')
		return False
	else:
		for char in t:
			if char not in s:
				print('t contains letters not in s')
				return False
		charCount_s = getCharCount(s)
		charCount_t = getCharCount(t)
		for i in range(0, len(s)):
			print(s[i:i+len(t)])
			if anagramTest(t, s[i:i+len(t)]):
				print("True: s[i]-s[i+len(t)-1] is an anagram of t")
				return True
		print("False, no anagrams found")
		return False

question1("udacity", "ad")

