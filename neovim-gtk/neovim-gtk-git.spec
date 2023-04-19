%global debug_package %{nil}

Name:    neovim-gtk-git
Version: {{{ git_dir_version }}}
Release: 1%{dist}
Summary: A GTK4 UI for NeoVim, written in Rust

License: GPLv3
URL:     https://github.com/Lyude/neovim-gtk
VCS:     {{{ git_dir_vcs }}}
Source:  {{{ git_dir_pack }}}

BuildRequires: rust cargo pkgconfig(gtk4)
Requires:      neovim glib2 gtk4 pango
Conflicts:     neovim-gtk

%description
A GTK4 UI for NeoVim, written in Rust. Originally this project started as a fork
of daa84's neovim-gtk project. There are a very large number of improvements
from daa84's version, including lots of bugfixes, using GTK4, smooth resizing,
and more.

%files -n %{name}
%{_bindir}/nvim-gtk
%{_datadir}/*

%prep
{{{ git_dir_setup_macro }}}

%build
cargo build --release

%install
%make_install PREFIX=/usr
%{__install} -D -m644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE
rm -f %{buildroot}/%{_prefix}/.crates.toml %{buildroot}/%{_prefix}/.crates2.json

%changelog
{{{ git_dir_changelog }}}
