import pandas as pd
from datetime import datetime
import uuid
import p_mysql 

def read_battery_excel_data():
    # 读取 Excel 文件
    excel_file = r"D:\zyz\file\zcxh\泰州全业务\台账模板\电池数据模版.xlsx" 

    sheet_name = "Sheet1"  # 工作表名

    # 使用 pandas 读取 Excel 文件
    df = pd.read_excel(excel_file, sheet_name=sheet_name,usecols="A:F")
    data_tuples = [list(x) for x in df.values]
    
    #获取电池型号的字典code
    b_mode_dict = p_mysql.get_dict_by_code(['battery_model'])

    # 生成一个 UUID
    current_time = datetime.now()

    for item in data_tuples:
        generated_uuid = uuid.uuid4()
        # 获取 UUID 的 hex 格式，去除其中的连字符
        uuid_hex = generated_uuid.hex
        item.append(uuid_hex)
        item.append(current_time)
        #创建部门
        item.append(1556984886703722497) 
        #创建人
        item.append(1123598821738675201)
        #是否在库转换
        if (item[4] == '是'):
            item[4] = 1
        else:
            item[4] = 0
        #单位转换
        item[0] = '100112102106'
        #电池型号转换
        item[2] = b_mode_dict[item[2]]
    
    return data_tuples

#导入电池模板数据
def import_batetery_data():
     battery_data = read_battery_excel_data()
     print(battery_data)
     p_mysql.insert_data_to_battery(battery_data)



def read_mount_excel():
    # 读取 Excel 文件
    excel_file = r"D:\zyz\file\zcxh\泰州全业务\台账模板\挂载设备数据模版.xlsx" 

    sheet_name = "Sheet1"  # 工作表名

    # 使用 pandas 读取 Excel 文件
    df = pd.read_excel(excel_file, sheet_name=sheet_name,usecols="A:F")
    data_tuples = [list(x) for x in df.values]
    
    #获取挂载类型字典code
    b_mode_dict = p_mysql.get_dict_by_code(['mount_model'])

    # 生成一个 UUID
    current_time = datetime.now()

    for item in data_tuples:
        generated_uuid = uuid.uuid4()
        # 获取 UUID 的 hex 格式，去除其中的连字符
        uuid_hex = generated_uuid.hex
        item.append(uuid_hex)
        item.append(current_time)
        #创建部门
        item.append(1556984886703722497) 
        #创建人
        item.append(1123598821738675201)
        #是否在库转换
        if (item[4] == '是'):
            item[4] = 1
        else:
            item[4] = 0
        #单位转换
        item[0] = '100112102106'
        #电池型号转换
        item[2] = b_mode_dict[item[2]]
    
    return data_tuples


def import_mount_data():
    mount_data = read_mount_excel()
    print(mount_data)
    p_mysql.insert_data_to_mount(mount_data)


def generate_diff_excel():
    excel_file = r"D:\zyz\file\zcxh\泰州全业务\台账模板\无人机类型字典_provide.xlsx" 

    sheet_name = "Sheet1"  # 工作表名

    # 使用 pandas 读取 Excel 文件
    df = pd.read_excel(excel_file, sheet_name=sheet_name,usecols="A")
    data_list = [x[0] for x in df.values]
    print(data_list)

    new_data_list = []
    dic_val_set = p_mysql.get_dic_val_by_code(['uav_model'])

    dic_code_val = p_mysql.get_dict_by_code(['uav_model'])

    for item in data_list:
        if item not in dic_val_set:
            new_data_list.append(str(item) + "_nozxhc")
        else:
            new_data_list.append(item+"__"+dic_code_val[item])
    data = {
    'type':new_data_list
    }

    df = pd.DataFrame(data)

    # 将 DataFrame 写入 Excel 文件
    excel_file = r"D:\zyz\file\zcxh\泰州全业务\台账模板\无人机类型字典_provide_new.xlsx" 
    df.to_excel(excel_file, index=False)


def get_dict_value():
    # 读取 Excel 文件
    excel_file = r"D:\zyz\file\zcxh\泰州全业务\台账模板\作业_型号_整理.xlsx" 

    sheet_name = "Sheet1"  # 工作表名

    # 使用 pandas 读取 Excel 文件
    df = pd.read_excel(excel_file, sheet_name=sheet_name,usecols="A:C")
    data_list = [list(x) for x in df.values]
    
    uav_dic_code_val = p_mysql.get_dict_by_code(['uav_model'])
    work_dic_code_val = p_mysql.get_dict_by_code(['work_nature'])

    #判断两个字典都存在 不存在跳过
    data = []
    for item in data_list:
        if item[0]  in work_dic_code_val.keys() and item[1] in uav_dic_code_val.keys() and item[2] != "\\":
           key = []
           key.append(work_dic_code_val[item[0]]+"_"+uav_dic_code_val[item[1]])
           key.append(item[2])
           data.append(key)
    return data


def import_dict_to_db():
    data = get_dict_value()
    #这块逻辑修改为从数据库读取主键的最大值
    id = 1768901846247718913
    for item in data:
        id = id + 1
        item.append(id)
        item.append('000000')
        item.append('1768856998203408386')
        item.append('workType_device_mapping_mount')
        item.append(1)
        item.append(0)
    print(data)
    #
    p_mysql.insert_data_to_dict(data)









    
   




if __name__ == '__main__':
   pass
   #import_mount_data()
   #generate_diff_excel()
   #import_dict_value()   
   import_dict_to_db()



