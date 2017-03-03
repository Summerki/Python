import os
import os.path  
import shutil

def copyFiles(sourceDir,targetDir):
    i = 1
    for root,dirs,files in os.walk(sourceDir):
        for name in files:
            Olddir = os.path.join(root,name)
            if os.path.isfile(Olddir) and Olddir.find('.apk')>0:
                shutil.copy(Olddir,targetDir)
                print('已经迁移第'+str(i)+'个APP')
                i = i+1

def Rename():
    apklist = os.listdir(targetDir)
    j = 1
    for apks in apklist:
        Olddir = os.path.join(targetDir,apks)
        Split_name = os.path.splitext(apks)
        apk_name = Split_name[0]
        apk_type = Split_name[1]
        New_apk_name = apk_name.strip('_signed')
        Newdir = os.path.join(targetDir,New_apk_name+apk_type)
        os.rename(Olddir,Newdir)
        print('已经重命名第'+str(j)+'个APP')
        j = j + 1
                
        

sourceDir = ''
targetDir = ''
copyFiles(sourceDir,targetDir)
Rename()
print('恭喜，已经全部完成！享受其他的事情吧')
 
