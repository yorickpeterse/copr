%global debug_package %{nil}

Name:    inko
Version: 0.11.0
Release: %autorelease
Summary: A language for building concurrent software with confidence
License: MPL-2.0
URL:     https://github.com/inko-lang/inko
Source:  https://github.com/inko-lang/inko/archive/refs/tags/v%{version}.tar.gz

BuildRequires: gcc make rust cargo llvm15 llvm15-devel llvm15-static libstdc++-devel libstdc++-static libffi-devel zlib-devel git
Requires: libgcc gcc

%description
Inko is a language for building concurrent software with confidence. Inko makes
it easy to build concurrent software, without having to worry about
unpredictable performance, unexpected runtime errors, or race conditions.

%files -n %{name}
%{_bindir}/inko
%{_datadir}/*
%{_prefix}/lib/%{name}/*

%prep
%autosetup -n %{name}-%{version_no_tilde} -p0

%build
make build

%install
make install DESTDIR=%{buildroot}

%changelog
%autochangelog
