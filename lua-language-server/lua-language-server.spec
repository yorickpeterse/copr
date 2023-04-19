%global debug_package %{nil}

Name:    lua-language-server
Version: 3.6.18
Release: 1%{dist}
Summary: A language server that offers Lua language support
License: MIT
URL:     https://github.com/LuaLS/lua-language-server
Source0: https://github.com/LuaLS/lua-language-server/releases/download/%{version}/lua-language-server-%{version}-submodules.zip
Source1: wrapper

BuildRequires: git
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: libstdc++-devel
BuildRequires: libstdc++-static

%description
A language server that offers Lua language support

%prep
%setup -q -c

%build
cd 3rd/luamake
./compile/install.sh
cd ../..
./3rd/luamake/luamake

%global optdir /opt/%{name}

%install
%{__install} -D -m 755 bin/lua-language-server %{buildroot}%{optdir}/bin/lua-language-server
%{__install} -D -m 644 bin/main.lua %{buildroot}%{optdir}/bin/main.lua
%{__install} -D -m 644 main.lua %{buildroot}%{optdir}/main.lua
%{__install} -D -m 664 debugger.lua %{buildroot}%{optdir}/debugger.lua
%{__install} -D -m 664 changelog.md %{buildroot}%{optdir}/changelog.md
cp -r locale meta script %{buildroot}%{optdir}
%{__install} -D -m 755 %{SOURCE1} %{buildroot}%{_bindir}/lua-language-server

%files
%license LICENSE
%doc README.md

%{optdir}
%{_bindir}/lua-language-server

%changelog
* Fri Mar 10 2023 Yorick Peterse <fedora@yorickpeterse.com> - 3.6.17-1
- Release 3.6.17
* Thu Mar 02 2023 Yorick Peterse <fedora@yorickpeterse.com> - 3.6.11-4
- Build from a zip archive that contains all submodules
* Wed Mar 01 2023 Yorick Peterse <git@yorickpeterse.com> 3.6.11-3
- Fix the patch for the header file (git@yorickpeterse.com)
* Wed Mar 01 2023 Yorick Peterse <git@yorickpeterse.com> 3.6.11-2
- Fix building on Fedora 38/Rawhide
- Include changelog.md so the --version flag reports the correct version
* Tue Feb 28 2023 Yorick Peterse <git@yorickpeterse.com> 3.6.11-1
- First release
