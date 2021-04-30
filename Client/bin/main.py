#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys

BASE_DIR = os.path.dirname(os.getcwd())
# print(BASE_DIR)
sys.path.append(BASE_DIR)

from core import handler

if __name__ == '__main__':
    handler.ArgvHandler(sys.argv)
    # handler.ArgvHandler('report_data')