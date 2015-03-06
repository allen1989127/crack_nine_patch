# crack_nine_patch

#说明
暴力破解android九宫格锁屏脚本

#使用前提
1. 只能破解android手机的九宫格屏幕锁屏

2. 手机必须进行root

#使用说明
1. 将android手机中的/data/system/gesture.key文件提出来

2. 将gesture.key与该脚本放在同一个目录下，并用python执行该脚本

3. 脚本破解成功会输出00010203这类数据，意思就是下表o的4个点

>> o|o|o
>> :---:|:---:|:---:
>> o|x|x
>> x|x|x
