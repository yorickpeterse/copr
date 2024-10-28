%global debug_package %{nil}

Name:    clogs
Version: 0.7.0
Release: 1%{?dist}
Summary: Generate a changelog from Git commits containing trailers
License: MPL-2.0
URL:     https://github.com/yorickpeterse/clogs
Source:  https://github.com/yorickpeterse/clogs/archive/refs/tags/v%{version}.tar.gz

BuildRequires: inko >= 0.17.0
Requires: git

%description
clogs is a tool for generating a Markdown changelog, populating the changelog from Git commits containing trailers.

%files -n %{name}
%{_bindir}/clogs
%{_datadir}/*

%prep
%autosetup -n %{name}-%{version_no_tilde} -p0

%build
make build

%install
%{__install} -D -m755 build/%{name} %{buildroot}%{_bindir}/%{name}
%{__install} -D -m644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE.md

%changelog
%autochangelog
