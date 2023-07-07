# npm_image_url

#### 利用npm和github action搭建一个简易图床

##### 友情提示： 

不要fork仓库，容易泄露隐私，自己下载代码，新建仓库并上传代码

##### 简介
手动上传文件到github后，自动触发action上传图片到npm，并将图片链接推送到telegram，同时利用telegram备份图片
效果图如下：
![https://qyucloud.ml/t/K4iTaT](https://qyucloud.ml/t/ur9WrH)
	
#####  代码说明
github action 运行代码来源于：[我的图床解决方案 - YFun's Blog](https://blog.yfun.top/posts/2876015612/) ，原版本使用不方便，需要上传图片后，手动更新release触发action，还要自己修改文件链接，还不能看到图片以及备份图片
本人仅做部分修改，具体修改内容如下：
- 修改node-version，12.x --> 16.X
- 安装python3及依赖库
- 增加telegram推送，每次github上传图片后后，自动发送图片链接到telegram（相当于备份图片）
- 更改action的触发方式， release --> push
- 删除压缩图片代码，直接使用原图

##### 准备工作
首先注册npm账号，注册地址：[npm注册](https://www.npmjs.com/)，注册后点击右上角的头像，然后选择Access Token，点击页面中的Generate New Token，classic token，生成Access Token，格式类似： npm_hF0123456789****
##### 安装教程
登录你的github账号，新建仓库，设置为私有（保护隐私），下载代码并push到自己仓库

不会push的请按以下过程手动操作：

第一步： https://github.com/w2r/npm_image_url/archive/refs/heads/main.zip 下载代码并解压，点击Add file，选择上传post2tg.py和package.json文件到仓库

第二步： 然后点击新建文件，文件名为rawimg/.gitkeep ， 内容空白即可， 同理创建webpimg/.gitkeep
![](https://cdn.jsdelivr.net/npm/w2r@1.2.44/rawimg/cherbim_2023-07-07_01-09-10.webp)


第三部： 复制.github/workflows/main.yml里面的内容，然后点击action，选择new workflow，点击 set up a workflow yourself，把前面复制main.yml内容粘贴进去，最后保存
![](https://cdn.jsdelivr.net/npm/w2r@1.2.43/rawimg/cherbim_2023-07-07_01-00-23.webp)



点击仓库的setting， 选择Secrets and variable-->Action，新增四个Secrets ，分别如下

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

给予Action读写权限
setting --> action --> General， 选择Read and write permissions
如下图：
![](https://cdn.jsdelivr.net/npm/w2r@1.2.39/rawimg/cherbim_2023-07-07_00-34-12.webp)





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
github action的触发方式为`rawimg/`文件夹push文件，所以每次上传完图片，会自动运行action，并推送图片链接到tg


##### 图片使用链接介绍
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
详细如下如，如果action运行结果出现publish package错误，请手动修改package.json的version（必须大于workflow出错图中的版本号，否则npm 无法publish)

![](https://qyucloud.ml/t/unbTOC)

	


		
