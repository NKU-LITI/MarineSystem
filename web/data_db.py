#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/27 19:32
# @Author : way
# @Site : 
# @Describe:


'''
目前通过create_engine和pandas的方式连接数据库，只进行了SELECT操作
为便于编辑减少重复，管理员界面的增删改查使用SQLAlchemy方式
'''
import pandas as pd
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from data import SourceDataDemo


ENGINE_CONFIG = 'mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8'
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
    
    # -------------- 以下为'数据中心'界面获取数据操作 -----------------
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

    # -------------- '数据中心'界面 结束 -----------------

    # -------------- 以下为mainInfo -----------------
    @ property
    def water_quality(self):
        sql = """
        SELECT *
        FROM water_quality
        LIMIT 1;
        """
        df = pd.read_sql(sql, self.ENGINE)
        # print("water_quality：",df.values[0][0])
        client_data = {
            '水温': df.values[0][2],
            'PH': df.values[0][3],
            '溶解氧': df.values[0][4],
            '浊度': df.values[0][6],
            '总氮': df.values[0][10]
        }
        return client_data
    
    @ property
    def water_quality_history(self):
        # 历史12天的
        sql = """
        SELECT *
        FROM water_quality
        LIMIT 12;
        """
        df = pd.read_sql(sql, self.ENGINE)
        client_data = [{
            '水温': row[2],
            'PH': row[3],
            '溶解氧': row[4],
            '浊度': row[6],
            '总氮': row[10]
        } for row in df.values]
        print("history:",client_data)
        return client_data
    
    # -------------- 以下为管理员界面对'鱼类信息'的CRUD操作 -----------------
    @ property
    def all_fish(self):
        sql=""" SELECT * FROM `fish`; """
        df = pd.read_sql(sql, self.ENGINE)
        client_data = [{'id': row[0], 'Species': row[1], 'Weight': row[2], 
                        'Length': row[3], 'Height': row[4] , 
                        'Width': row[5], 'Status':row[6]} for row in df.values]
        return client_data
    
    
    @ property
    def get_fish_by_id(self, fish_id):
        sql = f"SELECT * FROM `fish` WHERE id = {fish_id};"
        df = pd.read_sql(sql, self.ENGINE)
        if df.empty:
            return None
        row = df.iloc[0]
        return {'id': row[0], 'Species': row[1].strip(), 'Weight': row[2], 
                'Length': row[3], 'Height': row[4], 
                'Width': row[5], 'Status': row[6].strip()}


    def update_fish(self, fish_id, species, weight, length, height, width, status):
        sql = text("""
        UPDATE fish SET 
            Species = :species, 
            Weight = :weight, 
            Length = :length, 
            Height = :height, 
            Width = :width, 
            Status = :status
        WHERE id = :fish_id;
        """)
        print(f"\n===={length}=====\n")
        with self.ENGINE.connect() as conn:
            conn.execute(sql, {
                'fish_id': fish_id,
                'species': species,
                'weight': weight,
                'length': length,
                'height': height,
                'width': width,
                'status': status
            })
            conn.commit() # 提交事务

    def insert_fish(self, species, weight, length, height, width, status):
        sql = text("""
        INSERT INTO `fish` (Species, Weight, Length, Height, Width, Status) VALUES (
            :species,
            :weight,
            :length,
            :height,
            :width,
            :status
        )
        """)
        print(f"\n===={length}=====\n")
        with self.ENGINE.connect() as conn:
            conn.execute(sql, {
                'species': species,
                'weight': weight,
                'length': length,
                'height': height,
                'width': width,
                'status': status
            })
            conn.commit()  # 提交事务

    def delete_fish(self, fish_id):
        sql = text("DELETE FROM `fish` WHERE id = :fish_id")
        with self.ENGINE.connect() as conn:
            conn.execute(sql, {'fish_id': fish_id})
            conn.commit()  # Commit the transaction after execution

    '''
    def search_fish(self, query,params):
        with self.ENGINE.connect() as conn:
            result = conn.execute(text(query), params).fetchall()
            #return [dict(row) for row in result]
            return  [dict(row._mapping) for row in result]
'''
        
    # -------------- '鱼类信息'的CRUD操作 结束 -----------------





    # -------------- 以下为管理员界面对'用户信息'的CRUD操作 -----------------

    @ property
    def get_user_by_id(self, user_id):
        sql = f"SELECT user_id, username, email, role, created_at FROM `user` WHERE id = {user_id};"
        df = pd.read_sql(sql, self.ENGINE)
        if df.empty:
            return None
        row = df.iloc[0]
        return {'user_id': row[0], 'username': row[1].strip(), 'email': row[2], 
                'role': row[3], 'created_at': row[4].strip()}


    @property
    def TotalUserCount(self): 
        sql = """
        SELECT COUNT(*) AS total_count FROM user;
        """
        df = pd.read_sql(sql, self.ENGINE)
        #提取出数字
        total_count = df['total_count'].iloc[0]
        return total_count
    
    @ property
    def all_users(self):
        sql=""" select user_id, username, email, role, created_at from user; """
        df = pd.read_sql(sql, self.ENGINE)
        client_data = [{'user_id': row[0], 'username': row[1], 
                        'email': row[2], 'role': row[3] , 
                        'created_at': row[4]} for row in df.values]
        return client_data




    def update_user(self, user_id, username, password, email, role):
        sql = text("""
        UPDATE user SET 
            username = :username, 
            password = :password, 
            email = :email, 
            role = :role
        WHERE user_id = :user_id;
        """)
        print(f"\n===={email}=====\n")
        with self.ENGINE.connect() as conn:
            conn.execute(sql, {
                'user_id': user_id,
                'username': username,
                'password': password,
                'email': email,
                'role': role
            })
            conn.commit() # 提交事务

    def insert_user(self, username, password, email, role):
        sql = text("""
        INSERT INTO `user` (username, password, email, role) VALUES (
            :username,
            :password,
            :email,
            :role
        )
        """)
        print(f"\n===={email}=====\n")
        with self.ENGINE.connect() as conn:
            conn.execute(sql, {
                'username': username,
                'password': password,
                'email': email,
                'role': role
            })
            conn.commit()  # 提交事务

    def delete_user(self, id):
        sql = text("DELETE FROM `user` WHERE user_id = :user_id")
        with self.ENGINE.connect() as conn:
            conn.execute(sql, {'user_id': id})
            conn.commit()  # Commit the transaction after execution        
    # -------------- '用户信息'的CRUD操作 结束 -----------------



    # -------------- '主要信息'的设备 -----------------
    @property
    def get_device(self):
        sql = """ 
        SELECT `设备ID`, `主控版本`, `主控温度`, `次控状态`, `警告状态`, `供氧系统`,
               `可见光摄像头`, `红外摄像头`, `可用空间`, `传输速率`, `屏幕亮度`, `音量`,
               `电源类型`, `剩余电量`
        FROM `device`;
        """
        try:
            df = pd.read_sql(sql, self.ENGINE)
            if not df.empty:
                row = df.iloc[0]
                device_data = {
                    '设备ID': row['设备ID'], 
                    '主控版本': row['主控版本'], 
                    '主控温度': row['主控温度'], 
                    '次控状态': row['次控状态'], 
                    '警告状态': row['警告状态'], 
                    '供氧系统': row['供氧系统'],
                    '可见光摄像头': row['可见光摄像头'],
                    '红外摄像头': row['红外摄像头'],
                    '可用空间': row['可用空间'],
                    '传输速率': row['传输速率'],
                    '屏幕亮度': row['屏幕亮度'],
                    '音量': row['音量'],
                    '电源类型': row['电源类型'],
                    '剩余电量': row['剩余电量']
                }
                return device_data
            else:
                return None
        except Exception as e:
            print(f"Error fetching device data: {str(e)}")
            return None



    # -------------- '主要信息'的设备 结束 -----------------