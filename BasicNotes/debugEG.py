
'''
调试的五种方法
    print方法打印
    assert断言
    logging日志 （推荐 终极武器）
    pdb调试工具
    IDE开发工具
'''

#print 简单粗暴，需要手动删除
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')

main()

#assert断言 断言失败会抛出AssertionError
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

>>>python err.py
>>>python -O err.py #使用-o参数关闭断言，此时assert相当于pass

#logging 日志，有等级约定debug，info，warning，error
import logging
logging.basicConfig(level=logging.INFO) #设置logging等级，没有设置会报ZeroDivisionError

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

#pdb是python的调试工具，多行不方便
# err.py  单步执行
s = '0'
n = int(s)
print(10 / n)
>>>python -m pdb err.py #-m启动，pdb单步调试，显示下一步要执行的代码
>>>l #l命令查看代码
>>>n #单步执行代码
>>>p s #p命令来查看变量
>>>q #退出当前的调试

#上面的例子是只能单步调试，pdb.set_trace()设置断点，只在可能出错的地方调试
# err.py
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
>>>python err.py #运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境
>>>c #c命令继续执行

#IDE比较常用的有Visual Studio Code和PyCharm;eclipse加上pydev插件也可以调试python程序
