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

#print("is g a graph?: "+str(isGraph(graph)))

#remove weights function removes weights from the adjacency list
def removeWeights(g):
    unweightedGraph = {}
    keys = list(g.keys())
    for key in keys:
        unweightedGraph[key] = []
        edges = g[key]
        for edge in edges:
            unweightedGraph[key].append(edge[0])
    print("unweightedGraph: "+str(unweightedGraph))
    return unweightedGraph

## listEdges function takes a graph g as input and returns the edges as a list tuples in the format (node1, node2, weight of edge), and filters out redundant nodes. Sorts by weight from low to high
def listEdges(g):
	edges = []
	for node in g:
		for key in g:
			for i in range(0, len(g[key])):
				if (g[key][i][0], key, g[key][i][1]) not in edges and (key, g[key][i][0], g[key][i][1]) not in edges:
					edges.append((key, g[key][i][0], g[key][i][1]))
	return sorted(edges, key=lambda x:x[2])

print(str(listEdges(graph)))
print("num edges equals "+str(len(listEdges(graph))))

#removes weight value from tuples returned by listEdges function
def unweightedEdges(l):
	unweightedEdges = []
	for edge in l:
		unweightedEdges.append((edge[0],edge[1]))
	print("Unweighted Edges: "+str(unweightedEdges))
	return unweightedEdges

#print(str(unweightedEdges(listEdges(graph))))
#print("num edges equals "+str(len(unweightedEdges(listEdges(graph)))))

#takes graph and returns boolean indicating presence of cycles
def hasCycles(g):
    keys = list(g.keys())
    print(str(keys))
    unweightedGraph=removeWeights(g)
    print(str(unweightedGraph))
    #initialize current node
    currentNode = keys[0]
    stack = [currentNode]
    print("initial stack: "+str(stack))
    while len(stack)>0:
        connectedNodes = unweightedGraph[currentNode]
        #if all nodes connected to the current node are already in the list, pop the current node from the stack
        if len(list(set(connectedNodes).intersection(stack))) == len(connectedNodes):
            print("stack: "+str(stack))
            print("popping from the stack")
            stack.pop()
            print("stack: "+str(stack))
        #if the current node is connected to 2 or more already-visited nodes, there is a cycle. Return True.
        elif (len(list(set(connectedNodes).intersection(stack)))) >= 2:
            print("cycle found between "+str(currentNode)+"and "+str(list(set(connectedNodes).intersection(stack))))
            return True
        #otherwise, go through connected nodes until you get to one not in the stack, and move on to that node
        else:
            for node in connectedNodes:
                if node not in stack:
                    print("current node is now "+str(node))
                    currentNode = node
                    print("stack: "+str(stack))
                    print("appending current node to stack")
                    stack.append(currentNode)
                    print("stack: "+str(stack))
    print("No cycles found")
    return False

hasCycles(graph)


#hasCycles(listEdges(graph))

# given 2 verticies x and y in adjacency tree g, determine if they are connected
def isConnected(x, y, g):
	for edge in g[x]:
		if edge[0] == y or edge[1] == y:
			print(str(x)+" is connected to "+str(y))
			return True
	print("Not connected")
	return False
#isConnected(1, 2, graph)

def kuslakMST(g):
	if not isGraph(g):
		print("Error: input is not a properly formatted graph")
		return False
	else:
		edges = listEdges(g)
		print("Edges: "+str(edges))
		if not hasCycles(edges):
			print("The graph does not have cycles, return entire graph")
			return g
		else:
			visitedNodes = []
			mstEdges = []
			for edge in edges:
				print("Currently looking at edge: "+str(edge))
				if edge[0] in visitedNodes and edge[1] in visitedNodes:
					print("both "+str(edge[0])+"and "+str(edge[1])+" are in visitedNodes. Therefore adding this edge would create a cycle. Pass over this edge")
					pass
				else:
					print("appending nodes to visitedNodes and edge to mstEdges")
					visitedNodes.append(edge[0])
					visitedNodes.append(edge[1])
					print("Visited Nodes: "+str(visitedNodes))
					mstEdges.append(edge)
					print("mstEdges: "+str(mstEdges))
			print("Final mst edges: "+str(mstEdges))
			return mstEdges

#kuslakMST(graph)