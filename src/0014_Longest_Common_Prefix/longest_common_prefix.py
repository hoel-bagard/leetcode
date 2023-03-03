# import numpy as np
# import numpy.typing as npt

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:  # noqa: N802
        strs.sort(key=len)

        for i, letter_shortest_string in enumerate(strs[0]):
            for string in strs[1:]:
                if string[i] != letter_shortest_string:
                    return string[:i]
        return strs[0]

    # def longestCommonPrefixOneris(self, strs: list[str]) -> str:
    #     """Oneris's answer"""

    #     if len(strs) == 1:
    #         return strs[0]

    #     if (max_length := max([len(string) for string in strs])) == 0:
    #         return ""

    #     strs_array: npt.NDArray[np.str_] = np.asarray([[char for char in string] + (max_length - len(string)) * ["0"]
    #                                                    for string in strs])
    #     answer = ""
    #     index = 0
    #     while index < max_length and len(set(strs_array[:, index])) == 1:
    #         answer += strs_array[0, index]
    #         index += 1

    #     return answer
