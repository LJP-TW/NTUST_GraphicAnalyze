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

  - 18/04/16 尚有點bug
![2018-04-16 20-18-07](https://user-images.githubusercontent.com/26863912/38808602-5d8631ca-41b3-11e8-97ef-2126f4bf27a4.png)