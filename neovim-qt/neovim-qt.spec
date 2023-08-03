%ifarch %{arm} %{ix86} x86_64 %{mips}
%bcond_without  tests
%else
%bcond_with     tests
%endif
# disable shared libraries to avoid building libneovim-qt-gui.so
# it's only needed for devel package which we're not providing
%undefine       _cmake_shared_libs
%undefine       _cmake_in_source_build

%define commit 1f73d6304f5db8669ff4da7990595e4b8d7925a0

Name:           neovim-qt
Version:        0.2.17^git%{commit}
Release:        1%{?dist}
Summary:        Qt GUI for Neovim

License:        ISC
URL:            https://github.com/equalsraf/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(msgpack)
BuildRequires:  neovim

Requires:       hicolor-icon-theme
Requires:       neovim

%description
%{summary}.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
%cmake \
    -DUSE_SYSTEM_MSGPACK:BOOL=ON  \
    -DENABLE_TESTS:BOOL=OFF
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/nvim-qt.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/nvim-qt
%{_datadir}/applications/nvim-qt.desktop
%{_datadir}/icons/hicolor/192x192/apps/nvim-qt.png
%{_datadir}/icons/hicolor/scalable/apps/nvim-qt.svg
%{_datadir}/nvim-qt/
