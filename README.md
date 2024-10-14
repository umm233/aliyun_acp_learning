# 阿里云大模型ACP教程

<img src="https://gw.alicdn.com/imgextra/i1/O1CN01xol8Y21oUw1VeGgbZ_!!6000000005229-0-tps-1096-569.jpg" alt="main" width="800px">

## :balloon: 欢迎新同学

欢迎来到阿里云大模型ACP高级工程师认证课程，这是阿里云大模型认证的进阶篇。在开始课程之前，先来了解阿里云大模型认证的体系架构，方便你选择适合自己定位的课程。
阿里云大模型认证体系架构：

<img src="https://gw.alicdn.com/imgextra/i1/O1CN01MC00f61wMhpgctA1q_!!6000000006294-0-tps-1445-478.jpg" alt="我的notebook" width="800px">

> 如果你尚不具备编程基础，或者想从零开始了解大模型，请跳转:point_right:[阿里云大模型ACA工程师认证课程](https://edu.aliyun.com/course/3126500)


## :feather:  课程定位

了解课程定位会帮助你更好地规划学习路径，确保课程内容与个人目标相匹配，从而提升学习效率和成果。通过学习阿里云大模型高级工程师ACP认证课程，你将
- 掌握以下知识与技能：
    - 大模型提示词技巧
    - 检索增强和微调的原理和流程
    - LangChain、Llama-Index和Dify等大模型开发组件的使用方法
    - 工程化评测的概念与方法
    - 大模型的规范和安全性
- 有能力完成以下任务：
    - 使用阿里云百炼平台构建大模型应用(开发、测评、部署、发布)
    - 使用提示词策略、检索增强、微调技术优化大模型回答质量
    - 使用Multi-Agent进行文本、图像、视频等多模态内容生产
    - 能够针对复杂业务场景设计并实施大模型驱动的解决方案
- 胜任以下岗位：
    - 大模型解决方案高级工程师
    - 大模型应用开发高级工程师


## :notebook: 课程列表

在阿里云大模型ACP认证中，课程整体将会以项目式的结构呈现。以项目式的结构设计课程可以帮助学员掌握课程所需的核心概念和技能，并且应用这些知识和技能解决实际问题。
在阿里云大模型ACP认证课程中，你将作为一位教育内容开发公司的员工，构建一个基于大模型的答疑机器人，从而解决新员工入职频繁答疑的问题；随后在公司需要教育课程时，你会利用大模型生成多种形式的教学内容，帮助公司完成业务目标。
通过这两个项目的练习，希望你可以思考如何将大模型的能力带入到不同的行业中，最终可以面向不同的业务场景设计并实施大模型驱动的解决方案。

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

<table>
<thead>
 <tr>
    <td style="background-color:#f2f2f2; font-weight:bold; padding:10px; border: 1px solid #ddd;">章序号</td>
    <td style="background-color:#f2f2f2; font-weight:bold; padding:10px; border: 1px solid #ddd;">章节名称</td>
    <td style="background-color:#f2f2f2; font-weight:bold; padding:10px; border: 1px solid #ddd;">课程序号</td>
    <td style="background-color:#f2f2f2; font-weight:bold; padding:10px; border: 1px solid #ddd;">课程链接</td>
 </tr>
 </thead>
 <tbody>
  <tr>
    <td rowspan="1" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">1</td>
    <td style="padding:10px; border: 1px solid #ddd;">Before start：环境准备</td>
    <td style="padding:10px; border: 1px solid #ddd;">1.0</td>
    <td style="padding:10px; border: 1px solid #ddd;">计算环境准备</td>
  </tr>
  <tr>
    <td rowspan="9" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">2</td>
    <td rowspan="9" style="padding:10px; border: 1px solid #ddd;">借助大模型构建答疑机器人</td>
    <td style="padding:10px; border: 1px solid #ddd;">2.0</td>
    <td style="padding:10px; border: 1px solid #ddd;">项目背景</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">2.1</td>
    <td style="padding:10px; border: 1px solid #ddd;">通过LlamaIndex开发新人答疑机器人</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">2.2</td>
    <td style="padding:10px; border: 1px solid #ddd;">优化提示词工程</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">2.3</td>
    <td style="padding:10px; border: 1px solid #ddd;">优化RAG索引与召回策略</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">2.4</td>
    <td style="padding:10px; border: 1px solid #ddd;">微调意图分类模型</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">2.5</td>
    <td style="padding:10px; border: 1px solid #ddd;">使用智能体和插件</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">2.6</td>
    <td style="padding:10px; border: 1px solid #ddd;">应用工程化评测</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">2.7</td>
    <td style="padding:10px; border: 1px solid #ddd;">应用安全与稳定性</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">2.8</td>
    <td style="padding:10px; border: 1px solid #ddd;">在生产环境中部署与发布</td>
  </tr>
    <tr>
    <td rowspan="6" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">3</td>
    <td rowspan="6" style="padding:10px; border: 1px solid #ddd;">借助大模型辅助内容生产</td>
    <td style="padding:10px; border: 1px solid #ddd;">3.0</td>
    <td style="padding:10px; border: 1px solid #ddd;">项目背景</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">3.1</td>
    <td style="padding:10px; border: 1px solid #ddd;">构建课程内容生成工作流</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">3.2</td>
    <td style="padding:10px; border: 1px solid #ddd;">构建课程内容翻译工作流</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">3.3</td>
    <td style="padding:10px; border: 1px solid #ddd;">构建课程内容转PPT工作流</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">3.4</td>
    <td style="padding:10px; border: 1px solid #ddd;">构建课程内容转音频工作流</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">3.5</td>
    <td style="padding:10px; border: 1px solid #ddd;">构建课程内容转视频工作流</td>
  </tr>
  </tbody>
</table>



## :100:考试大纲

带着目的学习可以提升学习效率。在开始课程之前，请了解大模型ACP认证的考试大纲，将更有利于你的课程学习。
### :star2:考试知识点分布


<table>
<thead>
 <tr>
    <td style="background-color:#f2f2f2; font-weight:bold; padding:10px; border: 1px solid #ddd;">考核知识点</td>
    <td style="background-color:#f2f2f2; font-weight:bold; padding:10px; border: 1px solid #ddd;">试题比例</td>
 </tr>
 </thead>
 <tbody>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">大模型应用开发</td>
    <td style="padding:10px; border: 1px solid #ddd;">16%</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">大模型提示词工程</td>
    <td style="padding:10px; border: 1px solid #ddd;">24%</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">大模型检索增强</td>
    <td style="padding:10px; border: 1px solid #ddd;">24%</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">大模型微调</td>
    <td style="padding:10px; border: 1px solid #ddd;">16%</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">大模型应用安全</td>
    <td style="padding:10px; border: 1px solid #ddd;">8%</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">AI 辅助多模态内容生产</td>
    <td style="padding:10px; border: 1px solid #ddd;">12%</td>
  </tr>
  
  </tbody>
</table>

### :star2:考试大纲
<table>
<thead>
 <tr>
    <td width="140px" style="background-color:#f2f2f2; font-weight:bold; padding:10px; border: 1px solid #ddd;">主要章节</td>
    <td width="300px" style="background-color:#f2f2f2; font-weight:bold; padding:10px; border: 1px solid #ddd;">主要内容</td>
    <td style="background-color:#f2f2f2; font-weight:bold; padding:10px; border: 1px solid #ddd;">考察知识点</td>
 </tr>
 </thead>
 <tbody>
  <tr>
    <td rowspan="1" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">大模型应用开发</td>
    <td style="padding:10px; border: 1px solid #ddd;">通过OpenAI API调用大模型 <br> 通过LlamaIndex向通义千问提问</td>
    <td style="padding:10px; border: 1px solid #ddd;">基本API参数如model、temperature、top_p等等 <br>批量生成与流式生成 <br> 理解消息与对话历史</td>
  </tr>
  <tr>
    <td rowspan="2" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">大模型提示词工程</td>
    <td style="padding:10px; border: 1px solid #ddd;">构建有效的提示词</td>
    <td style="padding:10px; border: 1px solid #ddd;">提示词框架如提示词要素、提示词分隔符、提示词模板 <br> 理解系统角色提示词的作用</td>
  </tr>
    <tr>
    <td style="padding:10px; border: 1px solid #ddd;">利用大模型创建算法应用</td>
    <td style="padding:10px; border: 1px solid #ddd;">理解大模型的适用场景<br> 利用大模型开发应用算法（如批量对员工咨询做意图分类、用大模型做文档审阅、实现针对问题的自动文档修订）</td>
  </tr>
   <tr>
    <td rowspan="3" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">大模型检索增强</td>
    <td style="padding:10px; border: 1px solid #ddd;">通过LlamaIndex构建RAG应用的基本使用方法</td>
    <td style="padding:10px; border: 1px solid #ddd;">理解RAG的核心要素，如文件解析、文本切片、段落召回、段落重排序。<br>理解对RAG做召回优化如句子窗口检索、自动合并检索等等。</td>
  </tr>
<tr>
    <td style="padding:10px; border: 1px solid #ddd;">持续优化检索增强能力</td>
    <td style="padding:10px; border: 1px solid #ddd;">理解更贴近实战的RAG优化方法如优化文本解析、标题改写优化、表格内容增强、文本分割方法对比等等</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">对检索增强的能力做自动化评测</td>
    <td style="padding:10px; border: 1px solid #ddd;">了解RAGAS指标体系<br>懂得RAG系统的评测方法。</td>
  </tr>
  <tr>
    <td rowspan="2" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">大模型的微调</td>
    <td style="padding:10px; border: 1px solid #ddd;">微调的概念与要求</td>
    <td style="padding:10px; border: 1px solid #ddd;">型微调的作用、前提、基本步骤、常用算法</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">微调的实验与评测</td>
    <td style="padding:10px; border: 1px solid #ddd;">微调数据集构建、微调参数介绍、微调模型评测</td>
  </tr>
  <tr>
    <td rowspan="1" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">大模型智能体与插件</td>
    <td style="padding:10px; border: 1px solid #ddd;">基于百炼Assistant API构建智能体</td>
    <td style="padding:10px; border: 1px solid #ddd;">理解智能体运行机制<br>掌握用生成多模态内容、构建个性化语音助手等能力</td>
  </tr>
  <tr>
    <td rowspan="2" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">大模型应用安全</td>
    <td style="padding:10px; border: 1px solid #ddd;">内容安全合规检查手段</td>
    <td style="padding:10px; border: 1px solid #ddd;">了解大模型开发中存在的内容安全问题<br>了解内容安全合规检测类型及常用方案</td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">大模型应用部署（云服务）安全</td>
    <td style="padding:10px; border: 1px solid #ddd;">了解在云服务环境下应用系统安全的基本要素和解决方案</td>
  </tr>
  <tr>
    <td rowspan="1" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">部署大模型应用</td>
    <td style="padding:10px; border: 1px solid #ddd;">在云上部署微调模型的基本方案<br>在云服务如（ECS、FC、PAI）中部署模型<br>在百炼上部署模型</td>
    <td style="padding:10px; border: 1px solid #ddd;">掌握如何使用vLLM进行大模型的部署操作<br>了解如何利用云服务如函数计算（FC）实现AI助手的快速发布</td>
  </tr>
  <tr>
    <td rowspan="2" style="background-color:#f9f9f9; padding:10px; border: 1px solid #ddd; vertical-align:top;">AI 辅助内容生产</td>
    <td style="padding:10px; border: 1px solid #ddd;">用 AI 辅助开发教学课件PPT</td>
    <td style="padding:10px; border: 1px solid #ddd;">了解阿里发布的通义系列多模态大模型及算法服务如Qwen-Max、Qwen-VL、通义万相、CosyVoice等作用和使用方法。
    </td>
  </tr>
  <tr>
    <td style="padding:10px; border: 1px solid #ddd;">用 AI 辅助将教学课件转为视频课件</td>
    <td style="padding:10px; border: 1px solid #ddd;">了解如何使用但不限于Flux-Merged、Marp、moviepy、ffmpeg等多媒体工具来辅助生成视频内容
    </td>
  </tr>
  </tbody>
</table>

本考纲旨在为考生提供考试内容的普遍方向，考试范围不仅限于文中提及的部分，可能还包括其他相关未列明的内容。


## :pushpin:问题反馈

如果你在学习过程中遇到任何问题，欢迎你参与问卷_____________反馈学习体验和课程评价。
你的批评和鼓励都是我们前进的动力！

