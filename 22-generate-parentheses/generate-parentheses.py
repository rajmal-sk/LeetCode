class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # def isValid(p_string):
        #     left_count = 0
        #     for p in p_string:
        #         if p == "(":
        #             left_count += 1
        #         else:
        #             left_count -= 1

        #         if left_count < 0:
        #             return False

        #     return left_count == 0

        answer = []
        queue = collections.deque([("", 0, 0)])
        while queue:
            cur_string, leftCount, rightCount = queue.popleft()

            # If the length of cur_string is 2 * n, add it to `answer` if
            # it is valid.
            if len(cur_string) == 2 * n:
                answer.append(cur_string)
                continue
                
            if leftCount < n:
                queue.append((cur_string + "(", leftCount + 1, rightCount))
            if rightCount < leftCount:
                queue.append((cur_string + ")", leftCount, rightCount + 1))

        return answer