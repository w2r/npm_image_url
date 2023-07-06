# npm_image_url

#### 利用npm和github action搭建一个简易图床

##### 简介
	利用github action自动上传图片到npm，并获得图片链接，推送到telegram，效果图如下：
![https://qyucloud.ml/t/K4iTaT](https://qyucloud.ml/t/K4iTaT)
	
#####  代码说明
github action 运行代码来源于：[我的图床解决方案 - YFun's Blog](https://blog.yfun.top/posts/2876015612/) 本人仅做部分修改，具体修改内容如下：
- 修改node-version，12.x --> 16.X
- 安装python3及依赖库
- 增加telegram推送，每次上传后，自动发送图片链接到telegram（备份图片）

##### 准备工作
首先注册npm账号，注册地址：[npm注册](https://www.npmjs.com/)，注册后点击右上角的头像，然后选择Access Token，点击页面中的Generate New Token，classic token，生成Access Token，格式类似： npm_hF0123456789****
##### 安装教程
登录你的github账号，并fork仓库，点击setting， 选择Secrets and variable-->Action，新增四个Secrets ，分别如下

~~~
# 准备工作里npm的Access Token
NPM_TOKEN -->  npm_hF0123456789****************
# botfather（https://t.me/BotFather ）新建机器人，并获得机器人的api token 
TELEGRAM_TOKEN --> 1384839096:AAGWot30iO4************
# 随意转发一条信息给机器人https://t.me/getidsbot， 可以获得telegram用户id
USER_ID --> 561661***
# 镜像选择，优先推荐jsDelivr，国内外速度都很优秀
# 可用参数jsdelivr/zhimg/bdstatic/eleme/unpkg
# 详情查看推荐镜像地址
CDN  -->  jsdelivr

~~~





##### 文件说明
workfolws-->main.yml  action运行文件，无需修改

rawimg和webpimg为临时储存文件夹，rawimg储存上传图片，webpimg储存压缩后的图片，推送到npm后，action会自动删除所有图片，避免github图片滥用封号

package.json, 主要记录版本号和用户名称，name和version可自行修改

~~~
{
  "name": "w2r",
  "version": "1.2.22",
  "description": "版本配置文件，每次图片发布后github action会自动修改",
  "author": "cherbim@MJJ"
}
~~~
	
post2tg.py 推送到telegram（默认文件无需修改）

##### 使用说明
将图片文件上传至仓库的 `rawimg/` 文件夹下，也可以使用第三方工具上传（比如PicGo / UPic 等）
github action的触发方式为Release更新，所以每次上传完图片，需要手动运行action或者更新Release

手动运行action示意图：
![](https://qyucloud.ml/t/aPe18K)




更新Release运行action：
点击右侧release， Draft a new release， 输入新的tag，其他不用修改，最后publish release
![](https://qyucloud.ml/t/rXzPSS)





##### 图片使用链接
以 jsDelivr 为例，原图链接为：
~~~
https://cdn.jsdelivr.net/npm/[package-name]@[version]/rawimg/[filename].[suffix]
~~~
压缩后的图片链接：
~~~
https://cdn.jsdelivr.net/npm/[package-name]@[version]/rawimg/[filename].webp
~~~
参数值说明：
~~~
-[package-name]             package.json文件中name的值
-[version]                  package.json文件中的version的值
-[filename]                 文件名
-[suffix]                   文件后缀名称
~~~
	  
##### 推荐镜像地址
~~~
https://cdn.jsdelivr.net/npm/  # jsDelivr  
https://unpkg.zhimg.com/ # 知乎  
https://code.bdstatic.com/npm/ # 百度 (不推荐)  
https://shadow.elemecdn.com/npm/ # 饿了么  
https://unpkg.com/ # Unpkg
~~~
##### 特殊说明
github action push代码有时抽风，导致push失败，需要手动修改一下版本号码
详细如下如，如果action运行结果出现以下错误，请手动修改package.json的version（必须大于图中的版本号，否则npm 无法publish)

![](https://qyucloud.ml/t/unbTOC)

	


		
