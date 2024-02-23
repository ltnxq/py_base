from distutils.core import setup
import py2exe  # type: ignore


'''
需要在cmd命令中执行打包的命令 不是直接run py
例如
python p_py_2_exe.py py2exe
'''

INCLUDES = []

#设置一些参数
options = {
    "py2exe" :
        {
            "compressed" : 1, # 压缩   
            "optimize" : 2,
            "bundle_files" : 1, # 所有文件打包成一个 exe 文件  
            "includes" : INCLUDES,
            "dll_excludes" : ["MSVCR100.dll"]
        }
}

setup(
    options=options,    
    description = "this is a py2exe test",   
    zipfile=None,
    console = [{"script":'p_word_2_PDF.py'}]
)