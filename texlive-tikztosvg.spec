Name:		texlive-tikztosvg
Version:	60289
Release:	1
Summary:	A utility for rendering TikZ diagrams to SVG
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikztosvg
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikztosvg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikztosvg.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a shell script that calls XeTeX and
pdf2svg to convert TikZ environments to SVG files.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/scripts/tikztosvg
%doc %{_texmfdistdir}/doc/support/tikztosvg
%doc %{_texmfdistdir}/doc/man/man1/*

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
