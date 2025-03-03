VER=0.1.9~pre1
__GLIBC_VER=2.41
__LIBXCRYPT_VER=4.4.38

SRCS="\
  file::rename=glibc.tar.xz::https://ftp.gnu.org/gnu/glibc/glibc-${__GLIBC_VER}.tar.xz \
  file::rename=patchelf.tar.gz::https://github.com/NixOS/patchelf/releases/download/0.18.0/patchelf-0.18.0.tar.gz \
  file::rename=libxcrypt.tar.xz::https://github.com/besser82/libxcrypt/releases/download/v${__LIBXCRYPT_VER}/libxcrypt-${__LIBXCRYPT_VER}.tar.xz \
"
CHKSUMS="\
  sha256::a5a26b22f545d6b7d7b3dd828e11e428f24f4fac43c934fb071b6a7d0828e901 \
  sha256::64de10e4c6b8b8379db7e87f58030f336ea747c0515f381132e810dbf84a86e7 \
  sha256::e5e1f4caee0a01de2aee26e3138807d6d3ca2b8e67287966d1fefd65e1fd8943 \
"
