'''
单元测试
    import unittest模块
    测试类，从unittest.TestCase继承
    以test开头，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
'''

'''
断言的方式
    是否相等 assertEqual
    是否抛出指定异常 assertRaises
'''

'''
单元测试运行方法
    main函数中执行 if __name__ == '__main__':    unittest.main()
    通过参数-m unittest直接运行单元测试
'''

'''
setUp()和tearDown() 测试方法前后执行
'''

#被测试的类
#mydict.py
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

#测试类
#TestDict.py
import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')


