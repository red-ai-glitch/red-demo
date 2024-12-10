class Node:
    def __init__(self, index):
        self.index = index
        self.children = set()
visited = set()
topologically_sorted_graph = list()
def topologically_sort(root):
    if root not in visited:
        visited.add(root)
        for child in root.children: topologically_sort(root)
        topologically_sorted_graph.append(root)
