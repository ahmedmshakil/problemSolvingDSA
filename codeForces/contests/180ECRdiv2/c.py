#shakil_13_ECR_180_div2_c.py
  
import sys

def skl():
    data = sys.stdin.read().split()
    t = int(data[0])
    p = []
    idx = 1
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = list(map(int, data[idx:idx+n])); idx += n
        total = 0
        mx = a[-1]
        for k in range(2, n):  # a[0]..a[n-1]
            ak = a[k]
            if k < n-1:
                m = mx
            else:
                m = a[n-2]
            T = m if m > 2*ak else 2*ak
            t_val = T - ak
            cnt = 0
            l = 0
            r = k-1
            while l < r:
                if a[l] + a[r] > t_val:
                    cnt += (r - l)
                    r -= 1
                else:
                    l += 1
            total += cnt
        p.append(str(total))
    sys.stdout.write("\n".join(p))

if __name__ == '__main__':
    skl()
