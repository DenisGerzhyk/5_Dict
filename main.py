# 1).

def mult_to_9(num: int) -> int:
    while num > 9:
        temp = 1
        while num > 0:
            num, remainder = divmod(num, 10)
            temp *= remainder
        num = temp
    return num


n = int(input("Enter a number: "))
print(mult_to_9(n))

# 2).

import string

print(string.ascii_letters)
start = input("Input start:")
end = input("Input end:")
counter1 = 0
counter2 = 0
for i in string.ascii_letters:
    if i == start:
        break
    counter1 += 1

for i in string.ascii_letters:
    if i == end:
        break
    counter2 += 1

print(string.ascii_letters[counter1:counter2 + 1])

x = input("input ")
s = string.ascii_letters
print(s[s.index(x[0]):s.index(x[2]) + 1])

# 3).

second = int(input("Input seconds:"))
days = second // 86400
hours = (second - (days * 86400)) // 3600
minutes = ((second - days * 86400) - (hours * 3600)) // 60
seconds = (second - (days * 86400 - hours * 3600 - minutes * 60)) // 3600

print("Days:", days, "d")
print("Hours:", hours, "h")
print("Minutes:", minutes, "m")
print("Seconds:", seconds, "s")
