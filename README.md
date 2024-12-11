# 🌦️基于机器学习的天气预测及可视化 WeatherNow


[![Contributors][contributors-shield]][contributors-url][![Forks][forks-shield]][forks-url][![Stargazers][stars-shield]][stars-url][![Issues][issues-shield]][issues-url][![MIT License][license-shield]][license-url]
<!-- 项目 LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Tyxy-R/WeatherNow">
    <img src="images/logo/trans_bg.png" alt="Logo" width="300" height="300">
  </a>

  <h3 align="center"><img src="https://user-images.githubusercontent.com/74038190/213844263-a8897a51-32f4-4b3b-b5c2-e1528b89f6f3.png" width="50px" /> &nbsp;Weather Now   <img src="https://user-images.githubusercontent.com/74038190/213844263-a8897a51-32f4-4b3b-b5c2-e1528b89f6f3.png" width="50px" /> &nbsp;</h3>

  <p align="center">
    基于机器学习的天气预测及可视化模型！
    <br />
    <a href="https://365.kdocs.cn/l/caMYQV4FKOYM"><strong>浏览文档 »</strong></a>
    <br />
    <br />
    <a href="https://weathernow-android.streamlit.app/">🔗 查看 Demo</a>
    ·
    <a href="https://github.com/Tyxy-R/WeatherNow/issues">🐞 反馈 Bug</a>
    ·
    <a href="https://github.com/Tyxy-R/WeatherNow/issues">✨ 请求新功能</a>
  </p>
</div>


<div align="center">


