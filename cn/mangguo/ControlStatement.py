str1 = 'whfuwhuiwe'

if len(str1) == 10 :
    print('字符串长度为10')
else:
    print('字符串长度不为10，为{}'.format(len(str1)))
list1 = [0,0,0,0,0,0,0,0]
n = 0
for i in str1:
    try:
        print(i)
        list1[n] = i
        n = n + 1
    except:
        print('访问列表不存在的索引')

print(list1)


