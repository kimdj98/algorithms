def binary_search(a, left, right, K):
    if right >= left:
        mid = (left + right) // 2 # since mid should be integer

        if a[mid] == K:
            return True

        elif a[mid] < K:
            return binary_search(a, mid+1, right, K)

        elif K < a[mid]:
            return binary_search(a, left, mid-1, K)

    else:
        return False

input_list = [10,20,25,35,45,55,60,75,85,90]
n = len(input_list)