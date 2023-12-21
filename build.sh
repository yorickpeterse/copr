#!/usr/bin/env bash

set -e

top="${PWD}/build"

if ! command -v spectool
then
    sudo dnf install rpmdevtools
fi

spectool --define "_topdir ${top}" -gR "${1}"

if [[ -d sources ]]
then
    cp -r sources/* "${top}/SOURCES"
fi

rpmbuild --define "_topdir ${top}" -bs "${1}"
mv "${top}"/SRPMS/*.src.rpm "${2}"
