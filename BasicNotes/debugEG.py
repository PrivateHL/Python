
'''
���Ե����ַ���
    print������ӡ
    assert����
    logging��־ ���Ƽ� �ռ�������
    pdb���Թ���
    IDE��������
'''

#print �򵥴ֱ�����Ҫ�ֶ�ɾ��
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')

main()

#assert���� ����ʧ�ܻ��׳�AssertionError
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

>>>python err.py
>>>python -O err.py #ʹ��-o�����رն��ԣ���ʱassert�൱��pass

#logging ��־���еȼ�Լ��debug��info��warning��error
import logging
logging.basicConfig(level=logging.INFO) #����logging�ȼ���û�����ûᱨZeroDivisionError

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

#pdb��python�ĵ��Թ��ߣ����в�����
# err.py  ����ִ��
s = '0'
n = int(s)
print(10 / n)
>>>python -m pdb err.py #-m������pdb�������ԣ���ʾ��һ��Ҫִ�еĴ���
>>>l #l����鿴����
>>>n #����ִ�д���
>>>p s #p�������鿴����
>>>q #�˳���ǰ�ĵ���

#�����������ֻ�ܵ������ԣ�pdb.set_trace()���öϵ㣬ֻ�ڿ��ܳ���ĵط�����
# err.py
import pdb

s = '0'
n = int(s)
pdb.set_trace() # ���е�������Զ���ͣ
print(10 / n)
>>>python err.py #���д��룬������Զ���pdb.set_trace()��ͣ������pdb���Ի���
>>>c #c�������ִ��

#IDE�Ƚϳ��õ���Visual Studio Code��PyCharm;eclipse����pydev���Ҳ���Ե���python����
