n, k = map(int, input().split())
def set_s(arg1, arg2):
    if arg2 > arg1:
        return 0
    if arg1 == 1 or arg2 == 0:
        return 1
    return set_s(arg1-1, arg2) + set_s(arg1-1, arg2-1)
print (set_s(n, k))