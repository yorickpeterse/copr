Name:      colemak-dh-ortho
Version:   1.0.0
Release:   1%{?dist}
Summary:   The Colemak DH Ortholinear keyboard layout
BuildArch: noarch
License:   LicenseRef-Fedora-Public-Domain
Source0:   colemak_dh_ortho.map
Source1:   base.xml
Source2:   evdev.xml
Source3:   us

%description
The Colemak DH Ortholinear keyboard layout

%prep

%build

%install
%{__install} -D -m 644 %{SOURCE0} %{buildroot}/usr/lib/kbd/keymaps/xkb/colemak_dh_ortho.map
%{__install} -D -m 644 %{SOURCE1} %{buildroot}/etc/xkb/rules/base.xml
%{__install} -D -m 644 %{SOURCE2} %{buildroot}/etc/xkb/rules/evdev.xml
%{__install} -D -m 644 %{SOURCE3} %{buildroot}/etc/xkb/symbols/us

%files
/usr/lib/kbd/keymaps/xkb/colemak_dh_ortho.map
/etc/xkb/rules/base.xml
/etc/xkb/rules/evdev.xml
/etc/xkb/symbols/us
