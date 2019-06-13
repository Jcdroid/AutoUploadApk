# -*- coding: utf-8 -*-
__author__ = 'Jcdroid'

from Tkinter import *
import requests
import json
import sys

# 解决编码问题
reload(sys)
sys.setdefaultencoding("utf-8")

root = Tk()
root.title('APK上传fir.im')
root.geometry('600x400')
path = StringVar()
pathShow = StringVar() # 显示文件名

atList = ['18665856941']
notifyUrl = "https://oapi.dingtalk.com/robot/send?access_token=XXX"

def get_upload_certificate():
    form_data = {
        'type':'android',
        'bundle_id':'com.triumen.trmchain',
        'api_token':'965e9b7c5787156f90c878bd2ab44966'
    }
    r = requests.post('http://api.fir.im/apps', data=form_data)
    res = r.text
    print res
    return json.loads(res)

def selectPath():
    path_ = tkinter.filedialog.askopenfilename(filetypes=[("apk文件", ".apk")])
    path.set(path_)

def upload(res):
    file = open('E:/Jcdroid/Android/workspace/trmchain-android/app/build/outputs/apk/devTriumen/release/app-dev-triumen-release.apk', 'rb')
    print file
    form_data = {
        'key':res['cert']['binary']['key'],
        'token':res['cert']['binary']['token'],
        'x:name':'超盟星球',
        'x:version':'1.0.0.DEV',
        'x:build':'1',
        'x:changelog':'',
    }
    files = {
        'file':file
    }
    result = requests.post(res['cert']['binary']['upload_url'], data=form_data, files=files)
    print result
    file.close()

def auto_upload():
    # print '^_^ 欢迎使用自动上传Apk到FIR，祝生活愉快！ ^_^'.decode('utf-8').encode('cp936') # cmd model
    print '^_^ 马上开始上传！ ^_^'.decode('utf-8')
    res = get_upload_certificate()
    upload(res)
    print '^_^ 上传完成！ ^_^'.decode('utf-8')

if __name__ == '__main__':
    auto_upload()
    # Label(root, text='api_token：', width=20).grid(row=0, column=0)
    # apiToken = Entry(root)
    # apiToken.grid(row=0, column=1)
    #
    # Label(root, text='文件路径：').grid(row=1, column=0)
    # Button(root, text="选择文件", command=selectPath).grid(row=1, column=1)
    #
    # Label(root, textvariable=pathShow, bg='white').grid(row=2, column=1, columnspan=2)
    #
    # Label(root, text='更新描述：').grid(row=3, column=0)
    # des = Entry(root)
    # des.grid(row=3, column=1, rowspan=3, sticky=E)
    #
    # Button(root, text="上传", command=auto_upload).grid(row=6, column=1)
    #
    # root.mainloop()
    # https://juejin.im/post/5acc746af265da238e0e11ae