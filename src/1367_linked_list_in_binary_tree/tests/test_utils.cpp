#include <unistd.h>

#include <chrono>
#include <memory>
#include <optional>
#include <queue>
#include <tuple>
#include <vector>

#include "solution.hpp"

std::shared_ptr<ListNode> vector_to_linked_list(std::vector<int>& arr) {
  std::shared_ptr<ListNode> head = nullptr;
  std::shared_ptr<ListNode> prev = nullptr;
  for (int elt : arr) {
    std::shared_ptr<ListNode> current = std::make_shared<ListNode>(elt);
    if (head == nullptr)
      head = current;
    else
      prev->next = current;
    prev = current;
  }
  return head;
}

std::shared_ptr<TreeNode> vector_to_b_tree(const std::vector<std::optional<int>>& vect) {
  if (vect.empty() || !vect[0].has_value()) {
    return nullptr;
  }

  std::shared_ptr<TreeNode> root = std::make_shared<TreeNode>(vect[0].value());
  std::queue<std::shared_ptr<TreeNode>> node_queue;
  node_queue.push(root);
  size_t i = 1;
  while (!node_queue.empty() && i < vect.size()) {
    std::shared_ptr<TreeNode> node = node_queue.front();
    node_queue.pop();

    if (vect[i].has_value()) {
      node->left = std::make_shared<TreeNode>(vect[i].value());
      node_queue.push(node->left);
    }
    i++;

    if (i < vect.size() && vect[i].has_value()) {
      node->right = std::make_shared<TreeNode>(vect[i].value());
      node_queue.push(node->right);
    }
    i++;
  }
  return root;
}
