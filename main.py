from collections import deque
from subway_graph import *

def dfs(graph, start_node):
    """dfs 함수"""
    stack = deque()  # 빈 스택 생성

    # 모든 노드를 처음 보는 노드로 초기화
    for station_node in graph.values():
        station_node.visited = 0
    
    # 작성 
    start_node.visited = 1
    stack.append(start_node)

    while len(stack) != 0:

        subtract_node=stack.pop()
        subtract_node.visited = 2 
        for find_node in subtract_node.adjacent_stations :
            if find_node.visited == 0:
                find_node.visited = 1
                stack.append(find_node)



stations = create_station_graph("C:\\python_data\\data-structure-and-algorithm\\new_stations.txt")  # stations.txt 파일로 그래프를 만든다

gangnam_station = stations["강남"]

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
dfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)
