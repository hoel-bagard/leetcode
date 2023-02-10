pub struct Solution {}

impl Solution {
    pub fn diagonal_sum(mat: Vec<Vec<i32>>) -> i32 {
        let mut sum = 0;
        let n = mat.len();
        for i in 0..n {
            sum += mat[i][i];
            sum += mat[i][n - 1 - i];
        }
        if n % 2 == 1 {
            sum -= mat[n / 2][n / 2]
        }
        sum
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case(vec![vec![1,2,3],
                vec![4,5,6],
                vec![7,8,9]], 25)]
    #[case(vec![vec![1,1,1,1],
                vec![1,1,1,1],
                vec![1,1,1,1],
                vec![1,1,1,1]], 8)]
    fn test_base(#[case] mat: Vec<Vec<i32>>, #[case] expected: i32) {
        assert_eq!(Solution::diagonal_sum(mat), expected);
    }
}
