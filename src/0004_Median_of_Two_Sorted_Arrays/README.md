# [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)

### Dependencies

Package :
* **g++** (part of `gcc`) : any version supporting c++17 standard (tested with gcc-12.2.1)
* **gtest** : for testing (`make test`), the package is named `gtest` on Arch Linux and `libgtest-dev` on Debian/Ubuntu.


### Uage

- `make test` will build and run the tests.

### Problem description
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.\
The overall run time complexity should be `O(log (m+n))`.

#### Example 1:
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

#### Example 2:
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

### Constraints:
- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10⁶ <= nums1[i], nums2[i] <= 10⁶`
