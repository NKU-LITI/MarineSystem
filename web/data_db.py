#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/27 19:32
# @Author : way
# @Site : 
# @Describe:

import pandas as pd
from sqlalchemy import create_engine
from data import SourceDataDemo

ENGINE_CONFIG = 'mysql+pymysql://root:123456@127.0.0.1:3306/fish?charset=utf8'


class SourceData(SourceDataDemo):

    def __init__(self):
        self.ENGINE = create_engine(ENGINE_CONFIG)

        
    @property
    def TotalCount(self): 
        sql = """
        SELECT COUNT(*) AS total_count FROM fish;
        """
        df = pd.read_sql(sql, self.ENGINE)
        #提取出数字
        total_count = df['total_count'].iloc[0]
        return total_count
    
    @property
    def GrowthCount(self): 
        sql = """
        SELECT COUNT(*) AS total_count FROM fish where Status="生长鱼";
        """
        df = pd.read_sql(sql, self.ENGINE)
        #提取出数字
        total_count = df['total_count'].iloc[0]
        return total_count

    @property
    def NoGrowthCount(self): 
        sql = """
        SELECT COUNT(*) AS total_count FROM fish where Status="鱼苗";
        """
        df = pd.read_sql(sql, self.ENGINE)
        #提取出数字
        total_count = df['total_count'].iloc[0]
        return total_count
    

    @property
    def FishSpecies(self): 
        sql = """
        SELECT COUNT(DISTINCT species) AS total_species_count
        FROM fish;
        """
        df = pd.read_sql(sql, self.ENGINE)
        #提取出数字
        total_count = df['total_species_count'].iloc[0]
        return total_count

    @property
    def pie(self): #鱼种数量占比饼图
        sql = """
        SELECT Species, COUNT(*) AS fish_count
        FROM fish
        GROUP BY Species
        ORDER BY LEFT(species, 1);
        """
        df = pd.read_sql(sql, self.ENGINE)
        client_data = [{'name': row[0].strip(), 'value': row[1]} for row in df.values]
        return client_data
    
    @property  #鱼数量变化折线图
    def line(self):
        '''
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
        '''
        
    @property
    def line_bream(self):
        sql1="""
        SELECT
        CASE
            WHEN Weight BETWEEN 200 AND 299 THEN '200-299'
            WHEN Weight BETWEEN 300 AND 399 THEN '300-399'
            WHEN Weight BETWEEN 400 AND 499 THEN '400-499'
            WHEN Weight BETWEEN 500 AND 599 THEN '500-599'
            WHEN Weight BETWEEN 600 AND 699 THEN '600-699'
            WHEN Weight BETWEEN 700 AND 799 THEN '700-799'
            WHEN Weight BETWEEN 800 AND 899 THEN '800-899'
            WHEN Weight BETWEEN 900 AND 999 THEN '900-999'
            ELSE '1000+'
        END AS WeightRange,
        COUNT(*) AS Count
        FROM fish
        WHERE Species = 'Bream'
        GROUP BY WeightRange
        ORDER BY MIN(Weight);
        """

        sql2="""
        SELECT
        CASE
            WHEN Length BETWEEN 30 AND 32 THEN '30-32'
            WHEN Length BETWEEN 32 AND 34 THEN '32-34'
            WHEN Length BETWEEN 34 AND 36 THEN '34-36'
            WHEN Length BETWEEN 36 AND 38 THEN '36-38'
            WHEN Length BETWEEN 38 AND 40 THEN '38-40'
            WHEN Length BETWEEN 40 AND 42 THEN '40-42'
            WHEN Length BETWEEN 42 AND 44 THEN '42-44'
            WHEN Length BETWEEN 44 AND 46 THEN '44-46'
            ELSE '46+'
        END AS LengthRange,
        COUNT(*) AS Count
        FROM fish
        WHERE Species = 'Bream'
        GROUP BY LengthRange
        ORDER BY MIN(Length);
        """

        df1 = pd.read_sql(sql1, self.ENGINE)
        df2 = pd.read_sql(sql2, self.ENGINE)

        data = {
            'attribute1': [row[0].strip() for row in df1.values ],
            'count1': [row[1] for row in df1.values],
            'attribute2': [row[0].strip() for row in df2.values ],
            'count2': [row[1] for row in df2.values]
        }
        return data
    

    @property
    def line_roach(self):
        sql1="""
        SELECT
        CASE
            WHEN Weight BETWEEN 0 AND 50 THEN '0-50'
        WHEN Weight BETWEEN 50 AND 100 THEN '50-100'
        WHEN Weight BETWEEN 100 AND 150 THEN '100-150'
        WHEN Weight BETWEEN 150 AND 200 THEN '150-200'
        WHEN Weight BETWEEN 200 AND 250 THEN '200-250'
        WHEN Weight BETWEEN 250 AND 300 THEN '250-300'
        WHEN Weight BETWEEN 300 AND 350 THEN '300-350'
        WHEN Weight BETWEEN 350 AND 400 THEN '350-400'
        ELSE '400+'
    END AS WeightRange,
    COUNT(*) AS Count
FROM fish
WHERE Species = 'Roach'
GROUP BY WeightRange
ORDER BY MIN(Weight);
        """

        sql2="""
        SELECT
    CASE
        WHEN Length BETWEEN 16 AND 20 THEN '16-20'
        WHEN Length BETWEEN 20 AND 24 THEN '20-24'
        WHEN Length BETWEEN 24 AND 28 THEN '24-28'
        WHEN Length BETWEEN 28 AND 30 THEN '28-30'
        WHEN Length BETWEEN 30 AND 32 THEN '30-32'
        WHEN Length BETWEEN 32 AND 34 THEN '32-34'
        WHEN Length BETWEEN 34 AND 36 THEN '34-36'
        ELSE '36+'
    END AS LengthRange,
    COUNT(*) AS Count
FROM fish
WHERE Species = 'Roach'
GROUP BY LengthRange
ORDER BY MIN(Length);
        """

        df1 = pd.read_sql(sql1, self.ENGINE)
        df2 = pd.read_sql(sql2, self.ENGINE)

        data = {
            'attribute1': [row[0].strip() for row in df1.values ],
            'count1': [row[1] for row in df1.values],
            'attribute2': [row[0].strip() for row in df2.values ],
            'count2': [row[1] for row in df2.values]
        }
        return data
    

    @property
    def line_whitefish(self):
        sql1="""
        SELECT
        CASE
            WHEN Weight BETWEEN 200 AND 299 THEN '200-299'
            WHEN Weight BETWEEN 300 AND 399 THEN '300-399'
            WHEN Weight BETWEEN 400 AND 499 THEN '400-499'
            WHEN Weight BETWEEN 500 AND 599 THEN '500-599'
            WHEN Weight BETWEEN 600 AND 699 THEN '600-699'
            WHEN Weight BETWEEN 700 AND 799 THEN '700-799'
            WHEN Weight BETWEEN 800 AND 899 THEN '800-899'
            WHEN Weight BETWEEN 900 AND 999 THEN '900-999'
            ELSE '1000+'
        END AS WeightRange,
        COUNT(*) AS Count
        FROM fish
        WHERE Species = 'Whitefish'
        GROUP BY WeightRange
        ORDER BY MIN(Weight);
        """

        sql2="""
        SELECT
        CASE
            WHEN Length BETWEEN 28 AND 30 THEN '28-30'
            WHEN Length BETWEEN 30 AND 32 THEN '30-32'
            WHEN Length BETWEEN 32 AND 34 THEN '32-34'
            WHEN Length BETWEEN 34 AND 36 THEN '34-36'
            WHEN Length BETWEEN 36 AND 38 THEN '36-38'
            WHEN Length BETWEEN 38 AND 40 THEN '38-40'
            WHEN Length BETWEEN 40 AND 42 THEN '40-42'
            WHEN Length BETWEEN 42 AND 44 THEN '42-44'
            ELSE '44+'
        END AS LengthRange,
        COUNT(*) AS Count
        FROM fish
        WHERE Species = 'Whitefish'
        GROUP BY LengthRange
        ORDER BY MIN(Length);
        """

        df1 = pd.read_sql(sql1, self.ENGINE)
        df2 = pd.read_sql(sql2, self.ENGINE)

        data = {
            'attribute1': [row[0].strip() for row in df1.values ],
            'count1': [row[1] for row in df1.values],
            'attribute2': [row[0].strip() for row in df2.values ],
            'count2': [row[1] for row in df2.values]
        }
        return data
    

    @property
    def line_Parkki(self):
        sql1="""
        SELECT
        CASE
            WHEN Weight BETWEEN 50 AND 100 THEN '50-100'
            WHEN Weight BETWEEN 100 AND 150 THEN '100-150'
            WHEN Weight BETWEEN 150 AND 200 THEN '150-200'
            WHEN Weight BETWEEN 200 AND 250 THEN '200-250'
            WHEN Weight BETWEEN 250 AND 300 THEN '250-300'
            ELSE '300+'
        END AS WeightRange,
        COUNT(*) AS Count
        FROM fish
        WHERE Species = 'Parkki'
        GROUP BY WeightRange
        ORDER BY MIN(Weight);
        """

        sql2="""
        SELECT
        CASE
            WHEN Length BETWEEN 16 AND 20 THEN '16-20'
            WHEN Length BETWEEN 20 AND 24 THEN '20-24'
            WHEN Length BETWEEN 24 AND 28 THEN '24-28'
            WHEN Length BETWEEN 28 AND 30 THEN '28-30'
            ELSE '30+'
        END AS LengthRange,
        COUNT(*) AS Count
        FROM fish
        WHERE Species = 'Parkki'
        GROUP BY LengthRange
        ORDER BY MIN(Length);
        """

        df1 = pd.read_sql(sql1, self.ENGINE)
        df2 = pd.read_sql(sql2, self.ENGINE)

        data = {
            'attribute1': [row[0].strip() for row in df1.values ],
            'count1': [row[1] for row in df1.values],
            'attribute2': [row[0].strip() for row in df2.values ],
            'count2': [row[1] for row in df2.values]
        }
        return data
    

    @property
    def line_Perch(self):
        sql1="""
        SELECT
        CASE
        WHEN Weight BETWEEN 0 AND 50 THEN '0-50'
        WHEN Weight BETWEEN 50 AND 100 THEN '50-100'
        WHEN Weight BETWEEN 100 AND 150 THEN '100-150'
        WHEN Weight BETWEEN 150 AND 200 THEN '150-200'
        WHEN Weight BETWEEN 200 AND 250 THEN '200-250'
        WHEN Weight BETWEEN 250 AND 300 THEN '250-300'
        ELSE '300+'
        END AS WeightRange,
        COUNT(*) AS Count
        FROM fish
        WHERE Species = 'Perch'
        GROUP BY WeightRange
        ORDER BY MIN(Weight);
        """

        sql2="""
        SELECT
        CASE
        WHEN Length BETWEEN 16 AND 20 THEN '16-20'
        WHEN Length BETWEEN 20 AND 24 THEN '20-24'
        WHEN Length BETWEEN 24 AND 28 THEN '24-28'
        WHEN Length BETWEEN 28 AND 30 THEN '28-30'
        WHEN Length BETWEEN 30 AND 34 THEN '30-34'
        WHEN Length BETWEEN 34 AND 38 THEN '34-38'
        WHEN Length BETWEEN 38 AND 42 THEN '38-42'
        WHEN Length BETWEEN 42 AND 46 THEN '42-46'
        ELSE '46+'
        END AS LengthRange,
        COUNT(*) AS Count
        FROM fish
        WHERE Species = 'Perch'
        GROUP BY LengthRange
        ORDER BY MIN(Length);
        """

        df1 = pd.read_sql(sql1, self.ENGINE)
        df2 = pd.read_sql(sql2, self.ENGINE)

        data = {
            'attribute1': [row[0].strip() for row in df1.values ],
            'count1': [row[1] for row in df1.values],
            'attribute2': [row[0].strip() for row in df2.values ],
            'count2': [row[1] for row in df2.values]
        }
        return data
    

    @property
    def line_Pike(self):
        sql1="""
        SELECT
        CASE
        WHEN Weight BETWEEN 0 AND 500 THEN '0-500'
        WHEN Weight BETWEEN 500 AND 1000 THEN '500-1000'
        WHEN Weight BETWEEN 1000 AND 1500 THEN '1000-1500'
        ELSE '1500+'
        END AS WeightRange,
        COUNT(*) AS Count
        FROM fish
        WHERE Species = 'Pike'
        GROUP BY WeightRange
        ORDER BY MIN(Weight);
        """

        sql2="""
        SELECT
        CASE
        WHEN Length BETWEEN 30 AND 50 THEN '30-50'
        WHEN Length BETWEEN 50 AND 60 THEN '50-60'
        WHEN Length BETWEEN 60 AND 70 THEN '60-70'
        ELSE '70+'
        END AS LengthRange,
        COUNT(*) AS Count
        FROM fish
        WHERE Species = 'Pike'
        GROUP BY LengthRange
        ORDER BY MIN(Length);
        """

        df1 = pd.read_sql(sql1, self.ENGINE)
        df2 = pd.read_sql(sql2, self.ENGINE)

        data = {
            'attribute1': [row[0].strip() for row in df1.values ],
            'count1': [row[1] for row in df1.values],
            'attribute2': [row[0].strip() for row in df2.values ],
            'count2': [row[1] for row in df2.values]
        }
        return data
    

    @property
    def line_Smelt(self):
        sql1="""
        SELECT
        CASE
        WHEN Weight BETWEEN 0 AND 10 THEN '0-10'
        WHEN Weight BETWEEN 10 AND 20 THEN '10-20'
        ELSE '20+'
        END AS WeightRange,
        COUNT(*) AS Count
        FROM fish
        WHERE Species = 'Smelt'
        GROUP BY WeightRange
        ORDER BY MIN(Weight);
        """

        sql2="""
        SELECT
        CASE
        WHEN Length BETWEEN 10 AND 15 THEN '10-15'
        WHEN Length BETWEEN 15 AND 20 THEN '15-20'
        ELSE '20+'
        END AS LengthRange,
        COUNT(*) AS Count
        FROM fish
        WHERE Species = 'Smelt'
        GROUP BY LengthRange
        ORDER BY MIN(Length);
        """

        df1 = pd.read_sql(sql1, self.ENGINE)
        df2 = pd.read_sql(sql2, self.ENGINE)

        data = {
            'attribute1': [row[0].strip() for row in df1.values ],
            'count1': [row[1] for row in df1.values],
            'attribute2': [row[0].strip() for row in df2.values ],
            'count2': [row[1] for row in df2.values]
        }
        return data
    

    @ property
    def line_height(self):
        sql="""
        SELECT
        CASE
        WHEN height BETWEEN 0 AND 5 THEN '0-5'
        WHEN height BETWEEN 5 AND 10 THEN '5-10'
        WHEN height BETWEEN 10 AND 15 THEN '10-15'
        WHEN height BETWEEN 15 AND 20 THEN '15-20'
        ELSE '20+'
        END AS WeightRange,
        COUNT(*) AS Count
        FROM fish
        GROUP BY WeightRange
        ORDER BY MIN(height);
        """

        df = pd.read_sql(sql, self.ENGINE)
        data = {
            'height': [row[0].strip() for row in df.values ],
            'count': [row[1] for row in df.values]
        }
        return data
    
    @ property
    def water_supply(self):
        sql = """
        SELECT *
        FROM water_supply
        WHERE 省份 != '北京';
        """
        df = pd.read_sql(sql, self.ENGINE)
        client_data = [{'省份': row[0].strip(), '流域': row[1].strip(), 
                        '断面': row[2].strip(), '水质类别': row[3] , 
                        '温度': row[4], 'PH':row[5] , 
                        '站点情况':row[6].strip() } for row in df.values]
        return client_data

    @ property
    def yield_data(self):
        sql = """
        SELECT `月份`, `产量`, `鱼排面积`, `同比增加`, `平均产量`
        FROM `yield`
        ORDER BY `月份` ASC;
        """
        df = pd.read_sql(sql, self.ENGINE)
        yield_data = {
            '产量': df['产量'].tolist(),
            '鱼排面积': df['鱼排面积'].tolist(),
            '同比增加': df['同比增加'].tolist(),
            '平均产量': df['平均产量'].tolist()
        }
        return yield_data
    

    @ property
    def all_yield(self):
        sql=""" SELECT * FROM `all_yield` WHERE `地区` = '全国'; """
        df = pd.read_sql(sql, self.ENGINE)
            # 初始化一个空的结果列表
        result = []
        
        # 将DataFrame中的每一行转换为{name: value}的形式，并加入到结果列表中
        for index, row in df.iterrows():
            data = {
                'name': '鱼类',
                'value': row['鱼类']
            }
            result.append(data)
            
            data = {
                'name': '甲壳类',
                'value': row['甲壳类']
            }
            result.append(data)
            
            data = {
                'name': '贝类',
                'value': row['贝类']
            }
            result.append(data)
            
            data = {
                'name': '藻类',
                'value': row['藻类']
            }
            result.append(data)
            
            data = {
                'name': '其它',
                'value': row['其它']
            }
            result.append(data)
        
        return result
