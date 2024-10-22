## 🚄 前言 

阿里云大模型ACP课程提供了丰富的Python代码教程。为了能够动手实践这些教程，你需要准备好计算环境，然而计算环境的准备并不轻松。

阿里云的PAI平台为用户提供了免费的算力支持，你无需进行繁琐的环境准备流程，仅需打开网页，便可在线编写与运行程序。我们建议你通过PAI的DSW平台进行课程的学习。


### 步骤一：前往PAI控制台

1.  首先你需要前往[PAI控制台](https://pai.console.aliyun.com/?regionId=cn-hangzhou#/workspace/overview)。
    
2.  如果你没有开通PAI平台服务，根据指引开通PAI并创建默认工作空间，点击**确认开通并创建默认工作空间**。等待开通完成后，点击**进入默认工作空间**。
    
<img src="https://img.alicdn.com/imgextra/i4/O1CN01SxUAgU1GEj4jiwFYW_!!6000000000591-0-tps-2430-1736.jpg" alt="我的notebook" width="500px">

3.  点击左侧边栏的**交互式建模（DSW）**，点击**新建实例**。

<img src="https://img.alicdn.com/imgextra/i2/O1CN01CrbZLb1OEk0wgkBQe_!!6000000001674-0-tps-846-1076.jpg" alt="我的notebook" width="300px">


### 步骤二：启动DSW实例

在新建实例页面，你需要填写三个参数：

*   **实例名称**：此处以**aliyun\_acp\_learning**为例。
    

*   **资源规格**：推荐选择**免费试用页签**中的**ecs.g6.xlarge**，无需选择GPU规格，这个规格足以运行本课程的项目；
    

> 请注意，免费试用的资源包需要领取，用于抵扣DSW实例的费用。领取链接在资源规格页中的**免费试用**页签可以看到。

*   **镜像**：推荐选择**modelscope:1.18.0-pytorch2.3.0-cpu-py310-ubuntu22.04**（需要将芯片类型切换为CPU）。
    

其它保持默认，单击**确定**，完成实例的创建，实例创建通常不会超过5分钟。

<img src="https://img.alicdn.com/imgextra/i2/O1CN01U9Ojw01PuFWajHfhq_!!6000000001900-0-tps-1902-1192.jpg" alt="我的notebook" width="600px">

当实例状态为运行中时，单击**操作**列中的**打开**，就可以启动DSW实例了。

### 步骤三：获取大模型ACP课程的代码仓库

我们的代码仓库存储在了github与atomgit上。你可以通过在Terminal中输入git clone命令来获取我们的代码仓库。

在Launcher中，点击下图的位置，即可打开一个Terminal窗口。  

<img src="https://img.alicdn.com/imgextra/i2/O1CN01DsVZwx1C7cSrXVeYQ_!!6000000000034-0-tps-1082-984.jpg" alt="打开Terminal" width="300px"><br>

在Terminal中输入以下命令：

```bash
git clone https://github.com/AlibabaCloudDocs/aliyun_acp_learning.git
```
如果遇到网络问题，请从atomgit获取。将命令修改为：
```bash
git clone https://atomgit.com/alibabaclouddocs/aliyun_acp_learning.git
```


运行完成后，你就可以在文件树中看到aliyun\_acp\_learning文件夹了。

<img src="https://img.alicdn.com/imgextra/i1/O1CN01WLnveT1oCcBZUt7tP_!!6000000005189-0-tps-870-480.jpg" alt="打开Terminal" width="300px"><br>


#### 拓展阅读：创建Conda环境（可选）

我们提供一组创建环境变量的指令。

- 如果你在自己的个人电脑上安装代码，你可以考虑创建项目专属的环境变量
- 如果你使用临时的云服务，一关机就会丢掉已经安装的依赖项，你也可以考虑忽略这一步。

<style>
    table {
      width: 80%;
      margin: 20px; /* Center the table */
      border-collapse: collapse; /* Collapse borders for a cleaner look */
      font-family: sans-serif; 
    }

    th, td {
      padding: 10px;
      text-align: left;
      border: 1px solid #ddd; /* Light gray border */
    }

    th {
      background-color: #f2f2f2; /* Light gray background for header */
      font-weight: bold;
    }

    tr:nth-child(even) { /* Zebra striping */
      background-color: #f9f9f9;
    }

    tr:hover { /* Highlight row on hover */
      background-color: #e0f2ff; /* Light blue */
    }
</style>
<table width="80%">
<tbody>
<tr>
<td>

```shell
conda create -n learnacp python=3.9.12 -y -q
conda activate learnacp
```
</td>
</tr>
</tbody>
</table>

执行以下命令可以将 learnacp 注册到 notebook 的环境变量列表中，这样你在 notebook 中指定 learnacp 环境后开始编码。比如在python 3.9.12环境中工作。

<table width="80%">
<tbody>
<tr>
<td>

```shell
pip install ipykernel
python -m ipykernel install --user --name learnacp --display-name "py39(learnacp)"
```
</td>
</tr>
</tbody>
</table>


### 步骤四：安装依赖

在 1_0_计算环境准备.ipynb的对应位置运行以下命令，安装本课程所需的依赖环境。

> 由于依赖项较多，你可能需要等待3-5分钟。

```bash
! pip install -r ../../requirements.txt
```



### 步骤五：配置环境变量并安装依赖

你需要前往[百炼API Key管理界面](https://bailian.console.aliyun.com/?apiKey=1)获取API Key，这样才能够使用大模型的API服务。

将API Key配置为环境变量可以保护你的账户安全，这样即使你的代码仓库公开，API Key也不会泄漏。

为了方便你进行环境变量的配置，我们封装好了一个load\_key函数，函数会自动辅助你进行环境变量的配置。

请你在DSW的文件树中打开代码仓库的：**大模型ACP认证教程**/**p1\_课程准备**/**1\_0\_计算环境准备.ipynb**，运行下边的代码块，将会提示你输入API Key，并自动将API Key配置到环境变量，你可以通过print方法查看配置是否生效。

> 如果之前已经配置过API Key，该函数将自动从JSON文件中获取API Key并配置到环境变量。

```python
import sys
import os
sys.path.append("../")
from config.load_key import load_key
load_key()
print(os.environ["DASHSCOPE_API_KEY"])
```


## 总结
你已经成功获取到了我们的代码仓库，并安装好了计算环境。

接下来你可以在文件树中点击 aliyun_acp_learning-大模型ACP认证教程文件夹-p2_构造大模型问答系统 文件夹，就能看到下一章的教程内容了。祝你在之后的课程学习之旅一切顺利！

<img src="https://img.alicdn.com/imgextra/i1/O1CN01OMsFi61C9S3FlXOZL_!!6000000000038-0-tps-964-1270.jpg" alt="第二章内容" width="300px">