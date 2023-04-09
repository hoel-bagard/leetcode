#pragma once

#include <chrono>
#include <optional>
#include <tuple>
#include <vector>

#include "solution.hpp"

ListNode* vector_to_linked_list(std::vector<int>& arr);
TreeNode* vector_to_b_tree(const std::vector<std::optional<int>>& vect);