[:page_with_curl: 更新日志](https://github.com/Tyxy-R/WeatherNow/blob/main/docs/%7Flog.md)[ :clipboard: 项目规范](https://github.com/Tyxy-R/WeatherNow/blob/main/docs/project-guidelines.md)

</div>
<div id="top"></div>

**关于本项目**


![image](https://github.com/Tyxy-R/WeatherNow/main/images/loading.gif)
GitHub 上有很多优秀的关于天气预测的 Repository ，但都是基于本地化和网络爬虫进行的，所以我创建了这个Repository。我们的项目基于机器学习的随机森林模型对天气进行预测，并且通过Streamlit Cloud 部署到服务器端。
<!---->


当然，没有一个Repository可以满足所有人的要求，因为你的需求可能与众不同。所以我们会在未来添加更多内容。你也可以通过复刻（fork）本仓库并且创建一个拉取请求（pull request）或者创建议题（issue）来向我们提出建议。感谢所有帮助我们扩充本仓库的贡献者！


如果你对我的网站感兴趣，欢迎访问我的线上网站[🌦️Weather Now](https://weathernow-android.streamlit.app/) 来开始。



## ✨ 功能
* **实时天气查询**：获取全球各城市的当前天气。
* **机器学习预测**：使用随机森林算法训练模型并拟合数据
* **天气详细信息**：显示温度、湿度、气压、风速等。
* **简洁易用**：友好的用户界面和交互体验。

## ⌨️ 技术栈
* **前端**：HTML, CSS, JavaScript
* **后端**：Python
* **API**：Streamlit API 
  
<!-- 使用方法 示例 -->
## 📦 项目架构
<details>

<summary>
软件结构规范
</summary>

### 软件结构规范
WeatherNow 项目符合现代 Web 开发的最佳实践，结构简洁清晰、模块化设计良好、易于扩展和维护。通过分离关注点、合理的 API 密钥管理以及清晰的文档，项目不仅具备高可用性和安全性，同时也便于开发者扩展和社区贡献。

本项目大体上采用了分层系统风格架构。
总体分为**表示层**，**应用层**，**服务层**，**数据访问层**。
层与层之前不能直接进行互通，非相邻分层之间不可以进行数据互通，只可以进行迭代访问。
```
表示层： 负责处理用户界面和用户交互。例如，网页或移动应用的前端界面。
应用层： 包含系统的业务逻辑，处理用户请求并执行相关的操作。
服务层： 提供应用层所需的特定服务，如认证或数据转换服务。
数据访问层： 负责与数据库或其他持久性存储进行交互。
```



_转到 [SoftwareArchitecture](docs/SoftwareArchitecture.md) 查看更多介绍_

</details>


<details>

<summary>
文件规范
</summary>


### 文件规范
我们遵循了 Github 项目：[pythonic-project-guidelines](https://github.com/pyloong/pythonic-project-guidelines)的规范要求，对项目文件结构构成如下：
> WeatherNow/
├── db              
├── src  
├ &emsp;    ├──lib  
├ &emsp;    ├──main\.py  
├── images        
├── test       
├── README\.md    
├── VISUALIZATION\.py

_转到 [project-guidelines](/docs/project-guidelines.md) 查看更多介绍_

</details>



## 🚀 部署环境


本项目完全由Python构建，请你确保正确安装了Python。
为避免Pypi兼容性，你的Python版本应在**3.9及以上**。
你可以通过以下方式查看你的Python版本
* Power Shell
  ```sh
  python --version​
  ```
* Python
  ```sh
  import sys
  #sys模块提供了一系列有关Python运行环境的变量和函数。
  print(sys.version)
  ```





<!-- 开始 -->
## 🏃 开始

这是一份在**本地**构建项目的指导的例子。
要获取本地副本并且配置运行，你可以按照下面的示例步骤操作。

### 🛠️ 依赖

如果你尝试本地部署本项目，请确保你正确安装了以下这些模块，以下是两种依赖安装的例程，他将指导你如何正确配置依赖。
1. 我们提供了配置依赖的工具[ Require.exe ](/Require.exe)，你可以**避免所有的命令行操作**，只需要运行此工具即可。

2. 如果你使用的并非`windos`系统或者基于其他理由希望使用命令行。
   你可以通过**依赖管理工具**，例如`pip`来安装这些模块。以下是使用`pip`进行依赖配置的例程。你可以在命令行中输入如下命令：
  >[!TIP]
  >在此之前，请确保你的`pip`处于最新版本
  >你可以通过如下命令对`pip`更新
  >```cmd
  >pip install --upgrade pip
  >```
  ```
  pip install moudelname
  ```

* [numpy](https://pypi.org/project/numpy/)
* [streamlit](https://pypi.org/project/streamlit/)
* [pandas](https://pypi.org/project/pandas/)
* [scikit_learn](https://pypi.org/project/scikit_learn/)

_转到 [requirements.txt](/requirements.txt) 查看所有你所应安装的模块_




### 👨‍💻 安装

下面是一个指导你如何安装和配置你的应用的例子。这个模板**不需要**任何服务器知识或相关网络服务。


1. 克隆本仓库
   ```sh
   git clone https://github.com/Tyxy-R/WeatherNow.git
   ```
2. 使用命令行工具安装外部依赖
    ```
    pip install -r requirements.txt
    ```
3. 使用命令行工具启动项目
   ```
   streamlit run /yourpath/src/VISUALIZATION.py
   ```
************************
如果你对命令行不熟悉或者基于其他任何原因希望避免使用命令行，我们提供了[ WeatherNow.exe ](WeatherNow.exe)帮助你进行**一键安装**。你所需要的做的仅有：
1. 从[ release ](https://github.com/Tyxy-R/WeatherNow/releases)中下载我们最新的发行版本。
2. 运行[ WeatherNow.exe ](WeatherNow.exe)
3. **enjoy it** :smile:








<!-- 路线图 -->
## 📝 项目更新

- [ ] 针对训练数据进行本地化存储
- [ ] 进一步调优模型的拟合效果
- [ ] 更换数据源减少网站响应延迟
- [ ] 使用Streamlit Cloud进行服务器部署
- [ ] 进一步优化可视化界面


到 [open issues](https://github.com/Tyxy-R/WeatherNow/issues) 页查看所有请求的功能 （以及已知的问题）。



<!-- 贡献 -->
## ✍️ 贡献

贡献让开源社区成为了一个非常适合学习、启发和创新的地方。你所做出的任何贡献都是**受人尊敬**的。

如果你有好的建议，请复刻（fork）本仓库并且创建一个拉取请求（pull request）。你也可以简单地创建一个议题（issue），并且添加标签「enhancement」。不要忘记给项目点一个 star！再次感谢！

1. 复刻（Fork）本项目
2. 创建你的 Feature 分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的变更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到该分支 (`git push origin feature/AmazingFeature`)
5. 创建一个拉取请求（Pull Request）


<!-- 许可证 -->
## 📃 许可证

根据 MIT 许可证分发。打开 [LICENSE](LICENSE) 查看更多内容。

<!-- 联系我们 -->
## 🤝 联系我们

<div align=center>

<a herf="https://github.com/Tyxy-R"><img src="https://avatars.githubusercontent.com/u/116926526?s=96&v=4">

@author:R  

<div align=center><img src="https://workspace.google.com/lp/static/images/logo-gmail.png?fingerprint=c2eaf4aae389c3f885e97081bb197b97" alt="tian5784879@gmail.com"  width="15" height="15">tian5784879@gmail.com</div>

项目链接: [https://github.com/Tyxy-R/WeatherNow](https://github.com/Tyxy-R/WeatherNow)
</div>



<!-- 致谢 -->
## 💛致谢

此项目的可视化模板和对streamlit部署环境处理主要灵感来源于作者`JuneWaySue`  
此项目的可视化界面的大部分组件主要来源于[Streamlit Gallery](https://streamlit.io/gallery)，感谢为开源做出贡献的作者。

* [GW Quickview](https://gw-quickview.streamlit.app/)
* [30Day of Streamlit](https://30days.streamlit.app/)
* [JuneWaySue](https://github.com/JuneWaySue)
* [Streamlit中文文档](https://www.streamlit.org.cn/)


<p align="right">(<a href="#top">返回顶部</a>)</p>



<!-- MARKDOWN 链接 & 图片 -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Tyxy-R/WeatherNow.svg?style=for-the-badge
[contributors-url]: https://github.com/Tyxy-R/WeatherNow/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Tyxy-R/WeatherNow.svg?style=for-the-badge
[forks-url]: https://github.com/Badmin1025/WeatherNow/network/members
[stars-shield]: https://img.shields.io/github/stars/Tyxy-R/WeatherNow.svg?style=for-the-badge
[stars-url]: https://github.com/Tyxy-R/WeatherNow/stargazers
[issues-shield]: https://img.shields.io/github/issues/Tyxy-R/WeatherNow.svg?style=for-the-badge
[issues-url]: https://github.com/Tyxy-R/WeatherNow/issues
[license-shield]: https://img.shields.io/github/license/Tyxy-R/WeatherNow.svg?style=for-the-badge
[license-url]: https://github.com/Tyxy-R/WeatherNow/blob/master/LICENSE.txt


