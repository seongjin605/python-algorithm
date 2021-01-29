from functools import reduce

# https://leetcode.com/problems/product-of-array-except-self/submissions/
def productExceptSelf():
    # nums = [1, 2, 3, 4]
    nums = [9, 0, -2]
    # has_zero = filter( lambda x: x == 0, nums )
    # if has_zero == None:

    result = []
    for index, value in enumerate( nums ):
        # 자신을 제외한 배열을 곱한다.
        filtered_nums = filter( lambda x: x != value, nums )
        reduced_num = reduce( lambda x, y: x * y, filtered_nums, 1 )
        result.append( reduced_num )
    return result


r = productExceptSelf()
print( r )
