# 练习1
string1 = "hello world"
print(string1)

string2 = "Let's go"
print(string2)

string3 = '"The Zen of Python" -- by Tim Peters'
print(string3)

# 练习2
str1 = 'xyz'
str2 = 'abc'
str3 = str1 + str2
print(str3)

print('第二个数据：{er}, 第三个数据：{san}'.format(er = str1[1], san = str1[2]))

print(str2 * 10)

print('a' in str1)
print('a' in str2)

# 联系3
list1 = [1, 2, 3, 4, 5]
list1.append(100)

print(list1[1: 4])
list1.remove(3)
print(type(list1))
print(list1)
print(list1[-2])