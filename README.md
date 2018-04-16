# NTUST_GraphicAnalyze

辨識學生系統的圖形驗證碼

# 使用方式

需要先行安裝 python module PIL

```sh
$ pip install Pillow
```

主程式為 imgToString.py

將 image 傳進 imgToString() 裡

就會回傳 string

example:

```sh
image = Image.open('verifyCode.png')
imageStr = imgToString(image)
print(imageStr)
```

# Screen Shot

  - 18/04/16
![2018-04-16 21-19-02](https://user-images.githubusercontent.com/26863912/38811434-0dfa3a30-41bc-11e8-82f1-f8a2eb4c60b2.png)
