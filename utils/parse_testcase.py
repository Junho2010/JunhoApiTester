# coding:utf8
'''
功能，将yaml编写的测试用例文件转换为测试用例数组。其中：
1.变量替换  在每个用例开始时，将config中的变量全部替换；每个用例执行完成之后，将
2.函数替换  config中的函数，在开始时执行；test中的函数，在测试时执行；validators中的函数，在测试结束之后执行
3.
'''