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
		#print('False: input error')
		return False
	else:
		charCount_s = getCharCount(s)
		charCount_t = getCharCount(t)
		if charCount_s == charCount_t:
			print('True: '+s+" is an anagram of "+t)
			return True
		return False

## QUESTION1: given 2 strings s and t, is some anagram of t a substring of s?
def question1(s, t):
	#check that s and t are strings, and s is longer than t
	if type(s) != str or type(t) != str or len(s) < len(t):
		print('False: Improperly formated input')
		return False
	else:
		#check if t contains letters not found in s
		for char in t:
			if char not in s:
				print('False: t contains letters not in s')
				return False
		#for each len(t) long substring of s, run anagram test
		for i in range(0, len(s)):
			if anagramTest(t, s[i:i+len(t)]):
				print("True: "+s[i:i+len(t)]+" is an anagram of "+t)
				return True
		print("False, no anagrams found")
		#if all anagram tests fail, return false
		return False

def testQ1():
	print("Q1 Test1: expected outcome True")
	question1("udacity", "ad")
	print("Q1 Test2: expected outcome False")
	question1("udacity", "aj")
	print("Q1 Test3: expected outcome False")
	question1("udacity", 2)
#s = s[ beginning : beginning + LENGTH]
testQ1()

def isPalindrome(s):
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
		print("lps is "+lps)
		return lps

def testQ2():
	print("Q2 test 1, should print 'lps is racecar'")
	question2("driver racecarsdsadasgfdhgfsdsadsfgfdgjhgkguliuseweadsdadfghf")
	print("Q2 test 2, should print 'lps is dad'")
	question2("dad173123")
	print("Q2 test 3, should print 'Error: non-string input'")
	question2(1)

testQ2()
## QUESTION 3: Find minimum spanning tree of a graph

### isGraph function takes in a dictionary and determines whether it fits the format of a graph adjacency list as defined in the udacity assignment. Should return true for the above test graph.
def isGraph(g):
	if type(g) != dict:
		#print("input is not dict")
		return False
	else:
		for key in graph:
			if type(key) is not int:
				return False
			if isinstance(type(g[key]), list):
				return False
			else:
				for i in range(0, len(g[key])):
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
# Solution inspired by (nothing copied from) GeneDer's solution on Github https://github.com/GeneDer/Technical-Interview/blob/master/Solutions.py
def question3(g):
	#check that the input is a properly formatted graph adjacency tree
	if not isGraph(g):
		print("The input graph is not properly formatted")
		return False
	#get node set
	nodes = g.keys()
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
	# loop through edges and store only those which do not create cycles with disjoin set/union find algorithm
	mst_edges = []
	x = 0
	nodes = list(nodes)
	for node in nodes:
		nodes[x] = set([node])
		x += 1
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
	return mst

def testQ3():
	for key in list(graph.keys()):
		for edge in question3(graph)[key]:
			if edge not in graphMST[key]:
				print("Q3 fail")
				return False
		else:
			print("Q3 pass")
			return True
testQ3()
#question3(graph)

############ Question 4 #####################
# Find least common ancestor (LCA) of two nodes in a binary search tree
# Solution inspired by (nothing copied from) GeneDer's solution on Github https://github.com/GeneDer/Technical-Interview/blob/master/Solutions.py
# Solution employs a tree data structure which is similar to that shown in the Udacity fsnd videos on trees, rather than the matrix format defined in the question.
# This solution was employed because this tree data structure is more elegant and easier to traverse than the matrix.
# Define node class which inherits class object. Every node in a tree has a value, a smaller left child, and a larger right child. Both children are initialized to type Node.
# A tree is created by defining a series of Node objects which are chained together
class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

# bst_search function searches if n is in the tree
def bst_search(r, n):
	current_node = r
	while current_node.left != None or current_node.right != None:
		# go left if current node is greater than n
		if current_node.value > n:
			if current_node.left != None:
				current_node = current_node.left
			else:
				return False
		# go right if current node is less than n
		elif current_node.value < n:
			# make sure right node exist
			if current_node.right != None:
				current_node = current_node.right
			else:
				return False
		# if current node is n, return True
		else:
			return True
	# if n is a leaf return true
	if current_node.value == n:
		return True
	else:
		return False

