from .reverse_nodes import ListNode, reverse_k_group


def create_linked_list(values: list[int]) -> ListNode:
    head = node = ListNode()
    for i, val in enumerate(values):
        node.val = val
        if i < len(values)-1:
            new_node = ListNode()
            node.next_node = new_node
            node = new_node
        else:
            node.next_node = None
    return head


def linked_list_to_list(head: ListNode) -> list[int]:
    values: list[int] = []
    while True:
        values.append(head.val)
        if head.next_node is None:
            return values
        head = head.next_node


def test_base():
    values = [1, 2, 3, 4, 5]
    k = 2
    expected_res = [2, 1, 4, 3, 5]
    head = create_linked_list(values)
    assert expected_res == linked_list_to_list(reverse_k_group(head, k))


def test_not_multiple():
    values = [1, 2, 3, 4, 5]
    k = 3
    expected_res = [3, 2, 1, 4, 5]
    head = create_linked_list(values)
    assert expected_res == linked_list_to_list(reverse_k_group(head, k))
