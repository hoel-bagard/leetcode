#include <gtest/gtest.h>
#include <unistd.h>

#include <chrono>
#include <tuple>
#include <vector>

#include "solution.hpp"
#include "test_utils.hpp"

TEST(MedianTest, ShouldFail1) {
  {
    std::vector<int> head = {1, 4, 2, 21};
    std::vector<std::optional<int>> root = {1, 4, 4, std::nullopt, 2, 2, std::nullopt, 1, std::nullopt, 6, 8, std::nullopt, std::nullopt, std::nullopt, std::nullopt, 1, 3};

    ListNode* linked_list_head = vector_to_linked_list(head);
    TreeNode* tree_root = vector_to_b_tree(root);

    Solution solution_object;
    EXPECT_FALSE(solution_object.isSubPath(linked_list_head, tree_root));
  }
}

TEST(MedianTest, ShouldFail2) {
  {
    std::vector<int> head = {1, 10};
    std::vector<std::optional<int>> root = {1, std::nullopt, 1, 10, 1, 9};

    ListNode* linked_list_head = vector_to_linked_list(head);
    TreeNode* tree_root = vector_to_b_tree(root);

    Solution solution_object;
    EXPECT_TRUE(solution_object.isSubPath(linked_list_head, tree_root));
  }
}

TEST(MedianTest, ShouldFail3) {
  {
    std::vector<int> head = {2, 2, 1};
    std::vector<std::optional<int>> root = {2, std::nullopt, 2, std::nullopt, 2, std::nullopt, 1};

    ListNode* linked_list_head = vector_to_linked_list(head);
    TreeNode* tree_root = vector_to_b_tree(root);

    Solution solution_object;
    EXPECT_TRUE(solution_object.isSubPath(linked_list_head, tree_root));
  }
}
