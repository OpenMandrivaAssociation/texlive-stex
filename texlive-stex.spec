Name:		texlive-stex
Version:	20190321
Release:	1
Summary:	An Infrastructure for Semantic Preloading of LaTeX Documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The sTeX package collection is a version of TeX/LaTeX that
allows to markup TeX/LaTeX documents semantically without
leaving the document format, essentially turning it into a
document format for mathematical knowledge management (MKM).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/stex
%doc %{_texmfdistdir}/doc/latex/stex
#- source
%doc %{_texmfdistdir}/source/latex/stex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
