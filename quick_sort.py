def quick_sort(arr):
    left = []
    right = []
    if len(arr) <= 1:
        return arr

    # データの状態に左右されないためにrandom.choice()を用いることもある。
    # ref = random.choice(arr)
    ref = arr[0]
    ref_count = 0

    for ele in arr:
        # if ele < ref:
        if comp(ele, ref) == 1:
            left.append(ele)
        # elif ele > ref:
        elif comp(ele, ref) == -1:
            right.append(ele)
        else:
            ref_count += 1
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [ref] * ref_count + right
