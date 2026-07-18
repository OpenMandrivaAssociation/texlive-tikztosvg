%global tl_name tikztosvg
%global tl_revision 60289
%global tl_bin_links tikztosvg:%{_texmfdistdir}/scripts/tikztosvg/tikztosvg

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3.0
Release:	%{tl_revision}.1
Summary:	A utility for rendering TikZ diagrams to SVG
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/tikztosvg
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikztosvg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikztosvg.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(tikztosvg.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
This package provides a shell script that calls XeTeX and pdf2svg to
convert TikZ environments to SVG files.

