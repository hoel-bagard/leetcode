#include <bits/stdc++.h>
using namespace std;

#include <algorithm>
#include <vector>

#include "median.hpp"

double Solution::findMedianSortedArrays(std::vector<int>& nums1, std::vector<int>& nums2) {
  // Swap to make nums1 the smaller of the two arrays.
  if (nums1.size() > nums2.size()) return Solution::findMedianSortedArrays(nums2, nums1);

  long unsigned int length_smaller = nums1.size();
  long unsigned int length_longer = nums2.size();

  long unsigned int start = 0;
  long unsigned int end = length_smaller;
  long unsigned int mid_in_merged_array = (length_smaller + length_longer + 1) / 2;

  while (start <= end) {
    // Compute the number of elements contributed to the left partition from each input array.
    long unsigned int mid = (start + end) / 2;
    long unsigned int left_nums1_size = mid;
    long unsigned int left_nums2_size = mid_in_merged_array - mid;

    // Check for indices overflow.
    int left_nums1 = (left_nums1_size > 0) ? nums1[left_nums1_size - 1] : INT_MIN;
    int left_nums2 = (left_nums2_size > 0) ? nums2[left_nums2_size - 1] : INT_MIN;
    int right_nums1 = (left_nums1_size < length_smaller) ? nums1[left_nums1_size] : INT_MAX;
    int right_nums2 = (left_nums2_size < length_longer) ? nums2[left_nums2_size] : INT_MAX;

    // If the partition is correct, then return, otherwise continue the binary search by updating start or end.
    if (left_nums1 <= right_nums2 and left_nums2 <= right_nums1) {
      if ((length_smaller + length_longer) % 2 == 0)
        return (max(left_nums1, left_nums2) + min(right_nums1, right_nums2)) / 2.0;
      return max(left_nums1, left_nums2);
    } else if (left_nums1 <= right_nums2) {
      start = mid + 1;
    } else
      end = mid - 1;
  }

  return 0.0;
}

// double Solution::findMedianSortedArrays(std::vector<int>& nums1,
//                                         std::vector<int>& nums2) {
//   // Merge the arrays and sort the merged array.
//   std::vector<int> v;
//   for (auto num : nums1) v.push_back(num);
//   for (auto num : nums2) v.push_back(num);
//   sort(v.begin(), v.end());

//   long unsigned int n = v.size();
//   return n % 2 ? v[n / 2] : (v[n / 2 - 1] + v[n / 2]) / 2.0;
// };
