
class RailRoad:

	def __init__(self):
		self.graph ={}

	def build(self,string_railroad):
		list_string_node = string_railroad.split(", ")
		for e in list_string_node:
			self.addroute(e)

	def addroute(self,edge):
		dep = edge[0]
		arr = edge[1]
		dist = int(edge[2:])

		my_road = {arr : dist}

		if dep in self.graph :
			self.graph[dep].update(my_road)
		else:
			self.graph.update({dep : my_road})

	def distance(self, path_str):
		path_list = path_str.split('-')

		# Si il n'y a qu'une ville !
		
		l = 0
		actual_town = path_list[0]
		next_town =path_list[1]
		i=2

		for i in range(len(path_list)-1):
			actual_town = path_list[i]
			next_town = path_list[i+1]

			if next_town not in self.graph[actual_town]:
				return 'NO SUCH ROUTE'
			else:
				l+= self.graph[actual_town][next_town]
		return l

	def possibles(self, dep, stops):
		dico_paths = {}
		self.search_paths( '', dep, 0, stops, dico_paths)
		return dico_paths


	def search_paths(self, path, town, length, stops, dico):
		if stops == -1: 
			pass
		else :
			new_path = path + town
			dico.update({new_path: length})

			for key,value in self.graph[town].items():
				self.search_paths(new_path, key, length + value, stops-1, dico)

