#shakil_13_1043div3_c.py (Hard Version)
import sys

def skl():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    p3 = [1]
    for i in range(1, 31):
        p3.append(p3[-1] * 3)

    def gtc(n):
        cnt = [0] * 31
        i = 0
        while n > 0:
            cnt[i] = n % 3
            n //= 3
            i += 1
        return cnt

    def cc(j, p3):
        if j == 0:
            return 3
        else:
            return (j + 9) * p3[j - 1]

    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        cnt = gtc(n)
        s = sum(cnt)

        if s > k:
            print(-1)
            continue
        p = n % 2
        upper = min(n, k)
        
        
        if upper < s:
            print(-1)
            continue
        if upper % 2 == p:
            m = upper
        else:
            m = upper - 1
        if m < s:
            print(-1)
            continue
        f = (m - s) // 2
        c_cnt = cnt[:]
        rf = f
        
        
        for x in range(30, 0, -1):
            if rf == 0:
                break
            sh = min(rf, c_cnt[x])
            c_cnt[x] -= sh
            c_cnt[x - 1] += 3 * sh
            rf -= sh

        c = 0
        for j in range(31):
            if c_cnt[j] > 0:
                c += c_cnt[j] * cc(j, p3)

        print(c)

if __name__ == "__main__":
   skl()