Version:        2.3.3
Release:        1%{?dist}
URL:            https://github.com/ryanoasis/nerd-fonts

%global foundry           Nerd Fonts
%global fontlicense       OFL
%global fontlicenses      LICENSE
%global fontdocsex        %{fontlicenses}

%global fontfamily        SourceCodePro Nerd Font
%global fontsummary       Monospaced font family for user interface and coding environments
%global fonts             *.ttf
%global fontconfs         %{SOURCE1}
%global fontdescription   %{expand:
Source Code Pro is a set of monospaced OpenType fonts that have been designed to
work well in coding environments. This family of fonts is a complementary design
to the Source Sans family. It is available in seven weights (Extralight, Light,
Regular, Medium, Semibold, Bold, Black).
}

Source0: https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/SourceCodePro.zip
Source1: 60-%{fontpkgname}.conf

%fontpkg

%prep
%autosetup -c
%{__rm} -vfr ./*Windows*.ttf

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog

* Mon Feb 27 2023 Yorick Peterse 2.3.3-1
- Initial package
