# https://www.youtube.com/watch?v=gcYvFVZ_LUA&t=513s
'''Lower bound: either the element if it is present in the array or just greater element.
Upper bound: Just greater element, not the same element (strictly greater element)'''
def findNextUpper(target, arr):
    beg, end = 0, len(arr)-1
    while end-beg>1:
        mid = (beg + end)//2
        if arr[mid]<=target:
            beg = mid+1
        elif arr[mid]>target:
            end = mid
    
    if arr[beg]>target:
        return beg
    if arr[end]>target:
        return end