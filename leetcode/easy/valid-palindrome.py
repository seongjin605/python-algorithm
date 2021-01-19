# 1차 sumit: https://leetcode.com/submissions/detail/445067496/
def isPalindrome() -> bool:
    # s = "A man, a plan, a canal: Panama"
    s = "race a car"
    print("len:", len(s))
    arr = []
    for ch in s:
        if ch.isalnum():
            arr.append(ch.lower())

    halfOfLen = int(len(arr) / 2)
    for i in range(0, halfOfLen):
        if arr[i] != arr[len(arr) - i - 1]:
            return False
    return True


result = isPalindrome()
print("result:", result)
