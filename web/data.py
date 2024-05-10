#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site : 
# @Describe:

from random import randint

class SourceDataDemo:


    #鱼种数量占比饼图
    @property 
    def pie(self):
        data = [
            {'value': 3, 'name': 'A'},
            {'value': 3, 'name': 'B'},
            {'value': 3, 'name': 'C'},
            {'value': 3, 'name': 'D'},
            {'value': 3, 'name': 'E'},
            {'value': 3, 'name': 'F'}
        ]
        return data


    #鱼种数量折线图
    @property
    def line(self):

        data2 = {
            '数量': [randint(1, 10) for i in range(10)],
            'legend': ['4/1', '4/2', '4/3', '4/4', '4/5', '4/6', '4/7','4/8', '4/9', '4/10',],
        }
        return data2


    #鱼属性分布折线图

    @property
    def line2(self):
        data3 = {
            'A':{
                'weight': {
                    'legend': [1.2, 2.5, 1.7, 3.8],
                    'count': [randint(1, 10) for i in range(4)]
                },
                'size': {
                    'legend': [1.2, 2.5, 1.7, 3.8],
                    'count':  [randint(1, 10) for i in range(4)]
                },
                'status': {
                    'legend': ['fry', 'growth'],
                    'count': [1,2]
                }
            },
            'B':{
                'weight': {
                    'legend': [1.2, 2.5, 1.7, 3.8],
                    'count':  [randint(1, 10) for i in range(4)]
                },
                'size': {
                    'legend': [1.2, 2.5, 1.7, 3.8],
                    'count': [randint(1, 10) for i in range(4)]
                },
                'status': {
                    'legend': ['fry', 'growth'],
                    'count': [1,2]
                }
            },
            'C':{
                'weight': {
                    'legend': [1.2, 2.5, 1.7, 3.8],
                    'count':  [randint(1, 10) for i in range(4)]
                },
                'size': {
                    'legend': [1.2, 2.5, 1.7, 3.8],
                    'count':  [randint(1, 10) for i in range(4)]
                },
                'status': {
                    'legend': ['fry', 'growth'],
                    'count': [1,2]
                }
            },
            'D':{
                'weight': {
                    'legend': [1.2, 2.5, 1.7, 3.8],
                    'count':  [randint(1, 10) for i in range(4)]
                },
                'size': {
                    'legend': [1.2, 2.5, 1.7, 3.8],
                    'count':  [randint(1, 10) for i in range(4)]
                },
                'status': {
                    'legend': ['fry', 'growth'],
                    'count': [1,2]
                }
            },
            'E':{
                'weight': {
                    'legend': [1.2, 2.5, 1.7, 3.8],
                    'count':  [randint(1, 10) for i in range(4)]
                },
                'size': {
                    'legend': [1.2, 2.5, 1.7, 3.8],
                    'count':  [randint(1, 10) for i in range(4)]
                },
                'status': {
                    'legend': ['fry', 'growth'],
                    'count': [1,2]
                }
            },
            'F':{
                'weight': {
                    'legend': [1.2, 2.5, 1.7, 3.8],
                    'count':  [randint(1, 10) for i in range(4)]
                },
                'size': {
                    'legend': [1.2, 2.5, 1.7, 3.8],
                    'count':  [randint(1, 10) for i in range(4)]
                },
                'status': {
                    'legend': ['fry', 'growth'],
                    'count': [1,2]
                }
            },
        }

        return data3
   


class SourceData(SourceDataDemo):
    ...