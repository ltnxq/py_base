import os
import win32com.client as win32
import sys


'''
使用前安装python、install win32com.client第三方库
如何使用 python p_word_2_PDF.py  doc文件的绝对路径  
'''

def convert_doc_to_pdf_wps(input_path, output_path):
    '''
    wps的word文档转换为PDF
    '''
    # 获取输入文件的绝对路径
    input_file = os.path.abspath(input_path)

    # 创建WPS应用程序对象
    wps_app = win32.Dispatch("KWPS.Application")

    try:
        # 打开Word文档
        doc = wps_app.Documents.Open(input_file)

        # 保存为PDF格式 、17固定为PDF格式的代号
        doc.ExportAsFixedFormat(output_path, 17)
    except Exception as e:
        print("转换失败：", str(e))
    finally:
        # 关闭Word文档和应用程序
        doc.Close()
        wps_app.Quit()


def convert_word_to_pdf(input_path, output_path):

    '''
    微软的word文档转换为PDF
    '''
    # 获取输入文件的绝对路径
    input_file = os.path.abspath(input_path)

    # 创建Word应用程序对象
    word_app = win32.Dispatch("Word.Application")
    
    try:
        # 打开Word文档
        doc = word_app.Documents.Open(input_file)

        # 保存为PDF格式
        doc.SaveAs(output_path, FileFormat=17)
    except Exception as e:
        print("转换失败：", str(e))
    finally:
        # 关闭Word文档和应用程序
        doc.Close()
        word_app.Quit()




if __name__ == '__main__':
    args = sys.argv
    if(len(args) < 2):
      print("arg error at least input_path ")
      exit(1) 

    input_doc_path = args[1]
    if not os.path.exists(input_doc_path) :
       print("input_doc path is not exits")
       exit(1)

    #得到输入路径的目录和文件名
    index = input_doc_path.find('.')
    out_pdf_path = input_doc_path[0:index] + '.pdf'

    #将basename的文件名后缀替换为pdf
    convert_doc_to_pdf_wps(input_doc_path, out_pdf_path)
    

