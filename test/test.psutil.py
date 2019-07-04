#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import psutil

# data = psutil.test()
# print(data)
p = psutil.Process(10296)
mp = p.memory_percent()
print(mp)
print(p.memory_info())
