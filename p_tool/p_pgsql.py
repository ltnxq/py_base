import psycopg2,uuid,time

#简单查询
def query(cur):
    sql = "select * from base.catalog_user_entity cue"
    cur.execute(sql)
    rows = cur.fetchall()
    print(rows)

def insert(conn,cur):

    uid = str(uuid.uuid4())
    suid = ''.join(uid.split('-'))
    nowstr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
    sql = """
     INSERT INTO base.consume_config (id, "source", description, energy_type, calculation, threshold, unit, organization_id, website_id,
       is_system_defined, created_at, updated_at, created_by, updated_by, data_category, statistics_cycle) VALUES
       (%s, '测试4来源_py', '回答哈哈', 'gas', 'lt', 365.3000, 'kw.h/t', '6477386486b443e99a2c8ac3d4b25049', 
     '8bf6042a2c2242a98dd07d838febfff5', false, %s, NULL, 'fef50c17852a4e0c9b79c4b684dee253', NULL, 'analog', NULL)   
    """.format(suid,nowstr)
    # print(suid)
    # print(nowstr)
    print(sql)
    try:
        cur.execute(sql,(suid,nowstr))
        conn.commit()
    except Exception as result:
        print('检测出异常{}'.format(result))
        conn.rollback()
    conn.close()

def update(conn,cur):
    #根基id修改数据
    id= '6a3ebf7c03054a4787a55b8f7c8f535e'

    sql = "update base.consume_config  set description  = '修改后的描述1222wwww11' where id = %s"
    try:
        #防止sql注入，注意后面是元组 只有一个元素的时候加上逗号
        cur.execute(sql,(id,))
        conn.commit()
    except Exception as result:
        print('检测出异常{}'.format(result))
        conn.rollback()
    finally:
        conn.close()


def dele(conn,cur):
    #根基主键ID删除数据
    id = '4d26c0ca9f0b4735820279c4d8fab4c6'
    sql = "DELETE FROM base.consume_config WHERE id='{}'".format(id)
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as result:
        print('检测出异常{}'.format(result))
        conn.rollback()
    finally:
        conn.close()



def batchUpdate(conn,cur,ids):
    sql4Value = 'select value from base.his_accumulator_statistics has  where id = %s'
    insertSqllist = []
    for id in ids:
        cur.execute(sql4Value,(id,))
        data = cur.fetchone()
        newvalue = data[0] * 3
        print(id,data[0],newvalue)
        insertSql = 'update base.his_accumulator_statistics  set carbon_emission_value = %f where id = %s'
        try:
            cur.execute(insertSql,(newvalue,id))
            conn.commit()
        except Exception as result:
            print('检测出异常{}'.format(result))
            conn.rollback()
        finally:
            conn.close()


    




if __name__ == "__main__":
    conn  = psycopg2.connect(database = "ssep",user = "postgres",password = "!Password1",host = "192.168.10.222",port = "5432")
    cur = conn.cursor()
    # insert(conn,cur)
    # dele(conn,cur)
    # update(conn,cur)