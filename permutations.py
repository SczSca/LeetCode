from typing import List
class Solution:
    '''
        recursive function. Gets and stores all possible permutations of n characters
        O(n!)
        n: Ammount of characters in param nums
        :param nums: List of int. e.g. [1,2,3]
        :param left_pointer: int. tree height. Indicates when to stop the recursion
        :param result_container: List of Lists of int. variable in which all the permutations are stored

    '''
    def swap(self, nums: List[int], left_pointer: int , result_container: List[List[int]]):
            #base case that tells when to stop switching position of characters
            if left_pointer == len(nums) - 1:
                result_container.append(list(nums))

            else:
                for i in range(left_pointer, len(nums)):
                    #variable that helps to fix characters in a position so the next iterations are not affected
                    # e.g. nums = [1,2,3]. When all the permutations with the character 1 in position fixed 0 are done, the iterations that will be done for character 2 in position fixed 0 wont be affected
                    transversal = list(nums)

                    #swapping characters
                    temp = transversal[left_pointer]
                    transversal[left_pointer] = nums[i]
                    transversal[i] = temp

                    #recursive calling till base case is reached
                    self.swap(transversal, left_pointer + 1, result_container)

    #main func
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []

        self.swap(nums, 0, result)

        return result
    
    '''attempt before understanding problem'''
    # def swap(self, nums: List[int], left_pointer: int ):
    #     if left_pointer == len(nums) - 1:
    #         return nums
    #     else:
    #         for i in range(left_pointer, len(nums)):
    #             temp = nums[left_pointer]
    #             nums[left_pointer] = nums[i]
    #             nums[i] = temp
    #             self.swap(nums, left_pointer + 1)

    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     result: List[List[int]] = []
    #     traversal: List[int] = []
    #     for i in range(0, len(nums)):
    #         result.append(self.swap(nums, i))
    #     return result

data: List[int] = [1,2,3]
solution_manager = Solution()

result = solution_manager.permute(data)
print(result, len(result))