# AUTOGENERATED FILE from spec.main using genspec
VER=0.1.5~pre4
_mirror="http://pkg.loongnix.cn/loongnix"
__GLIBC_VER=2.39
__LIBXCRYPT_VER=4.4.36

SRCS="\
  file::rename=glibc.tar.xz::https://ftp.gnu.org/gnu/glibc/glibc-${__GLIBC_VER}.tar.xz \
  file::rename=patchelf.tar.gz::https://github.com/NixOS/patchelf/releases/download/0.18.0/patchelf-0.18.0.tar.gz \
  file::rename=libxcrypt.tar.xz::https://github.com/besser82/libxcrypt/releases/download/v${__LIBXCRYPT_VER}/libxcrypt-${__LIBXCRYPT_VER}.tar.xz \
"
CHKSUMS="\
  sha256::f77bd47cf8170c57365ae7bf86696c118adb3b120d3259c64c502d3dc1e2d926 \
  sha256::64de10e4c6b8b8379db7e87f58030f336ea747c0515f381132e810dbf84a86e7 \
  sha256::e5e1f4caee0a01de2aee26e3138807d6d3ca2b8e67287966d1fefd65e1fd8943 \
"
