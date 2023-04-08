#include <gtest/gtest.h>
#include <unistd.h>

#include <chrono>
#include <tuple>
#include <vector>

#include "median.hpp"

TEST(MedianTest, Example1) {
  {
    std::vector<int> nums1 = {1, 3};
    std::vector<int> nums2 = {2};

    Solution solution_object;
    auto median = solution_object.findMedianSortedArrays(nums1, nums2);

    EXPECT_EQ(median, 2);
  }
}

TEST(MedianTest, Example2) {
  {
    std::vector<int> nums1 = {1, 2};
    std::vector<int> nums2 = {3, 4};

    Solution solution_object;
    auto median = solution_object.findMedianSortedArrays(nums1, nums2);

    EXPECT_EQ(median, 2.5);
  }
}
