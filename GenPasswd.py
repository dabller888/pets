#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   password01.py
@Time    :   2020/06/21 22:23:03
@Author  :   iceld 
@Version :   1.0
@Contact :   dabller888@163.com
@License :   (C)Copyright 2020-2022
@Desc    :   None
'''


# here put the import lib
#figlet -f slant GenPassword
import random
import time
import string

print('''
  / ____/__  ____  / __ \____ ____________      ______  _________/ /
 / / __/ _ \/ __ \/ /_/ / __ `/ ___/ ___/ | /| / / __ \/ ___/ __  / 
/ /_/ /  __/ / / / ____/ /_/ (__  |__  )| |/ |/ / /_/ / /  / /_/ /  
\____/\___/_/ /_/_/    \__,_/____/____/ |__/|__/\____/_/   \__,_/                                                                       
                                                                by iceld
''')

# print(string.ascii_letters)
# print(string.digits)
# print(string.printable)


def gen_pass(s, _len=8):
    generate_str = ''.join(random.sample(s, _len))
    print('{0} is len:{1}'.format(generate_str, len(generate_str)))


if __name__ == "__main__":
    gen_pass(string.printable, 16)
