from collections import deque

def search(graph, activity):
    search_queue = deque()
    search_queue += graph[activity]
    searched = [activity]
    while search_queue:
        activity = search_queue.popleft()
        if not activity in searched:
            search_queue += graph[activity]
            searched.append(activity)
    return searched


graph = {}
graph["wake up"] = ["exercise", "pack lunch", "brush teeth"]
graph["exercise"] = ["shower"]
graph["brush teeth"] = ["eat breakfast"]
graph["pack lunch"] = []
graph["eat breakfast"] = []
graph["pack lunch"] = ["wake up"]
graph["shower"] = ["get dressed"]
graph["get dressed"] = []

print(search(graph, "wake up"))