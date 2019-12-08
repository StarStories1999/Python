# implementation of an undirected graph using Adjacency Matrix, with weighted or unweighted links
class Node:
	def __init__(self, n):
		self.name = n

class Graph:
	nodes = {}
	links = []
	link_indices = {}
	
	def add_node(self, node):
		if isinstance(node, Node) and node.name not in self.nodes:
			self.nodes[node.name] = node
			for row in self.links:
				row.append(0)
			self.links.append([0] * (len(self.links)+1))
			self.link_indices[node.name] = len(self.link_indices)
			return True
		else:
			return False
	
	def add_link(self, u, v, weight=1):
		if u in self.nodes and v in self.nodes:
			self.links[self.link_indices[u]][self.link_indices[v]] = weight
			self.links[self.link_indices[v]][self.link_indices[u]] = weight
			return True
		else:
			return False
			
	def print_graph(self):
		for v, i in sorted(self.link_indices.items()):
			print(v + ' ', end='')
			for j in range(len(self.links)):
				print(self.links[i][j], end='')
			print(' ')    

g = Graph()
# print(str(len(g.nodes)))
a = Node('A')
g.add_node(a)
g.add_node(Node('B'))
for i in range(ord('A'), ord('K')):
	g.add_node(Node(chr(i)))

links = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for link in links:
	g.add_link(link[:1], link[1:])

g.print_graph()
