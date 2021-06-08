def gcd(a, b):
    while b != 0:
        d = a%b
        a, b = b, d
    return a


upper1, lower1 = map(int, input().split())
upper2, lower2 = map(int, input().split())

new_upper = lower2*upper1 + lower1*upper2
new_lower = lower1 * lower2

gcd_num = gcd(new_upper, new_lower)

new_upper //= gcd_num
new_lower //= gcd_num

print(new_upper, new_lower)