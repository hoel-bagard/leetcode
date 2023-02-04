pub struct Solution {}

impl Solution {
    pub fn maximum_xor(nums: Vec<i32>) -> i32 {
        nums.into_iter().fold(0, |max, num| max | num)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case(vec![3, 2, 4, 6], 7)]
    #[case(vec![1, 2, 3, 9, 2], 11)]
    fn test_base(#[case] nums: Vec<i32>, #[case] expected: i32) {
        assert_eq!(Solution::maximum_xor(nums), expected);
    }
}
