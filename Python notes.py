#Round a floating point number to nearest 0:
int(num)


# sort two arrays based on key of 2 array
combined = sorted(zip(arr1,arr2), key = lambda x: x[0])
                        # or
c1,c2 = zip(*sorted(zip(arr1,arr2), key = lambda x: x[0]))