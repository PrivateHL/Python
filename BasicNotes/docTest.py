'''
文档测试（注释文档）
    import re模块
    在def定义的后一排用多行注释编写
'''


def abs(n):
    '''
    Function to get absolute value of number.
    
    Example:
    
    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)