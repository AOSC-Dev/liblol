libLoL (for Debian)
===

To build libLoL for Debian, simply run:

```bash
./build.bash
```

Procedure Breakdown
---

Install compiler toolchain and build-time dependencies:

```bash
apt install build-essential devscripts git
apt build-dep .
```

Create a Debian original source archive.

```bash
git deborig $(git rev-parse HEAD)
```

Create the Debian patch archive (`.debian.tar.xz`):

```
dpkg-buildpackage -S -us -uc
```

Assemble sources for glibc, libxcrypt, and patchelf:

```
./debian/rules assemble-orig-source
```

Build the package:

```bash
dpkg-buildpackage -uc -us
```

About Sources
---

- `glibc` sources and patches are maintained at [AOSC-Tracking/glibc @ aosc/glibc-2.44-ow](https://github.com/AOSC-Tracking/glibc/tree/aosc/glibc-2.44-ow).
- Sources for `libxcrypt` and `patchelf` comes from Debian.
