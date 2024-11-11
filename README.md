# 基于机器学习的天气预测及可视化 WeatherNow
 
[![GitHub stars](https://img.shields.io/github/stars/admin1025/WeatherNow.svg?style=social&label=Stars)](https://github.com/admin1025/WeatherNow/stargazers)[![GitHub forks](https://img.shields.io/github/forks/admin1025/WeatherNow.svg?style=social&label=Fork)](https://github.com/admin1025/WeatherNow/network/members)[![GitHub watchers](https://img.shields.io/github/watchers/admin1025/WeatherNow.svg?style=social&label=Watch)](https://github.com/admin1025/WeatherNow/watchers)[![GitHub followers](https://img.shields.io/github/followers/admin1025.svg?style=social&label=Follow)](https://github.com/admin1025?tab=followers)

[![GitHub issues](https://img.shields.io/github/issues/admin1025/WeatherNow.svg)](https://github.com/admin1025/WeatherNow/issues)[![GitHub license](https://img.shields.io/github/license/admin1025/WeatherNow.svg)](https://github.com/admin1025/WeatherNow/blob/master/LICENSE)[![GitHub last commit](https://img.shields.io/github/last-commit/admin1025/WeatherNow.svg)](https://github.com/admin1025/WeatherNow/commits)[![GitHub release](https://img.shields.io/github/release/admin1025/WeatherNow.svg)](https://github.com/admin1025/WeatherNow/releases)



[更新日志](/docs/log.md)  
[项目规范](/docs/project-guidelines.md)




<!-- 项目 LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Weather Now</h3>

  <p align="center">
    基于机器学习的天气预测及可视化模型！
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>浏览文档 »</strong></a>
    <br />
    <br />
    <a href="https://github.com/admin1025/WeatherNow">查看 Demo</a>
    ·
    <a href="https://github.com/admin1025/WeatherNow/issues">反馈 Bug</a>
    ·
    <a href="https://github.com/admin1025/WeatherNow/issues">请求新功能</a>
  </p>
</div>






<div id="top"></div>
<!--
*** 感谢查看我们的最佳 README 模板，如果你有好的建议，请复刻（fork）本仓库并且创建一个
*** 拉取请求（pull request），或者直接创建一个带「enhancement」标签的议题（issue）。
*** 不要忘记给该项目点一个 star！
*** 再次感谢！现在快去创建一些了不起的东西吧！:D
-->



<!-- 项目 SHIELDS -->
<!--
*** 我们使用了 markdown 「参考风格」的链接以便于阅读。
*** 参考链接是用方括号 [ ] 包围起来的，而非 圆括号 ( )。
*** 请到文档末尾查看 contributors-url、forks-url 等变量的声明。这是一种可选的简洁语法，你可能会想要使用。
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

 关于本项目

[![产品截图][product-screenshot]](https://example.com)

GitHub 上有很多优秀的关于天气预测的 Repository ，但都是基于本地化和网络爬虫进行的，所以我创建了这个Repository。我们的项目基于机器学习的随机森林模型对天气进行预测，并且通过Streamlit Cloud 部署到服务器端。

以下是原因：
* 希望
* 你不应该一遍又一遍地做重复的工作，比如每次都从头编写一个 README
* 你应该在未来的生活中始终遵循 DRY 原则 :smile:

当然，没有一个Repository可以满足所有人的要求，因为你的需求可能与众不同。所以我们会在未来添加更多内容。你也可以通过复刻（fork）本仓库并且创建一个拉取请求（pull request）或者创建议题（issue）来向我们提出建议。感谢所有帮助我们扩充本仓库的贡献者！


如果你对我的网站感兴趣，欢迎访问我的线上网站[:rainbow:Weather Now](https://weathernowpublic.streamlit.app/) 来开始。





### 构建工具

如果你尝试本地部署本项目，请确保你正确安装了以下这些模块，你可以通过
```python
$ pip install moudelname
```

* [Streamlit](https://nextjs.org/)
* [Requests](https://reactjs.org/)
* [Sklearn](https://vuejs.org/)





<!-- 开始 -->
## 开始

这是一份在本地构建项目的指导的例子。
要获取本地副本并且配置运行，你可以按照下面的示例步骤操作。

### 依赖

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

### 安装

_下面是一个指导你的受众如何安装和配置你的应用的例子。这个模板不需要任何外部依赖或服务。_

1. 在 [`Streamlit Could`](https://share.streamlit.io/) 获取一个免费的 API Key。
2. 克隆本仓库
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. 在 `Streamlit Could` 中填写你的 API
   ```js
   const API_KEY = '填写你的 API';
   ```




<!-- 使用方法 示例 -->
## 使用方法

在这里你可以展示项目的使用方法。把附加的截图、代码示例和演示放在这里也很不错。你也可以用链接引用其他资源。

_转到 [文档](https://example.com) 查看更多示例_





<!-- 路线图 -->
## 项目更新

- [x] 添加更新日志
- [x] 使用 Radom Frost 进行模型训练
- [x] 使用Streamlit进行数据可视化
- [X] 使用Streamlit Cloud进行服务器部署
- [ ] 进一步优化可视化界面
    - [x] 增加侧边栏控件
    - [x] 增加开屏动画
    - [ ] 增加多种数据展示图样
- [ ] 优化模型超参数


到 [open issues](https://github.com/admin1025/WeatherNow/issues) 页查看所有请求的功能 （以及已知的问题）。



<!-- 贡献 -->
## 贡献

贡献让开源社区成为了一个非常适合学习、启发和创新的地方。你所做出的任何贡献都是**受人尊敬**的。

如果你有好的建议，请复刻（fork）本仓库并且创建一个拉取请求（pull request）。你也可以简单地创建一个议题（issue），并且添加标签「enhancement」。不要忘记给项目点一个 star！再次感谢！

1. 复刻（Fork）本项目
2. 创建你的 Feature 分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的变更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到该分支 (`git push origin feature/AmazingFeature`)
5. 创建一个拉取请求（Pull Request）


<!-- 许可证 -->
## 许可证

根据 MIT 许可证分发。打开 [LICENSE.txt](LICENSE.txt) 查看更多内容。




tian5784879@gmail.com
<!-- 联系我们 -->
## 联系我们
<div align=center>@author:R  
<div align=center><img src="https://workspace.google.com/lp/static/images/logo-gmail.png?fingerprint=c2eaf4aae389c3f885e97081bb197b97" alt="tian5784879@gmail.com"  width="15" height="15">tian5784879@gmail.com</div>

项目链接: [https://github.com/admin1025/WeatherNow](https://github.com/admin1025/WeatherNow)
</div>



<!-- 致谢 -->
## 致谢

这个项目的可视化界面的大部分组件主要来源于[Streamlit Gallery](https://streamlit.io/gallery),感谢为开源做出贡献的作者。

* [GW Quickview](https://gw-quickview.streamlit.app/)
* [30Day of Streamlit](https://30days.streamlit.app/)


<p align="right">(<a href="#top">返回顶部</a>)</p>



<!-- MARKDOWN 链接 & 图片 -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/BreakingAwful/Best-README-Template-zh.svg?style=for-the-badge
[contributors-url]: https://github.com/BreakingAwful/Best-README-Template-zh/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/BreakingAwful/Best-README-Template-zh.svg?style=for-the-badge
[forks-url]: https://github.com/BreakingAwful/Best-README-Template-zh/network/members
[stars-shield]: https://img.shields.io/github/stars/BreakingAwful/Best-README-Template-zh.svg?style=for-the-badge
[stars-url]: https://github.com/BreakingAwful/Best-README-Template-zh/stargazers
[issues-shield]: https://img.shields.io/github/issues/BreakingAwful/Best-README-Template-zh.svg?style=for-the-badge
[issues-url]: https://github.com/BreakingAwful/Best-README-Template-zh/issues
[license-shield]: https://img.shields.io/github/license/BreakingAwful/Best-README-Template-zh.svg?style=for-the-badge
[license-url]: https://github.com/BreakingAwful/Best-README-Template-zh/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png