# MentoHust2024

## 致敬mentohust

人到华中大，有甜亦有辣。明德厚学地，求是创新家

## 实现方式

利用selenium调用edge爬取学校认证服务器

## 使用方式

修改config.json里的账号密码,可以自己在autoconnect.py里配置具体规则,多个账号切换

### 源码使用方法

需要python selenium库,使用以下命令安装

```

pip install selenium
```

默认需要edge,可以自行修改为火狐,chrome

autoconnect.py同目录下放置config.json

[edge需要下载edgedriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

下载后将压缩包移动到此路径,解压在本目录下

### exe使用方法

发布版本使用方法,同目录下放置config.json

[edge需要下载edgedriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## 可二次开发方向

有的学校需要输入或选择其它的栏目,请自行研究

web.py是核心代码,可以拿去调试

之后再改get_connect的函数即可

其他学校需要调整认证服务器,调整跳转url
