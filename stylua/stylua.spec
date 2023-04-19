%global debug_package %{nil}

Name:    stylua
Version: 0.17.1
Release: %autorelease
Summary: An opinionated Lua code formatter
License: MPL-2.0
URL:     https://github.com/JohnnyMorganz/StyLua
Source:  https://github.com/JohnnyMorganz/StyLua/archive/refs/tags/v%{version}.tar.gz

BuildRequires: rust cargo

%description
An opinionated code formatter for Lua 5.1, 5.2, 5.3, 5.4 and Luau, built using
full-moon. StyLua is inspired by the likes of prettier, it parses your Lua
codebase, and prints it back out from scratch, enforcing a consistent code
style.

%files -n %{name}
%{_bindir}/stylua
%{_datadir}/*

%prep
%autosetup -n StyLua-%{version} -p0

%build
cargo build --release

%install
%{__install} -D -m755 target/release/%{name} %{buildroot}%{_bindir}/stylua
%{__install} -D -m644 LICENSE.md %{buildroot}%{_datadir}/licenses/%{name}/LICENSE.md

%changelog
%autochangelog
