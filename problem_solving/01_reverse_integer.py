
def reverse_the_number(num):
    reversed_num = 0
    if num < 0:
        sign = -1
    else:
        sign = 1
    while num > 0 or num < 0:
        print("num", num)
        num = abs(num)
        last_digit = num % 10
        reversed_num = reversed_num * 10 + last_digit
        num //= 10
    print("sign", sign)
    reversed_num *= sign
    return reversed_num


print(reverse_the_number(-12345))
print(reverse_the_number(-67897645))
