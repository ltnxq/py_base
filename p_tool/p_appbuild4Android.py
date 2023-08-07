import subprocess
import os
import time

def killProcessAndExit(process):
    process.kill()
    time.sleep(10)
    exit(1)

def log_ok(log_str):
    format_log_str = "\033[1;32;40m{}{}{}\033[0m".format("+++++++++++++++++",log_str,"+++++++++++++++++++")
    print(format_log_str)

def log_error(log_str):
    format_log_str = "\033[1;31;40m{}{}{}\033[0m".format("------------------",log_str,"-------------------")
    print(format_log_str)


'''
使用windows_shell 编译打包成安卓 apk 程序
'''
if   __name__ == '__main__':
        
    #环境变量读取ssep-app的项目目录和cordova_ssep_app的项目目录
    ssep_app_vue_dir = os.getenv("ssep_app_vue_dir")
    cordova_ssep_app = os.getenv("cordova_ssep_app")

    #切换目录  是否可以通过环境变量去设置
    cmd_npm_build = r'cd /d ' + ssep_app_vue_dir + r'\ssep-app-vue '+ ' & npm run build'
    print(cmd_npm_build)

    p = subprocess.Popen(args=cmd_npm_build,shell=True)

    try:
        if p.wait(timeout=200) == 0:
           log_ok("npm run build sucess")
        else:
            log_error("some error in npm run build")
            killProcessAndExit(p)
    except subprocess.TimeoutExpired:
        log_error("npm run build failed TimeoutExpired")
        killProcessAndExit(p)
    except subprocess.SubprocessError:
        log_error("npm run build failed SubprocessError")
        killProcessAndExit(p)


    #r 取消转义
    srcDir = ssep_app_vue_dir + r'\www'
    destDir = cordova_ssep_app+ r'\www'
    cmd_xcopy = r"xcopy /s/y "+srcDir+" "+destDir
    print(cmd_xcopy)

    p1 = subprocess.Popen(args=cmd_xcopy,shell=True)

    try:
        if p1.wait(timeout=60) == 0:
          log_ok("xcopy files sucess!")
        else:
            log_error('some error in xcopy!!')
            killProcessAndExit(p1)
    except subprocess.TimeoutExpired:
        log_error("xcopy failed TimeoutExpired ")
        killProcessAndExit(p1)
    except subprocess.SubprocessError:
        log_error("xcopy failed SubprocessError")
        killProcessAndExit(p1)


    #执行安卓build
    cmd_build_android = r'cd /d '+ cordova_ssep_app
    cmd_build_android += '& cordova build android'
    p2 = subprocess.Popen(args=cmd_build_android,shell=True)

    try:
        if p2.wait(timeout=300) == 0:
          log_ok("cordova build android sucess")
        else:
          log_error('some error in cordova build android!!')
          killProcessAndExit(p2)
    except subprocess.TimeoutExpired:
        log_error("cordova build android failed ")
        killProcessAndExit(p2)
    except subprocess.SubprocessError:
        log_error("cordova build android SubprocessError")
        killProcessAndExit(p2)
