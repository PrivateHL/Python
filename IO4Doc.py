'''
�ļ�IO ��ȡд�� python��C����
���ļ�
    ���ļ�����ʹ��Python���õ�open()�����������ļ����ͱ�ʾ��
        һ���ļ� r
        �������ļ� rb
        ָ�������ʽ ����encoding 
        �������벻�淶�������UnicodeDecodeError �������Ӳ��� errors='ignore'����
    ��ȡ�ļ���read()��������һ�ζ�ȡ�ļ���ȫ�����ݣ�����һ��str���󣨴洢���ڴ棩
        С�ļ�         read(size) һ�ζ�ȡ�����ļ��������ڴ�ռ��
        ���ļ�         readlinereadline() ���ж�ȡ
        �����ļ�       readlines() ������������ɵ�list
    �ر��ļ���close()�����ر��ļ� 
        �������쳣����ִ�У���Ҫtry-catch-finally��֤һ����ر�/ʹ��with as �Զ�close��
д�ļ�
    ���ļ���ͬ��ʹ��open���� ��ʶ�� w wb a
        ͬ����with as���Ա�֤�쳣�������Զ��ر��ļ�
    д���ļ���write() �Ȼᱣ�浽�ڴ棬����ʱ��Ż�д�����
    �ر��ļ���closeִ��ʱ�����ܱ�֤���������ݶ�д�������
'''

'''
file-like object ָ�����ڴ���ֽ��������������Զ������ȿ���read�Ķ��󣬲��ô��ض���̳У���read�������У�
    StringIO�������ڴ��д�����file-like Object����������ʱ����
��ȡ�������ļ� ģʽ rb
    
'''
#���ļ�  Ĭ��utf-8��ʽ   �ļ��������׳�һ��IOError
f = open('/Users/michael/test.txt', 'r')
#���ļ� �������ļ� ��ͼƬ��Ƶ ����ʮ�����Ʊ�ʾ���ַ�
f = open('/Users/michael/test.jpg', 'rb')
#���ļ� ָ�������ʽ ��GBK
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
#���ļ� ���Բ��淶�ı����ʽ����
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

f.read()
f.close()
#try-catch-finally��ȫ�ر��ļ�
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
#with as һ�д��룬���Զ��ر��ļ�
with open('/path/to/file', 'r') as f:
    print(f.read())
#���ж�ȡlist
for line in f.readlines():
    print(line.strip()) # ��ĩβ��'\n'ɾ��

#д�ļ� ���ļ�
f = open('/Users/michael/test.txt', 'w')
#д�ļ� with as�Զ��ر��ļ���ʽ���ļ�
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')