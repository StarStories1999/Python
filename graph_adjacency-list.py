# implementation of an undirected graph using Adjacency Lists
class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
	
	def add_neighbor(self, target_node):
		if target_node not in self.neighbors:
			self.neighbors.append(target_node)
			self.neighbors.sort()  # Python list.sort() sorts alphabetically if no params to sort otherwise.

class Graph:
	vertices = {}

	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			# comparing if this vertex is same as one in class Vertex
			self.vertices[vertex.name] = vertex
			return "I'm in add_vertex - previously no vertices"
		else:
			return "I didn't work 1 - already vertices"
	
	def add_edge(self, node, target_node):
		if node in self.vertices and target_node in self.vertices:
			# my YouTube video shows a silly for loop here, but this is a much faster way to do it
			self.vertices[node].add_neighbor(target_node)
			self.vertices[target_node].add_neighbor(node)
			return "I'm in add_edge"
		else:
			return "I didn't work 2"

	def print_graph(self):
		for key in (list(self.vertices.keys())):
			print(key + (str(self.vertices[key].neighbors)))

g = Graph()
# print(str(len(g.vertices)))
g.add_vertex(Vertex('A'))
g.add_vertex(Vertex('B'))

for i in range(ord('A'), ord('K')):
	print(g.add_vertex(Vertex(chr(i))))

# for i in range(ord('A'), ord('K')):
# 	print((g.add_vertex(Vertex(str(i)))))  # Already added so returns False.

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	mapping = g.add_edge(edge[:1], edge[1])
	# print(sorted(mapping,key=len))                      # Splitting each edge from everything up to first element.

g.print_graph()
