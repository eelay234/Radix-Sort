def counting_sort(A, r, k):
    t = []
    for i in range(0, k+1):
        t.append(0)
    for i in range(0, len(r)):
        t[r[i]] += 1
    for i in range(1, k+1):
        t[i] = t[i-1] + t[i]
    f = []
    for i in range(0, len(r)):
        f.append(0)
    for i in range(len(r)-1, -1, -1):
        if t[r[i]] != 0:
           f[t[r[i]]-1] = A[i]
	   t[r[i]] -= 1
    return f
        

def radix_sort(A, d):
    denom = 10
    n = 1
    r = []
    q = []
    for i in range(0, len(A)):
        r.append(0)
	q.append(A[i])
    for i in range(1, d+1):
        for j in range(0, len(A)):	    
            r[j] = (A[j] % denom) 
	    if i > 1:
	       r[j] = r[j] / n
            q[j] = A[j] / denom

        A = counting_sort(A, r, 9)
	denom = denom * 10
	n = n * 10
    return A 

a=[234, 12, 1999, 518]
b = radix_sort(a, 4)
print b
