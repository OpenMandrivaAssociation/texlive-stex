%global tl_name stex
%global tl_revision 79507

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.1.0
Release:	%{tl_revision}.1
Summary:	An infrastructure for semantic preloading of LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/stex
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The sTeX package collection is a version of TeX/LaTeX that allows to
markup TeX/LaTeX documents semantically without leaving the document
format, essentially turning it into a document format for mathematical
knowledge management (MKM).

