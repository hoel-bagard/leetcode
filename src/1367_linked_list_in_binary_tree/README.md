# [1367. Linked List in Binary Tree](https://leetcode.com/problems/linked-list-in-binary-tree/)

### Dependencies

Package :
* **g++** (part of `gcc`) : any version supporting c++17 standard (tested with gcc-12.2.1)
* **gtest** : for testing (`make test`), the package is named `gtest` on Arch Linux and `libgtest-dev` on Debian/Ubuntu.


### Uage

- `make tests` will build and run the tests.

### Problem description
Given a binary tree `root` and a linked list with `head` as the first node.\
Return True if all the elements in the linked list starting from the `head` correspond to some *downward path* connected in the binary tree otherwise return False.\
In this context downward path means a path that starts at some node and goes downwards.

#### Example 1:
![Example 1 figure](./assets/example_1.png?raw=true)
```
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.
```

#### Example 2:
![Example 2 figure](./assets/example_2.png?raw=true)
```
Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
```

### Constraints:
- The number of nodes in the tree will be in the range `[1, 2500]`.
- The number of nodes in the list will be in the range `[1, 100]`.
- `1 <= Node.val <= 100` for each node in the linked list and binary tree.
