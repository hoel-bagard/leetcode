import pytest

from .merge_in_between_linked_lists import ListNode, Solution

solution = Solution()


def list_to_linked_list(in_list: list[float]) -> ListNode:
    """Converts a list to a linked list."""
    start_node = current_node = ListNode(in_list[0])
    for value in in_list[1:]:
        current_node.next = ListNode(value)
        current_node = current_node.next

    return start_node


def linked_list_to_list(linked_list: ListNode) -> list[float]:
    """Converts a linked list to a list."""
    out_list: list[float] = []
    current_node: ListNode | None = linked_list
    while current_node is not None:
        out_list.append(current_node.val)
        current_node = current_node.next
    return out_list


@pytest.mark.parametrize("list1, a, b, list2, solution_as_list",
                         [([0, 1, 2, 3, 4, 5], 3, 4, [1000000, 1000001, 1000002],
                           [0, 1, 2, 1000000, 1000001, 1000002, 5]),
                          ([0, 1, 2, 3, 4, 5, 6], 2, 5, [1000000, 1000001, 1000002, 1000003, 1000004],
                           [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6]),
                          ])
def test_base(list1: list[float], a: int, b: int, list2: list[float], solution_as_list: list[float]):
    linked_list1 = list_to_linked_list(list1)
    linked_list2 = list_to_linked_list(list2)
    result = solution.mergeInBetween(linked_list1, a, b, linked_list2)
    result_as_list = linked_list_to_list(result)
    assert result_as_list == solution_as_list


def test_a_equal_b():
    linked_list1 = list_to_linked_list([0, 1, 4, 5])
    linked_list2 = list_to_linked_list([101, 102, 103])
    a, b = 1, 1
    solution_as_list = [0, 101, 102, 103, 4, 5]
    result = solution.mergeInBetween(linked_list1, a, b, linked_list2)
    result_as_list = linked_list_to_list(result)
    assert result_as_list == solution_as_list


# 1 <= a In the problem description
# def test_a_equal_0():
#     linked_list1 = list_to_linked_list([0, 1, 2, 3])
#     linked_list2 = list_to_linked_list([100, 101])
#     a, b = 0, 1
#     solution_as_list = [100, 101, 2, 3]
#     result = solution.mergeInBetween(linked_list1, a, b, linked_list2)
#     result_as_list = linked_list_to_list(result)
#     assert result_as_list == solution_as_list


# b < list1.length - 1 In the problem description.
def test_b_too_big():
    linked_list1 = list_to_linked_list([0, 1, 2, 3])
    linked_list2 = list_to_linked_list([101, 102, 103])
    a, b = 1, 10
    solution_as_list = [0, 101, 102, 103]
    result = solution.mergeInBetween(linked_list1, a, b, linked_list2)
    result_as_list = linked_list_to_list(result)
    assert result_as_list == solution_as_list
