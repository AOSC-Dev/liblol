libLoL
======

简体中文自述文档请见[此处](README.zh.md)

libLoL (LoongArch on LoongArch) is a compatibility runtime for applications
designed for LoongArch's old-world ABI. By and large, these are applications
built for Loongson's Loongnix reference Linux distribution and UnionTech's
UOS, consisting mostly commercial applications designed for the mainland
Chinese market, such as:

- Tencent's QQ for Linux
- Kingsoft's WPS for Linux
- Loongson Browser (based on Chromium)

As these applications have not yet been ported to the new-world ABI, this
runtime is meant to provide help users of new-world Linux distributions use
the aforementioned applications.

For a brief introduction on old-world and new-world incompatibility, please
refer to [this essay](https://areweloongyet.com/docs/old-and-new-worlds/) (in
Chinese) from the Loongson Open Source Community's *Are We Loong Yet?* site.

Components
----------

libLoL consists of two components, one in the kernel-space and the other in
the user-space.

- Kernel: The [la_ow_syscall](https://github.com/AOSC-Dev/la_ow_syscall)
  modules provides support for old-world system call support in the Linux
  Kernel, making it possible to run old-world applications on new-world
  (upstream) kernels.
- User-space: A [patched Glibc](https://github.com/AOSC-Dev/glibc-loongarch-oldworld)
  provides symbol support for old-world applications - see the Autobuild
  building procedure in this repository. Additional runtime may be provided
  by the distribution or in binary form from [Loongnix](https://www.loongson.cn/system/loongnix).

Reporting Issues
----------------

Please use the [Issues](https://github.com/AOSC-Dev/liblol/issues) function
for reporting any developer or user issues (feel free to use English or
Chinese).

You are also welcome to report issues at AOSC's various
[chat groups](https://aosc.io/contact/).
