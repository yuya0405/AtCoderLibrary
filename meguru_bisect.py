def is_ok(mid):
    return mid < N

def meguru_bisect(ng, ok):
    while(abs(ok-ng)>1):
        mid = (ok+ng)//2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return (ok)

print (meguru_bisect(101, 0))
