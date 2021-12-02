class Node:
    """이진 트리 노드 클래스"""
    def __init__(self, data):
            self.data = data
            self.left_child = None
            self.right_child = None


# root 노드 생성
root_node = Node("A")

# 코드를 쓰세요
c_node=Node('C')
f_node=Node('F')
root_node.right_child = c_node
c_node.right_child=f_node

b_node=Node('B')
e_node=Node('E')
g_node=Node('G')
h_node=Node('H')

root_node.left_child=b_node
b_node.right_child=e_node
e_node.left_child=g_node
e_node.right_child=h_node




# 실행 코드
test_node = root_node.right_child.right_child
print(test_node.data)

test_node = root_node.left_child.right_child.left_child
print(test_node.data)

test_node = root_node.left_child.right_child.right_child
print(test_node.data)