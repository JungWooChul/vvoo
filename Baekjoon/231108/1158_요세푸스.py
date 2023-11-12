import sys
input = sys.stdin.readline

N, K = map(int, input().split())

ppl = [str(i) for i in range(1,N+1)]

del_idx = 0
print('<', end="")
while len(ppl) > 0:
    del_idx = (del_idx + K - 1) % len(ppl)
    print(ppl.pop(del_idx), end = "")

    if len(ppl) != 0:
        print(',', end = " ")
print('>')