def question4(r, n1, n2):
	# make sure r is a node object
	if type(r) != Node:
		return "r not properly formatted"
	# make sure n1 and n2 are integers
	if type(n1) != int:
		return "n1 not int"
	if type(n2) != int:
		return "n2 not int"
	# make sure n1 and n2 in the tree
	if not bst_search(r, n1):
		return "n1 not in tree"
	if not bst_search(r, n2):
		return "n2 not in tree"
	#Traverse tree starting at root
	current_node = r
	while current_node.left != None or current_node.right != None: 
		# if the current node is greater than both n1 and n2, go left
		if current_node.value > n1 and current_node.value > n2:
			current_node = current_node.left
		# if the current node is less than both n1 and n2, go left
		elif current_node.value < n1 and current_node.value < n2:
			current_node = current_node.right
		# If the current node is between n1 and n2, the current node is the lca
		else:
			#print(str(current_node.value))
			return current_node.value
	#print(str(current_node.value))
	return current_node.value

####Chain together node objects to construct a tree for test purposes

#root
r = Node(9)							#     			 9     
#row 1									 			/ \
n5 = Node(5)						#   		   /   \
n15 = Node(15)						#  			  5    15
r.left = n5							#			 / \   / \
r.right = n15						#			/	\ /	  \
#row 2								#		   3	7 10   16
n3 = Node(3)						
n7 = Node(7)
n10 = Node(10)
n16 = Node(16)
n5.left = n3
n5.right = n7
n15.left = n10
n15.right = n16

def test4():
	print("Q4 test1: r not Node type:", "Pass" if "r not properly formatted" == question4(747, 5, 15) else "Fail")
	print("Q4 test2: n1 not int", "Pass" if "n1 not int" == question4(r, "5", 15) else "Fail")
	print("Q4 test3: n2 not int", "Pass" if "n2 not int" == question4(r, 5, "15") else "Fail")
	print("Q4 test4: n1 not in the tree:", "Pass" if "n1 not in tree" == question4(r, 77, 5) else "Fail")
	print("Q4 test5: n1 = 3 and n2 = 15:", "Pass" if 9 == question4(r, 3, 15) else "Fail") 
	print("Q4 test6: n1 = 7 and n2 = 10", "Pass" if 9 == question4(r, 7, 10) else "Fail")
	print("Q4 test7: n1 = 10 and n2 = 16", "Pass" if 15 == question4(r, 10, 16) else "Fail")
	print("Q4 test8: n1 = 5 and n2 = 9", "Pass" if 9 == question4(r, 5, 9) else "Fail")

test4()

#####################Question 5######################
# Find element in a singly linked list which is m elements from the end.
class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

#### String together a linked list: ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

n1 = Node("one")
n2 = Node("two")
n3 = Node("three")
n4 = Node("four")
n5 = Node("five")
n6 = Node("six")
n7 = Node("seven")
n8 = Node("eight")
n9 = Node("nine")
n10 = Node("ten")

n1.next = n2
n2.next = n3
n3.next= n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10

def findLength(n):
	x = 1
	currentNode = n
	while currentNode.next != None:
		currentNode = currentNode.next
		x += 1
	return x

print(str(findLength(n1)))

def question5(n, m):
	if type(n) != Node:
		return "n is not a node object"
	if type(m) != int:
		return "m is not int"
	lengthList = findLength(n)
	currentNode = n
	x = 0
	while x < lengthList - m - 1:		
		currentNode = currentNode.next
		x += 1
	return currentNode.value

def testQ5():
	print("expected outcome: 'four'")
	print(str(question5(n1, 6)))
	print("expected outcome: 'ten'")
	print(str(question5(n1, 0)))
	print("expected outcome: 'n is not a node object'")
	print(str(question5(1, 1)))
	print("expected outcome: 'm is not int'")
	print(str(question5(n1, "1")))

testQ5()