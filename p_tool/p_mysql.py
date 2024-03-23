import mysql.connector



#返回数据库对象
def mysql_dec(fn):
    def wrapper(*args):
        db = mysql.connector.connect(
            host="10.10.2.101",
            port = "3306",
            user="root",
            password="zxhc789",
            database="uav_zxhc_province"
            )
        cursor = db.cursor()
        #这个必须也加上
        res = fn(cursor,*args)

        db.commit()
        #关闭连接
        db.close()
        cursor.close()
        #包装前也必须加上返回值
        return res
    return wrapper
          

'''
查询字典数据
'''
@mysql_dec
def get_dict_by_code(cursor,code):
    sql = "select * from zxhc_dict_biz zd where code  = %s and parent_id != 0"
    params = [code]

    cursor.execute(sql,params)
    res = cursor.fetchall()
    dic_res = {item[5]:item[4] for item in res}
    print(dic_res)
    return dic_res

@mysql_dec
def get_dic_val_by_code(cursor,code):
    sql = "select dict_value  from zxhc_dict_biz zd where code  = %s  and parent_id  != 0 "
    params = [code]
    cursor.execute(sql,params)
    res = cursor.fetchall()
    dic_val = {item[0] for item in res}
    print(dic_val)
    return dic_val


   
    

@mysql_dec
def insert_data_to_battery(cursor,values):
     # 定义批量插入的语句
    sql = '''
    INSERT INTO basis_equip_battery_info
    (dept_code,battery_sn_code,battery_model,battery_label,is_library,destination,
    battery_guid,create_time,create_dept,create_user)values(
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s
    )
    '''
    # 执行批量插入操作
    cursor.executemany(sql, values)
    # 打印插入结果
    print("{}条记录插入成功".format(cursor.rowcount))


@mysql_dec
def insert_data_to_mount(cursor,values):
    sql =  '''
        INSERT INTO uav_zxhc_province.basis_equip_mount_info
      ( dept_code,mount_sn_code, mount_model, mount_label, is_library, 
        destination, mount_guid, create_time,create_dept,  create_user)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    # 执行批量插入操作
    cursor.executemany(sql, values)
    # 打印插入结果
    print("{}条记录插入成功".format(cursor.rowcount))

@mysql_dec
def insert_data_to_dict(cursor,values):
    sql = '''
     INSERT INTO uav_zxhc_province.zxhc_dict_biz
    (dict_key,dict_value,id, tenant_id, parent_id, code,  sort, is_sealed)
    VALUES(%s, %s,  %s, %s, %s, %s, %s,%s)
   '''
    # 执行批量插入操作
    cursor.executemany(sql, values)
    # 打印插入结果
    print("{}条记录插入成功".format(cursor.rowcount))


if __name__ == '__main__':
    pass
    #get_dict_by_code('battery_model')
    get_dict_by_code('uav_model')
    
 

