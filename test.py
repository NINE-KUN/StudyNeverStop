# def lengthOfLongestSubstring(s: str) -> int:
#     if not s: return 0
#     left = 0
#     lookup = set()
#     n = len(s)
#     max_len = 0
#     cur_len = 0
#     for i in range(n):
#         cur_len += 1
#         while s[i] in lookup:
#             lookup.remove(s[left])
#             left += 1
#             cur_len -= 1
#         if cur_len > max_len:
#             max_len = cur_len
#         lookup.add(s[i])
#     return max_len
#
# print(lengthOfLongestSubstring('abcabcbb'))


# def longestCommonPrefix(strs):
#     res = ""
#     for tmp in zip(*strs):
#         tmp_set = set(tmp)
#         if len(tmp_set) == 1:
#             res += tmp[0]
#         else:
#             break
#     return res
# print(longestCommonPrefix(["flower","flow","flight"]))
#
# lst=["flower","flow","flight"]
# lst1=["flower1","flow1","flight1","flight1"]
# print(list(zip(lst)))
# print(list(zip(*lst)))
# print(list(zip(*lst,lst1)))

str = 'ABBA'
print(str[1:3],str[2:0:-1],str[0:2:-1])
# n = len(str)
# list = []
# for i in range(n-1):
#     for j in range(1,n):
#         if str[j] == str[i] and str[i+1:j] == str[j-1:i:-1]:
#             A=str[i + 1:j]
#             C=str[j - 1:i:-1]
#             list.append(len(str[i:j+1]))
# print(max(list))

