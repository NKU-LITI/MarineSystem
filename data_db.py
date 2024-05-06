#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/27 19:32
# @Author : way
# @Site : 
# @Describe:

import pandas as pd
from sqlalchemy import create_engine
from data import SourceDataDemo

ENGINE_CONFIG = 'mysql+pymysql://root:2002821@127.0.0.1:3306/marinesystem?charset=utf8'


class SourceData(SourceDataDemo):

    def __init__(self):
        self.ENGINE = create_engine(ENGINE_CONFIG)

    @property
    def pie(self): #鱼种数量占比饼图
        sql = """
        SELECT species, COUNT(*) AS fish_count
        FROM fish
        GROUP BY species
        ORDER BY LEFT(species, 1);
        """
        df = pd.read_sql(sql, self.ENGINE)
        client_data = [{'name': row[0].strip(), 'value': row[1]} for row in df.values]
        return client_data
    
    @property  #鱼数量变化折线图
    def line(self):
        sql = """
        SELECT DISTINCT 
        t1.entry_date,
        (SELECT COUNT(*) FROM fish t2 WHERE t2.entry_date <= t1.entry_date AND (t2.life_status != 'death' OR t2.life_status IS NULL)) AS cumulative_fish_count
        FROM fish t1
        ORDER BY t1.entry_date;
        """
        df = pd.read_sql(sql, self.ENGINE)
        data = {
            '数量': [row[0].strip() for row in df.values ],
            'legend': [row[1] for row in df.values]
        }
        return data
    
    @property  #鱼属性分布
    def line2(self):
        #这里过后再补
        sql = """
        
        """
        df = pd.read_sql(sql, self.ENGINE)
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