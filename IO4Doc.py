'''
文件IO 读取写入 python和C兼容
读文件
    打开文件对象：使用Python内置的open()函数，传入文件名和标示符
        一般文件 r
        二进制文件 rb
        指定编码格式 参数encoding 
        遇到编码不规范，会出现UnicodeDecodeError 可以增加参数 errors='ignore'忽略
    读取文件：read()方法可以一次读取文件的全部内容，返回一个str对象（存储到内存）
        小文件         read(size) 一次读取多大的文件，避免内存占用
        大文件         readlinereadline() 按行读取
        配置文件       readlines() 返回所有行组成的list
    关闭文件：close()方法关闭文件 
        （出现异常不能执行，需要try-catch-finally保证一定会关闭/使用with as 自动close）
写文件
    打开文件：同样使用open函数 标识符 w wb a
        同样用with as可以保证异常出现能自动关闭文件
    写入文件：write() 先会保存到内存，空闲时间才会写入磁盘
    关闭文件：close执行时，才能保证，所有数据都写入磁盘中
'''

'''
file-like object 指的是内存的字节流，网络流，自定义流等可以read的对象，不用从特定类继承（有read方法就行）
    StringIO就是在内存中创建的file-like Object，常用作临时缓冲
读取二进制文件 模式 rb
    
'''
#读文件  默认utf-8格式   文件不存在抛出一个IOError
f = open('/Users/michael/test.txt', 'r')
#读文件 二进制文件 如图片视频 返回十六进制表示的字符
f = open('/Users/michael/test.jpg', 'rb')
#读文件 指定编码格式 如GBK
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
#读文件 忽略不规范的编码格式错误
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

f.read()
f.close()
#try-catch-finally安全关闭文件
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
#with as 一行代码，可自动关闭文件
with open('/path/to/file', 'r') as f:
    print(f.read())
#按行读取list
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉

#写文件 打开文件
f = open('/Users/michael/test.txt', 'w')
#写文件 with as自动关闭文件方式打开文件
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')