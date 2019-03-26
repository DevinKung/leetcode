class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicts = {}
        for k, v in enumerate(nums): #遍历list，包括index和对应的值 
            if target - v in dicts:
                return [dicts.get(target-v), k]
            dicts[v] = k #将list中的值作为index
利用了字典
