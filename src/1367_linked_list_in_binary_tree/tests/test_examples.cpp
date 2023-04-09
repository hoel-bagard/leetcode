#include <gtest/gtest.h>
#include <unistd.h>

#include <chrono>
#include <tuple>
#include <vector>

#include "solution.hpp"
#include "test_utils.hpp"

class SolutionExampleTests : public ::testing::Test {
 protected:
  Solution solution;
};

TEST_F(SolutionExampleTests, Example1) {
  {
    std::vector<int> head = {1, 4, 2, 6};
    std::vector<std::optional<int>> root = {1, 4, 4, std::nullopt, 2, 2, std::nullopt, 1, std::nullopt, 6, 8, std::nullopt, std::nullopt, std::nullopt, std::nullopt, 1, 3};

    ListNode* linked_list_head = vector_to_linked_list(head);
    TreeNode* tree_root = vector_to_b_tree(root);

    EXPECT_TRUE(solution.isSubPath(linked_list_head, tree_root));
  }
}

TEST_F(SolutionExampleTests, Example2) {
  {
    std::vector<int> head = {1, 4, 2, 6};
    std::vector<std::optional<int>> root = {1, 4, 4, std::nullopt, 2, 2, std::nullopt, 1, std::nullopt, 6, 8, std::nullopt, std::nullopt, std::nullopt, std::nullopt, 1, 3};

    ListNode* linked_list_head = vector_to_linked_list(head);
    TreeNode* tree_root = vector_to_b_tree(root);

    EXPECT_TRUE(solution.isSubPath(linked_list_head, tree_root));
  }
}
