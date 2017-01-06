'''
Sau đây là thứ tự mà tôi đề nghị các bạn nên sử dụng

import random   # builtin libraries
from celery import task  # 3rd party libaries
from awesome.models import User  # current library package
from base import BaseService   # current same level package
'''

#Su dung module : truy xuat cac tai nguyen trong module su dung dau .
import Modun

print(Modun.__file__)
print(Modun.sum(2,15))

'''
function import : Function import cho phép bạn import một hoặc nhiều hàm trong modules, và chỉ được sử dụng các hàm mà nó đã được import.
'''
from Modun import sum

print(sum(1, 7))

import mypack.module1 as mod1
import mypack.module2 as mod2

print(mod1.subtract(7, 2))
print(mod2.sum(2, 5))