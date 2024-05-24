"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
      left, right = 0, len(height)
      max_area = 0
      while left < right:
        if height[left] < height[right]:
          max_area = max(max_area,height[left] * (right - left))
          left += 1
        else:
          max_area = max(max_area,height[right] * (right - left))
          right -= 1
      return max_area
          
