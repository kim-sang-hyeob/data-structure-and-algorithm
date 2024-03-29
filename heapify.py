def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1
    # 코드를 작성하세요 
    if left_child_index < tree_size : 
        if tree[index] > tree[left_child_index] and tree[index] > tree[right_child_index]:
            return 
        else:
            if tree[left_child_index] > tree[right_child_index]:
                swap(tree , index , left_child_index)
                heapify(tree , left_child_index , tree_size )

            else:
                swap(tree , index, right_child_index)
                heapify(tree , right_child_index , tree_size )
    else:
        return 


# 실행 코드
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
print(tree) 