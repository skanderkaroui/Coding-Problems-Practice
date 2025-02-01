oldToNew = {}

def dfs(node):

    if node in oldToNew:
        return oldToNew[node]

    

    for neighbor in node.neighbors():
