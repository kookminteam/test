def abstract(arr):
    return list(set(arr))


def merge(arr1, arr2):
    return list(set(arr1 + arr2))


def cross(arr1, arr2):
    return list(set(arr1) & set(arr2))

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(abstract(arr1))
print(abstract(arr2))

print(merge(arr1, arr2))

print(cross(arr1, arr2))
