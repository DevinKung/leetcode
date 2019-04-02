l 的左侧都是0，不含l 。 r 的右侧都是2, 不含 r
mid 代表着所有的1 (One)，在扫描的时候:
碰到0，交换到左边的l区间, 碰到2，交换到右边的r区间。扫描完后，中间部分就都是1 (One)

注意边界条件是mid <= r

class Solution:
    def sortColors(self, nums):
        l , r = 0, len(nums) - 1
        mid = 0
        
        while mid <= r:
            if nums[mid] == 0:
                nums[l], nums[mid] = nums[mid], nums[l]
                mid += 1 ; l += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[r] = nums[r], nums[mid]
                r -= 1
