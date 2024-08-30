def abstract(arr):
    arr = set(arr)
    return list(arr)


def merge(arr1, arr2):
    tmp = set(arr1 + arr2)
    return list(tmp)


def cross(arr1, arr2):
    arr1 = abstract(arr1)
    arr2 = abstract(arr2)

    answer = []

    for i in arr1:
        if i in set(arr2):
            answer.append(i)

    return answer


arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(abstract(arr1))
print(abstract(arr2))

print(merge(arr1, arr2))

print(cross(arr1, arr2))
