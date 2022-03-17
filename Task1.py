n=int(input())
m=int(input())
def seq(n,m):
    yield 1
    for i in range(m-1, n*m, m-1):
        k = i % n + 1
        if k == 1: return
        yield k

way=list(seq(n,m))
way_int=int((''.join(map(str,way))))
print(way_int)