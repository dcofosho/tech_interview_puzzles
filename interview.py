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
#question2("driver racecarsdsadasgfdhgfsdsadsfgfdgjhgkguliuseweadsdadfghf")


## QUESTION 3: Find minimum spanning tree of a graph

### isGraph function takes in a dictionary and determines whether it fits the format of a graph adjacency list as defined in the udacity assignment. Should return true for the above test graph.
def isGraph(g):
	if type(g) != dict:
		print("input is not dict")
		return False
	else:
		for key in graph:
			print("is type(key) not int?: "+str(type(key) is not int))
			if type(key) is not int:
				return False
			print("is type(g[key]) not array?: "+str(isinstance(type(g[key]), list)))
			if isinstance(type(g[key]), list):
				return False
			else:
				for i in range(0, len(g[key])):
					print("is type(g[key][i]) not tuple?: "+ str(type(g[key][i]) is not tuple))
					print(str(g[key][i]))
					if type(g[key][i]) is not tuple:
						return False
	return True

##a nice, reasonably complex graph to test with. Source http://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/
graph = {
    0:[(1,4),(7,8)],
    1:[(2,8),(0,4),(7,11)],
    2:[(1,8),(3,7),(5,4),(8,2)],
    3:[(2,7),(5,14),(4,9)],
    4:[(3,9),(5,10)],
    5:[(4,10),(3,14),(2,4),(6,2)],
    6:[(8,6),(5,2),(7,1)],
    7:[(6,1),(8,7),(1,11),(0,8)],
    8:[(7,7),(6,6),(2,2)]
}

graphMST = {
    0:[(1,4),(7,8)],
    1:[(0,4)],
    2:[(3,7),(5,4),(8,2)],
    3:[(2,7),(4,9)],
    4:[(3,9)],
    5:[(2,4),(6,2)],
    6:[(5,2),(7,1)],
    7:[(6,1),(0,8)],
    8:[(2,2)]
}

# Question3: Find minimum spanning tree for undirected weighted graph
def question3(g):
	#check that the input is a properly formatted graph adjacency tree
	if not isGraph(g):
		print("The input graph is not properly formatted")
		return False
	#get node set
	nodes = g.keys()
	print("Nodes: "+str(nodes))
	#get edge set
	edges = set()
	for x in nodes:
		for y in g[x]:
			if x > y[0]:
				edges.add((y[1], y[0], x))
			elif x < y[0]:
				edges.add((y[1], x, y[0]))
	# sort edges
	edges = sorted(list(edges))
	print("edges: "+str(edges))
	# loop through edges and store only those which do not create cycles with disjoin set/union find algorithm
	mst_edges = []
	x = 0
	nodes = list(nodes)
	for node in nodes:
		nodes[x] = set([node])
		print(str(nodes))
		x += 1
	print(str(nodes))
	for x in edges:
		# get indices of both nodes
		for y in range(0, len(nodes)):
			if x[1] in nodes[y]:
				x1 = y
			if x[2] in nodes[y]:
				x2 = y
		# Store union in the smaller index and pop the larger. Append edge to mst_edges
		if x1 < x2:
			nodes[x1] = set.union(nodes[x1], nodes[x2])
			nodes.pop(x2)
			mst_edges.append(x)
		if x1 > x2:
			nodes[x2] = set.union(nodes[x1], nodes[x2])
			nodes.pop(x1)
			mst_edges.append(x)
		# break loop when all nodes are in one graph
		if len(nodes) == 1:
			break
	#  put mst in proper format
	mst = {}
	for x in mst_edges:
		if x[1] in mst:
			mst[x[1]].append((x[2], x[0]))
		else:
			mst[x[1]] = [(x[2], x[0])]
		if x[2] in mst:
			mst[x[2]].append((x[1], x[0]))
		else:
			mst[x[2]] = [(x[1], x[0])]
	print(str(mst))
	return mst

question3(graph)