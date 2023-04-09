#include <gtest/gtest.h>
#include <unistd.h>

#include <chrono>
#include <functional>
#include <tuple>
#include <vector>

#include "solution.hpp"
#include "test_utils.hpp"

class SolutionFixture : public ::testing::Test {
 protected:
  Solution solution;
};

class SolutionExtraTests
    : public SolutionFixture,
      public ::testing::WithParamInterface<std::tuple<std::vector<int>, std::vector<std::optional<int>>, bool>> {};

TEST_P(SolutionExtraTests, CheckNotInTree) {
  std::vector<int> head = std::get<0>(GetParam());
  std::vector<std::optional<int>> root = std::get<1>(GetParam());
  bool expected = std::get<2>(GetParam());

  ListNode* linked_list_head = vector_to_linked_list(head);
  TreeNode* tree_root = vector_to_b_tree(root);

  ASSERT_EQ(expected, solution.isSubPath(linked_list_head, tree_root));
}

INSTANTIATE_TEST_SUITE_P(
    SolutionExtraTests, SolutionExtraTests,
    ::testing::Values(
        std::make_tuple(std::vector<int>{1, 4, 2, 21},
                        std::vector<std::optional<int>>{1, 4, 4, std::nullopt, 2, 2, std::nullopt, 1, std::nullopt, 6,
                                                        8, std::nullopt, std::nullopt, std::nullopt, std::nullopt, 1,
                                                        3},
                        false),
        std::make_tuple(std::vector<int>{1, 10}, std::vector<std::optional<int>>{1, std::nullopt, 1, 10, 1, 9}, true),
        std::make_tuple(std::vector<int>{2, 2, 1},
                        std::vector<std::optional<int>>{2, std::nullopt, 2, std::nullopt, 2, std::nullopt, 1}, true)));
