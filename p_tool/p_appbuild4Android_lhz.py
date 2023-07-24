import subprocess

ssep_app_vue_dir = r'D:\enStudio\ssep-app'
cordova_ssep_app = r'D:\ssepdev\ssep-app'

#切换目录  是否可以通过环境变量去设置
cmd_npm_build = r'cd /d ' + ssep_app_vue_dir + r'\ssep-app-vue '+ ' & npm run build'
print(cmd_npm_build)

p = subprocess.Popen(args=cmd_npm_build,shell=True)

try:
    p.wait(timeout=200)
    print("npm run build sucess")
except subprocess.TimeoutExpired:
    p.kill()
    print("npm run build failed")
    exit(1)

#r 取消转义
srcDir = ssep_app_vue_dir + r'\www'
destDir = cordova_ssep_app+ r'\www'
cmd_xcopy = r"xcopy /s/y "+srcDir+" "+destDir
print(cmd_xcopy)

p1 = subprocess.Popen(args=cmd_xcopy,shell=True)

try:
    p1.wait(timeout=60)
    print("move sucess")
except subprocess.TimeoutExpired:
    p1.kill()
    print("move failed ")
    exit(1)


 #执行安卓build
cmd_build_android = r'cd /d '+ cordova_ssep_app
cmd_build_android += '& cordova build android'
p2 = subprocess.Popen(args=cmd_build_android,shell=True)

try:
    p2.wait(timeout=300)
    print("build android sucess")
except subprocess.TimeoutExpired:
    p2.kill()
    print("build android failed ")
    exit(1)

