
## 🚄 前言 

动手实践是学习大模型的过程中必不可少的环节。为了帮助你更好的掌握相关知识，我们在每个章节都设计了丰富的示例代码。

建议你通过阿里云人工智能平台 PAI 上的 [DSW](https://help.aliyun.com/zh/pai/user-guide/dsw-overview)进行课程学习，借助 PAI DSW，你可以像下图所示的那样，在阅读课程文档的同时运行代码，以便更好地理解和应用大模型。

<img src="https://img.alicdn.com/imgextra/i4/O1CN01jh8Sp41NNc4S3fp4u_!!6000000001558-1-tps-512-176.gif" alt="PAI DSW Notebook Demo" width="500px">

## 开始
接下来我们将一起准备好基于 PAI DSW 的在线学习环境。

> 阿里云为新用户提供了 PAI DSW 的免费试用，在正式创建 PAI DSW 实例之前，你可以通过[阿里云的免费试用频道](https://free.aliyun.com/?searchKey=%E4%BA%A4%E4%BA%92%E5%BC%8F%E5%BB%BA%E6%A8%A1+PAI-DSW)来领取免费试用额度。
> 
> <img src="https://img.alicdn.com/imgextra/i2/O1CN01lS7pPJ1J3DyiROdLB_!!6000000000972-0-tps-946-838.jpg" width="260px" alt="免费试用">

### 步骤一：创建 PAI DSW 实例

1.  首先你需要前往[PAI控制台](https://pai.console.aliyun.com/?regionId=cn-hangzhou#/workspace/overview)。
    
2.  如果你没有开通PAI平台服务，根据指引开通PAI并创建默认工作空间，点击**确认开通并创建默认工作空间**。等待开通完成后，点击**前往默认工作空间**。
    
    <img src="https://img.alicdn.com/imgextra/i4/O1CN01SxUAgU1GEj4jiwFYW_!!6000000000591-0-tps-2430-1736.jpg" alt="我的notebook" width="500px">

3.  点击左侧边栏的**交互式建模（DSW）**，点击**新建实例**。

    <img src="https://img.alicdn.com/imgextra/i2/O1CN01CrbZLb1OEk0wgkBQe_!!6000000001674-0-tps-846-1076.jpg" alt="我的notebook" width="300px">

    在新建实例页面，填写实例名称、选择资源规格和镜像：

      *   **实例名称**：可以填写**aliyun\_acp\_learning**，或者其他方便自己记忆和查找的名字。
    
      *   **资源规格**：推荐选择**免费试用页签**中的**ecs.g6.xlarge**。  
          无需选择 GPU 实例，因为该规格足以运行本课程的大多数项目，可以在后续需要用到 GPU 实例的章节时，再创建 GPU 实例以减少免费额度消耗（免费额度允许你使用 CPU 实例 8000 小时或 GPU 实例 715 小时）。
    
      *   **镜像**：推荐选择**modelscope:1.18.0-pytorch2.3.0-cpu-py310-ubuntu22.04**（需要将芯片类型切换为CPU）。    

    其它保持默认，单击**确定**，完成实例的创建，实例创建通常不会超过5分钟。

    <img src="https://img.alicdn.com/imgextra/i2/O1CN01U9Ojw01PuFWajHfhq_!!6000000001900-0-tps-1902-1192.jpg" alt="我的notebook" width="600px">

    当实例状态为运行中时，单击**操作**列中的**打开**，就可以进入到 DSW 提供的在线 Notebook 界面。

    > DSW是按照实例运行时间进行免费额度的抵扣或计费，如果你在学完某章节后暂时不使用该实例，建议及时停止实例。

    > 如果你没有免费额度，也可以尝试使用[ModelScope的Notebook功能](https://modelscope.cn/my/mynotebook)完成本教程学习。

#### 检查环境变量

- 请检查你当前的 **python** 版本是 3.10 版本，你可以在命令行输入```python --version```来确认。

- 我们建议你直接使用上文介绍的镜像 **modelscope:1.18.0-pytorch2.3.0-cpu-py310-ubuntu22.04** 。

- 如果你使用镜像时遇到了版本冲突方面的问题，我们建议你创建自己的环境，你可以参考本文最后的**拓展阅读**中的内容，搭建一个新的python环境。

### 步骤二：获取大模型ACP课程的代码

在DSW中，你可以通过点击顶部的 Terminal 来进入命令行环境：

<img src="https://img.alicdn.com/imgextra/i1/O1CN017mqjfk1v1Lkvazikm_!!6000000006112-0-tps-1648-628.jpg" alt="打开Terminal" width="500px"><br>


然后你就可以在在 Terminal 中输入以下命令来获取 ACP 课程的代码：

```bash
git clone https://github.com/AlibabaCloudDocs/aliyun_acp_learning.git
```
> 如果遇到网络问题，也可以从atomgit获取：`git clone https://atomgit.com/alibabaclouddocs/aliyun_acp_learning.git`  
> 如果你比较熟悉 jupyter notebook，希望在本地运行，建议你使用 python 3.10 环境来运行。



运行完成后，在顶部切换到Notebook，你就可以在文件树中看到aliyun\_acp\_learning文件夹了。

<img src="https://img.alicdn.com/imgextra/i1/O1CN01WLnveT1oCcBZUt7tP_!!6000000005189-0-tps-870-480.jpg" alt="打开Terminal" width="300px"><br>

## 总结
你已经准备好了环境并获取到了课程代码，。

接下来你可以在文件树中点击 ```./aliyun_acp_learning/大模型ACP认证教程/p2_构造大模型问答系统``` 文件夹，就能看到下一章的教程内容了。

<img src="https://img.alicdn.com/imgextra/i1/O1CN01OMsFi61C9S3FlXOZL_!!6000000000038-0-tps-964-1270.jpg" alt="第二章内容" width="300px">

为了方便阅读，你可以通过左侧菜单，打开当前文档的导读界面：

<img src="https://img.alicdn.com/imgextra/i2/O1CN01yqsscw1kJFStmVJVK_!!6000000004662-2-tps-1398-960.png" alt="导读" width="300px">

如果你不习惯深色主题，也可以在顶部的 Settings 菜单中调整：

<img src="https://img.alicdn.com/imgextra/i4/O1CN01E7kH2F1fBqzPMkkoZ_!!6000000003969-2-tps-961-279.png" alt="设置" width="600px">

祝你在之后的课程学习之旅一切顺利！

### 拓展阅读
如果你希望在本地或其他环境中运行课程代码，建议你使用 python 3.10，以确保课程代码可以正常运行。

如果你所用的环境已经有其他 python 版本，可以参考下面的步骤创建一个 python 3.10 的环境，。

#### 1. 通过 Conda 创建 Python 环境

执行以下指令可以让你创建一个 3.10 版本的 python 环境。

    ```shell
    conda create -n learnacp python=3.10.15 -y -q
    conda activate learnacp
    ```

执行以下指令，可以将 learnacp 注册到 notebook 的环境变量列表中，这样你在 notebook 中指定 learnacp 环境后开始编码。


    ```shell
    pip install ipykernel
    python -m ipykernel install --user --name learnacp --display-name "py310(learnacp)"
    ```

新的环境安装完成后，你可以在notebook的右上角点击切换。比如你用上述代码创建的 ```py310(learnacp)``` 环境。
 
<img src="https://gw.alicdn.com/imgextra/i3/O1CN015RdWi21gMDZG6A7Ga_!!6000000004127-0-tps-868-292.jpg" width="320px" alt="切换kernel">



#### 2. 在新 Python 环境里安装项目依赖
执行如下命令可激活新创建的环境变量 
```shell 
conda activate learnacp
```

从命令行进入文件夹 ```./aliyun_acp_learning/``` 运行以下命令 ，安装本课程所需的依赖环境。

```shell 
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ 
```

#### 3. DSW 的常见问题

Q1:为什么 DSW 里的 WebIDE 和 Notebook 交互输入框位置不一样？

A1: 在 2.1 教程中，你会输入 API Key，如果你使用 Notebook，那么输入框会非常容易看到（就在运行代码块的下方）；

<img src="https://img.alicdn.com/imgextra/i1/O1CN01bNeIzG1PJ9SjOilw7_!!6000000001819-0-tps-1642-286.jpg" width="500px" alt="切换kernel">

如果你使用 WebIDE，那么输入框会出现在代码文件的正上方。

<img src="https://img.alicdn.com/imgextra/i2/O1CN01horPgp1foKH3nnLW8_!!6000000004053-0-tps-1660-604.jpg" width="500px" alt="切换kernel">

Q2: 在 Notebook 中能够直接看到图片，可是为什么双击图片所在的 Markdown 块后，图片就显示不出来了？

A2: 这是因为双击图片所在的 Markdown 块后就进入了编辑模式，你只要点击 Markdown 块之外的代码块进入查看模式，图片就会显示出来了。

<img src="https://img.alicdn.com/imgextra/i4/O1CN012mnKlz1Q5hRev3onD_!!6000000001925-1-tps-1240-372.gif" width="500px" alt="切换kernel">

