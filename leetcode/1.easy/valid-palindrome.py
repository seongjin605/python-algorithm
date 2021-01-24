# 1차 sumit: https://leetcode.com/submissions/detail/445067496/
# 리스트에 넣고, 데칼코마니 방식의 인덱스 조회로 처리
# def isPalindrome() -> bool:
#     # s = "A man, a plan, a canal: Panama"
#     s = "race a car"
#     print("len:", len(s))
#     arr = []
#     for ch in s:
#         if ch.isalnum():
#             arr.append(ch.lower())
#
#     halfOfLen = int(len(arr) / 2)
#     for i in range(0, halfOfLen):
#         if arr[i] != arr[len(arr) - i - 1]:
#             return False
#     return True

# 리스트로 처리
# def isPalindrome() -> bool:
#     s = "A man, a plan, a canal: Panama"
#     strs = []
#     for ch in s:
#         if ch.isalnum():
#             strs.append(ch.lower())
#
#     while(len(strs) > 0):
#         if strs.pop(0) != strs.pop():
#             return False
#
#     return True
# import collections
# from typing import Deque
#
# # Deque로 구현
# # 리스트에서 pop(0)이 O(n)
# # Deque에서는 O(1)이기 때문에 각각 n번씩 반복하면 n^2, n이 되므로 성능차이가 큼.
# def isPalindrome() -> bool:
#     s = "A man, a plan, a canal: Panama"
#
#     strs: Deque = collections.deque()
#     for ch in s:
#         if ch.isalnum():
#             strs.append(ch.lower())
#
#     while(len(strs) > 1):
#         if(strs.popleft() != strs.pop()):
#             return False
#     return True
import re
# 문자열 슬라이싱 방식으로 처리
def isPalindrome() -> bool:
    s = "A man, a plan, a canal: Panama"
    s= s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1] # [::-1] 문자열 뒤집기

result = isPalindrome()
print("result:", result)
