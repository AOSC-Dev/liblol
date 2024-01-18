libLoL
======

libLoL (LoongArch on LoongArch) 是一款用于提供旧世界 ABI 兼容性的运行时。旧世界 ABI 常用于为龙芯官方的 Loongnix 参考发行和统信 UOS 设计的商业软件，如：

- 腾讯 QQ Linux 版
- 金山 WPS for Linux
- 龙芯浏览器（基于 Chromium）

由于这些应用程序尚未移植到新世界 ABI 上，本运行时旨在为新世界发行版用户提供运行上述应用程序的便利。欲知有关新旧世界应用不兼容来由的相关信息，请见龙芯开源社区《咱龙了吗？》站点的[《新世界与旧世界》](https://areweloongyet.com/docs/old-and-new-worlds/)一文。

组件
----

libLoL 由内核空间和用户空间两个组件组成：

- 内核部分：通过 [la_ow_syscall](https://github.com/AOSC-Dev/la_ow_syscall) 模块，给 Linux 内核新增旧世界系统调用支持，进而使得新世界内核得以兼容旧世界运行时和应用程序
- 用户空间部分：给 [Glibc 打补丁](https://github.com/AOSC-Dev/glibc-loongarch-oldworld)以提供旧世界应用程序所需符号的兼容性。其余运行时库由发行版软件包或 [Loongnix](https://www.loongson.cn/system/loongnix) 的二进制软件包提供。

报告问题
--------

请使用本仓库的[工单系统](https://github.com/AOSC-Dev/liblol/issues) 报告有关开发和使用方面的问题。您也可以通过我社的[聊天群组](https://aosc.io/zh-cn/contact/)报告问题。
