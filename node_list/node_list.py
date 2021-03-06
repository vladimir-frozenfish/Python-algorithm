class Node:
    """класс односвязного списка"""
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next
    print("None")

if __name__ == '__main__':
    n3 = Node('third')
    n2 = Node('second', n3)
    n1 = Node('first', n2)
    print_linked_list(n1)

    n0 = Node('zero', n1)
    print_linked_list(n0)
