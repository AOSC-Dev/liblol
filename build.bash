#!/bin/bash
set -euo pipefail

# Set language to C to prevent warnings in containers.
export LANG=C

if ! which sudo && \
   (( $EUID != 0 )); then
	echo "Please install sudo before continuing, or run this script as root!"
	exit 1
fi

echo ">>> Installing dependencies ..."
if (( $EUID != 0 )); then
	sudo apt install -y build-essential devscripts git
	sudo apt -y build-dep .
else
	apt install -y build-essential devscripts git
	apt build-dep -y .
fi

echo ">>> Creating original source archive ..."
git deborig --force $(git rev-parse HEAD)

echo ">>> Creating the Debian patch archive (.debian.tar.xz) ..."
dpkg-buildpackage -S -us -uc

echo ">>> Assembling sources for glibc, libxcrypt, and patchelf ..."
./debian/rules assemble-orig-source

echo ">>> Building libLoL ..."
dpkg-buildpackage -uc -us
