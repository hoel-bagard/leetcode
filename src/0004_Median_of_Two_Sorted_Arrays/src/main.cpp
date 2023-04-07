#include <filesystem>
#include <iostream>
#include <vector>

#include "median.hpp"

int main(int argc, char** argv) {
  std::vector<int> nums1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  std::vector<int> nums2 = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50};

  std::cout << "First array: ";
  for (int num : nums1) {
    std::cout << num << " ";
  }
  std::cout << std::endl;

  std::cout << "Second array: ";
  for (int num : nums2) {
    std::cout << num << " ";
  }
  std::cout << std::endl;

  Solution solution_object;

  auto median = solution_object.findMedianSortedArrays(nums1, nums2);
  std::cout << "Median of the two arrays: " << median;

  std::cout << std::endl << std::flush;

  return 0;
}
