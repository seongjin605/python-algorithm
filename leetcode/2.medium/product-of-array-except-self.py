from functools import reduce


# https://leetcode.com/problems/product-of-array-except-self/submissions/
def productExceptSelf():
    nums = [1, 2, 3, 4]
    # nums = [9, 0, -2] => [0,-18,0]
    # nums = [0, 0]

    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range( 0, len( nums ) ):
        out.append( p )
        p = p * nums[i]

    print( "p:", p )
    print( "output:", out )
    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range( len( nums ) - 1, -1, -1 ):
        print( "i:", i )
        out[i] = out[i] * p
        p = p * nums[i]
    return out


r = productExceptSelf()
print( r )
