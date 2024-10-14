# 1. 计算环境准备

ModelScope为用户提供了免费的算力支持，你无需进行繁琐的环境准备流程，仅需打开网页，便可在线编写与运行程序。

## 步骤一：前往ModelScope官网

前往[ModelScope官网](https://modelscope.cn/my/overview)并进行登录。

> 如果你之前没有注册过ModelScope账号，需要注册ModelScope。

## 步骤二：启动Notebook

登录之后点击左侧边栏的**我的Notebook。**

<img src="https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/r4mlQg5WLA2vqxow/img/a3d0d3a9-5efd-4e7e-b739-7933be86749c.png" alt="我的notebook" width="600px">

你可能需要绑定自己的阿里云资源。在绑定完成后，选择CPU环境，预装镜像选择下图版本。点击**查看Notebook**。

<img src="https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/r4mlQg5WLA2vqxow/img/04693be4-9b35-4e55-aa4b-f6a364208440.png" alt="查看Notebook" width="600px">

在Launcher中，点击下图图标，即可创建一个ipynb格式的Notebook文件。

<img src="https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/r4mlQg5WLA2vqxow/img/00040c4d-f1e5-4958-b98a-5d948839fb91.png" alt="创建Notebook" width="300px">

## 步骤三：在Notebook中运行Hello World

在输入框中输入`print("hello world!")`，点击Cell（代码块）左边的运行按钮，或使用键盘的`shift+enter`，就可以获得如下结果：

<img src="https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/r4mlQg5WLA2vqxow/img/18563090-10cb-4b2f-b3fc-41fb61b3a926.png" alt="查看结果" width="300px">

## 常见问题

1.  如何删除或添加代码块？  
    在当前选中的代码块点击添加按钮，就会在下方添加一个代码块；在当前选中的代码块点击删除按钮，就会删除当前代码块。  
    <img src="https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/r4mlQg5WLA2vqxow/img/538cf4ab-a537-42a0-b43f-0c75148b05c0.png" alt="删除按钮" width="400px">
    
2.  Notebook中除了运行python代码，能添加其它内容吗？  
    你可以添加Markdown格式的内容。在选中代码块之后，点击下图所示位置，将其更改为Markdown，就可以将指定代码块设置为Markdown格式。  
    <img src="https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/r4mlQg5WLA2vqxow/img/e09b29b0-cfc3-41b1-9e2d-b1acf32cda6c.png" alt="删除按钮" width="400px">
    
3.  我的文件会一直保存在ModelScope平台吗？  
    你的ipynb文件会持久化保存在ModelScope平台上，但是其它文件会在4个小时的有效期结束后清空。更多关于ModelScope Notebook的问题，请参考[Notebook参考文档](https://modelscope.cn/docs/Notebook%E5%8A%9F%E8%83%BD%E6%A6%82%E8%BF%B0)。