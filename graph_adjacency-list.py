# implementation of an undirected graph using Adjacency Lists
class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort() # Python list.sort() sorts alphabetically if no params to sort otherwise.

class Graph:
	vertices = {}

	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			# comparing if this vertex is same as one in class Vertex
			self.vertices[vertex.name] = vertex
			return "I'm in add_vertex - previously no vertices"
		else:
			return "I didn't work 1 - already vertices"
	
	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			# my YouTube video shows a silly for loop here, but this is a much faster way to do it
			self.vertices[u].add_neighbor(v)
			self.vertices[v].add_neighbor(u)
			return "I'm in add_edge"
		else:
			return "I didn't work 2"

	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors))

g = Graph()
# print(str(len(g.vertices)))
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
	print(g.add_vertex(Vertex(chr(i))))

for i in range(ord('A'), ord('K')):
	print(g.add_vertex(Vertex(chr(i))))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	print(g.add_edge(edge[:1], edge[1:])) # Splitting each edge from everything up to first element.

g.print_graph()
