try:
    i = 0
    j = 10 / i
    values = [1, '1']
    print(sum(values))
except TypeError:
    print("TypeError")
    j = 0
except ZeroDivisionError:
    print("ZeroDivisionError")
    j = 0
    print(j)
print("End")