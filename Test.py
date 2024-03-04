from image_nameProcessor import *


a1 = image_nameProcessor()
#开始绝对路径测试
print('>>> absolute path test <<<')
a1.process('E:/download/_python_test/Resource') # replace it with your directory path
#开始相对路径测试
print('>>> relative path test <<<')
a1.process('./Resource')