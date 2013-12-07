# revision 29803
# category Package
# catalog-ctan /macros/latex/contrib/stex
# catalog-date 2012-03-31 11:15:31 +0200
# catalog-license lppl
# catalog-version 1.4
Name:		texlive-stex
Version:	1.4
Release:	3
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
%{_texmfdistdir}/tex/latex/stex/cmath/cmath.sty
%{_texmfdistdir}/tex/latex/stex/cmath/cmath.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/cmathml/cmathml.sty
%{_texmfdistdir}/tex/latex/stex/cmathml/cmathml.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/cmathml/cmathmlx.sty
%{_texmfdistdir}/tex/latex/stex/cmathml/cmathmlx.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/cnx/cnx.cls
%{_texmfdistdir}/tex/latex/stex/cnx/cnx.cls.ltxml
%{_texmfdistdir}/tex/latex/stex/ctansvn.sty
%{_texmfdistdir}/tex/latex/stex/dcm/dcm.sty
%{_texmfdistdir}/tex/latex/stex/dcm/dcm.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/hwexam/hwexam.cls
%{_texmfdistdir}/tex/latex/stex/hwexam/hwexam.cls.ltxml
%{_texmfdistdir}/tex/latex/stex/hwexam/hwexam.sty
%{_texmfdistdir}/tex/latex/stex/hwexam/hwexam.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/metakeys/metakeys.sty
%{_texmfdistdir}/tex/latex/stex/metakeys/metakeys.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/mikoslides/beamerthemeJacobs.sty
%{_texmfdistdir}/tex/latex/stex/mikoslides/cc-by-sa.png
%{_texmfdistdir}/tex/latex/stex/mikoslides/cc_somerights.png
%{_texmfdistdir}/tex/latex/stex/mikoslides/dangerous-bend.png
%{_texmfdistdir}/tex/latex/stex/mikoslides/jacobs-logo.png
%{_texmfdistdir}/tex/latex/stex/mikoslides/mikoaffiliation.sty
%{_texmfdistdir}/tex/latex/stex/mikoslides/mikoaffiliation.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/mikoslides/mikoslides.cls
%{_texmfdistdir}/tex/latex/stex/mikoslides/mikoslides.cls.ltxml
%{_texmfdistdir}/tex/latex/stex/mikoslides/shading-l2r.png
%{_texmfdistdir}/tex/latex/stex/modules/modules.sty
%{_texmfdistdir}/tex/latex/stex/modules/modules.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/omdoc/omdoc.cls
%{_texmfdistdir}/tex/latex/stex/omdoc/omdoc.cls.ltxml
%{_texmfdistdir}/tex/latex/stex/omdoc/omdoc.sty
%{_texmfdistdir}/tex/latex/stex/omdoc/omdoc.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/omtext/omtext.sty
%{_texmfdistdir}/tex/latex/stex/omtext/omtext.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/presentation/presentation.sty
%{_texmfdistdir}/tex/latex/stex/presentation/presentation.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/problem/problem.sty
%{_texmfdistdir}/tex/latex/stex/problem/problem.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/rdfmeta/rdfmeta.sty
%{_texmfdistdir}/tex/latex/stex/rdfmeta/rdfmeta.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/reqdoc/reqdoc.sty
%{_texmfdistdir}/tex/latex/stex/reqdoc/reqdoc.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/sproof/sproof.sty
%{_texmfdistdir}/tex/latex/stex/sproof/sproof.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/sref/sref.sty
%{_texmfdistdir}/tex/latex/stex/sref/sref.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/statements/statements.sty
%{_texmfdistdir}/tex/latex/stex/statements/statements.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/stex-logo.sty
%{_texmfdistdir}/tex/latex/stex/stex-logo.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/stex.sty
%{_texmfdistdir}/tex/latex/stex/stex.sty.ltxml
%{_texmfdistdir}/tex/latex/stex/stex.tex
%{_texmfdistdir}/tex/latex/stex/workaddress/workaddress.sty
%{_texmfdistdir}/tex/latex/stex/workaddress/workaddress.sty.ltxml
%doc %{_texmfdistdir}/doc/latex/stex/README
%doc %{_texmfdistdir}/doc/latex/stex/cmath/README
%doc %{_texmfdistdir}/doc/latex/stex/cmath/cmath.pdf
%doc %{_texmfdistdir}/doc/latex/stex/cmathml/README
%doc %{_texmfdistdir}/doc/latex/stex/cmathml/cmathml.pdf
%doc %{_texmfdistdir}/doc/latex/stex/cnx/README
%doc %{_texmfdistdir}/doc/latex/stex/cnx/cnx.pdf
%doc %{_texmfdistdir}/doc/latex/stex/dcm/README
%doc %{_texmfdistdir}/doc/latex/stex/dcm/dcm.pdf
%doc %{_texmfdistdir}/doc/latex/stex/example/Makefile
%doc %{_texmfdistdir}/doc/latex/stex/example/README
%doc %{_texmfdistdir}/doc/latex/stex/example/background/Makefile
%doc %{_texmfdistdir}/doc/latex/stex/example/background/all.omdoc
%doc %{_texmfdistdir}/doc/latex/stex/example/background/all.tex
%doc %{_texmfdistdir}/doc/latex/stex/example/background/functions.omdoc
%doc %{_texmfdistdir}/doc/latex/stex/example/background/functions.sms
%doc %{_texmfdistdir}/doc/latex/stex/example/background/functions.tex
%doc %{_texmfdistdir}/doc/latex/stex/example/background/post.tex
%doc %{_texmfdistdir}/doc/latex/stex/example/background/pre.tex
%doc %{_texmfdistdir}/doc/latex/stex/example/background/reals.omdoc
%doc %{_texmfdistdir}/doc/latex/stex/example/background/reals.sms
%doc %{_texmfdistdir}/doc/latex/stex/example/background/reals.tex
%doc %{_texmfdistdir}/doc/latex/stex/example/paper/Makefile
%doc %{_texmfdistdir}/doc/latex/stex/example/paper/continuous.omdoc
%doc %{_texmfdistdir}/doc/latex/stex/example/paper/continuous.sms
%doc %{_texmfdistdir}/doc/latex/stex/example/paper/continuous.tex
%doc %{_texmfdistdir}/doc/latex/stex/example/paper/differentiable.omdoc
%doc %{_texmfdistdir}/doc/latex/stex/example/paper/differentiable.sms
%doc %{_texmfdistdir}/doc/latex/stex/example/paper/differentiable.tex
%doc %{_texmfdistdir}/doc/latex/stex/example/paper/intro.omdoc
%doc %{_texmfdistdir}/doc/latex/stex/example/paper/intro.sms
%doc %{_texmfdistdir}/doc/latex/stex/example/paper/intro.tex
%doc %{_texmfdistdir}/doc/latex/stex/example/paper/paper.omdoc
%doc %{_texmfdistdir}/doc/latex/stex/example/paper/paper.pdf
%doc %{_texmfdistdir}/doc/latex/stex/example/paper/paper.tex
%doc %{_texmfdistdir}/doc/latex/stex/example/test/Makefile
%doc %{_texmfdistdir}/doc/latex/stex/hwexam/README
%doc %{_texmfdistdir}/doc/latex/stex/hwexam/hwexam.pdf
%doc %{_texmfdistdir}/doc/latex/stex/metakeys/README
%doc %{_texmfdistdir}/doc/latex/stex/metakeys/metakeys.pdf
%doc %{_texmfdistdir}/doc/latex/stex/mikoslides/README
%doc %{_texmfdistdir}/doc/latex/stex/mikoslides/mikoslides.pdf
%doc %{_texmfdistdir}/doc/latex/stex/modules/README
%doc %{_texmfdistdir}/doc/latex/stex/modules/modules.pdf
%doc %{_texmfdistdir}/doc/latex/stex/omdoc/README
%doc %{_texmfdistdir}/doc/latex/stex/omdoc/omdoc.pdf
%doc %{_texmfdistdir}/doc/latex/stex/omtext/README
%doc %{_texmfdistdir}/doc/latex/stex/omtext/omtext.pdf
%doc %{_texmfdistdir}/doc/latex/stex/presentation/README
%doc %{_texmfdistdir}/doc/latex/stex/presentation/presentation.pdf
%doc %{_texmfdistdir}/doc/latex/stex/problem/README
%doc %{_texmfdistdir}/doc/latex/stex/problem/problem.pdf
%doc %{_texmfdistdir}/doc/latex/stex/rdfmeta/README
%doc %{_texmfdistdir}/doc/latex/stex/rdfmeta/certification.pdf
%doc %{_texmfdistdir}/doc/latex/stex/rdfmeta/certification.tex
%doc %{_texmfdistdir}/doc/latex/stex/rdfmeta/rdfmeta.pdf
%doc %{_texmfdistdir}/doc/latex/stex/reqdoc/README
%doc %{_texmfdistdir}/doc/latex/stex/reqdoc/reqdoc.pdf
%doc %{_texmfdistdir}/doc/latex/stex/reqdoc/requirements.pdf
%doc %{_texmfdistdir}/doc/latex/stex/reqdoc/requirements.tex
%doc %{_texmfdistdir}/doc/latex/stex/sproof/README
%doc %{_texmfdistdir}/doc/latex/stex/sproof/sproof.pdf
%doc %{_texmfdistdir}/doc/latex/stex/sref/README
%doc %{_texmfdistdir}/doc/latex/stex/sref/book.pdf
%doc %{_texmfdistdir}/doc/latex/stex/sref/book.tex
%doc %{_texmfdistdir}/doc/latex/stex/sref/idc.pdf
%doc %{_texmfdistdir}/doc/latex/stex/sref/idc.tex
%doc %{_texmfdistdir}/doc/latex/stex/sref/idcmain.tex
%doc %{_texmfdistdir}/doc/latex/stex/sref/scr.pdf
%doc %{_texmfdistdir}/doc/latex/stex/sref/scr.tex
%doc %{_texmfdistdir}/doc/latex/stex/sref/scrmain.tex
%doc %{_texmfdistdir}/doc/latex/stex/sref/sref.pdf
%doc %{_texmfdistdir}/doc/latex/stex/statements/README
%doc %{_texmfdistdir}/doc/latex/stex/statements/statements.pdf
%doc %{_texmfdistdir}/doc/latex/stex/stex.pdf
%doc %{_texmfdistdir}/doc/latex/stex/workaddress/README
%doc %{_texmfdistdir}/doc/latex/stex/workaddress/workaddress.pdf
#- source
%doc %{_texmfdistdir}/source/latex/stex/bin/Makefile
%doc %{_texmfdistdir}/source/latex/stex/bin/Modparse.pm
%doc %{_texmfdistdir}/source/latex/stex/bin/README
%doc %{_texmfdistdir}/source/latex/stex/bin/TexId.pm
%doc %{_texmfdistdir}/source/latex/stex/bin/allgen
%doc %{_texmfdistdir}/source/latex/stex/bin/bms
%doc %{_texmfdistdir}/source/latex/stex/bin/checksum
%doc %{_texmfdistdir}/source/latex/stex/bin/convert-paths
%doc %{_texmfdistdir}/source/latex/stex/bin/filedate
%doc %{_texmfdistdir}/source/latex/stex/bin/gen-symdef-table.pl
%doc %{_texmfdistdir}/source/latex/stex/bin/grep-rerun
%doc %{_texmfdistdir}/source/latex/stex/bin/idcheck
%doc %{_texmfdistdir}/source/latex/stex/bin/msplit
%doc %{_texmfdistdir}/source/latex/stex/bin/old/Makefile
%doc %{_texmfdistdir}/source/latex/stex/bin/old/defcon.l
%doc %{_texmfdistdir}/source/latex/stex/bin/old/idcheck.l
%doc %{_texmfdistdir}/source/latex/stex/bin/old/modstr.l
%doc %{_texmfdistdir}/source/latex/stex/bin/old/symdef
%doc %{_texmfdistdir}/source/latex/stex/bin/rf
%doc %{_texmfdistdir}/source/latex/stex/bin/rng2dot/ModelRNC.pm
%doc %{_texmfdistdir}/source/latex/stex/bin/rng2dot/rng2dot
%doc %{_texmfdistdir}/source/latex/stex/bin/sgraph
%doc %{_texmfdistdir}/source/latex/stex/bin/sms
%doc %{_texmfdistdir}/source/latex/stex/bin/stexml
%doc %{_texmfdistdir}/source/latex/stex/bin/stexmlmod
%doc %{_texmfdistdir}/source/latex/stex/bin/termin
%doc %{_texmfdistdir}/source/latex/stex/cmath/cmath.dtx
%doc %{_texmfdistdir}/source/latex/stex/cmath/cmath.ins
%doc %{_texmfdistdir}/source/latex/stex/cmathml/cmathml.dtx
%doc %{_texmfdistdir}/source/latex/stex/cmathml/cmathml.ins
%doc %{_texmfdistdir}/source/latex/stex/cnx/cnx.dtx
%doc %{_texmfdistdir}/source/latex/stex/cnx/cnx.ins
%doc %{_texmfdistdir}/source/latex/stex/dcm/dcm.dtx
%doc %{_texmfdistdir}/source/latex/stex/dcm/dcm.ins
%doc %{_texmfdistdir}/source/latex/stex/hwexam/hwexam.dtx
%doc %{_texmfdistdir}/source/latex/stex/hwexam/hwexam.ins
%doc %{_texmfdistdir}/source/latex/stex/make/Makefile
%doc %{_texmfdistdir}/source/latex/stex/make/Makefile.base.in
%doc %{_texmfdistdir}/source/latex/stex/make/Makefile.base.vars
%doc %{_texmfdistdir}/source/latex/stex/make/Makefile.in
%doc %{_texmfdistdir}/source/latex/stex/make/Makefile.latex.in
%doc %{_texmfdistdir}/source/latex/stex/make/Makefile.latex.vars
%doc %{_texmfdistdir}/source/latex/stex/make/Makefile.latexml.in
%doc %{_texmfdistdir}/source/latex/stex/make/Makefile.latexml.vars
%doc %{_texmfdistdir}/source/latex/stex/make/Makefile.subdirs
%doc %{_texmfdistdir}/source/latex/stex/make/Makefile.vars
%doc %{_texmfdistdir}/source/latex/stex/make/README
%doc %{_texmfdistdir}/source/latex/stex/metakeys/metakeys.dtx
%doc %{_texmfdistdir}/source/latex/stex/metakeys/metakeys.ins
%doc %{_texmfdistdir}/source/latex/stex/mikoslides/mikoslides.dtx
%doc %{_texmfdistdir}/source/latex/stex/mikoslides/mikoslides.ins
%doc %{_texmfdistdir}/source/latex/stex/modules/modules.dtx
%doc %{_texmfdistdir}/source/latex/stex/modules/modules.ins
%doc %{_texmfdistdir}/source/latex/stex/omdoc/omdoc.dtx
%doc %{_texmfdistdir}/source/latex/stex/omdoc/omdoc.ins
%doc %{_texmfdistdir}/source/latex/stex/omtext/omtext.dtx
%doc %{_texmfdistdir}/source/latex/stex/omtext/omtext.ins
%doc %{_texmfdistdir}/source/latex/stex/presentation/presentation.dtx
%doc %{_texmfdistdir}/source/latex/stex/presentation/presentation.ins
%doc %{_texmfdistdir}/source/latex/stex/problem/problem.dtx
%doc %{_texmfdistdir}/source/latex/stex/problem/problem.ins
%doc %{_texmfdistdir}/source/latex/stex/rdfmeta/rdfmeta.dtx
%doc %{_texmfdistdir}/source/latex/stex/rdfmeta/rdfmeta.ins
%doc %{_texmfdistdir}/source/latex/stex/reqdoc/reqdoc.dtx
%doc %{_texmfdistdir}/source/latex/stex/reqdoc/reqdoc.ins
%doc %{_texmfdistdir}/source/latex/stex/schema/Makefile
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML-bib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML-bib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML-block.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML-block.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML-common.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML-common.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML-inline.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML-inline.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML-math.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML-math.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML-para.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML-para.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML-picture.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML-picture.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML-structure.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML-structure.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML-tabular.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML-tabular.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/LaTeXML.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-animation.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-animation.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-animevents-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-animevents-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-basic-clip.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-basic-clip.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-basic-filter.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-basic-filter.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-basic-font.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-basic-font.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-basic-graphics-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-basic-graphics-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-basic-structure.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-basic-structure.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-basic-text.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-basic-text.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-clip.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-clip.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-conditional.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-conditional.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-container-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-container-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-core-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-core-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-cursor.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-cursor.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-datatypes.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-datatypes.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-docevents-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-docevents-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-extensibility.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-extensibility.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-extresources-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-extresources-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-filter.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-filter.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-font.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-font.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-gradient.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-gradient.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-graphevents-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-graphevents-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-graphics-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-graphics-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-hyperlink.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-hyperlink.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-image.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-image.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-marker.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-marker.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-mask.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-mask.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-opacity-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-opacity-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-paint-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-paint-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-pattern.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-pattern.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-profile.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-profile.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-qname.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-script.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-script.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-shape.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-shape.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-structure.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-structure.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-style.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-style.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-text.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-text.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-view.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-view.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-viewport-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-viewport-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-xlink-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg-xlink-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg11-basic.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg11-tiny.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg11.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/LaTeXML/svg11.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/Makefile
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/metadata.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc+ltxml.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/MARCRelators.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/Makefile
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/README
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/arith1.omdoc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/creativecommons.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/dublincore.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/mathml3-common.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/mathml3-content.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/mathml3-presentation.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/mathml3-strict-content.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/mathml3-strict.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/mathml3.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/mocksoap.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omcd2.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omcdgroup2.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omcdsig2.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omdoc-common.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omdoc.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omdocadt.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omdoccc.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omdoccth.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omdocdc.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omdocdg.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omdocdoc.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omdocext.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omdocmeta.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omdocmobj.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omdocmtxt.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omdocpf.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omdocphys.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omdocpres.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omdocquiz.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omdocrt.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/omdocst.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/openmath2.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/pxhtml.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/schemas.xml
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/todo
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/todo.txt
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/xhtml-applet.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/xhtml-attribs.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/xhtml-basic-table.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/xhtml-bdo.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/xhtml-datatypes.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/xhtml-hypertext.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/xhtml-image.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/xhtml-inlstyle.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/xhtml-list.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/xhtml-object.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/xhtml-param.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/xhtml-table.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/omdoc/xhtml-text.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/owl.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/owl2+ltxml.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/owl2-xml.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/owl2xml.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/schemas.xml
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/statements.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-animation.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-animevents-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-basic-clip.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-basic-filter.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-basic-font.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-basic-graphics-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-basic-structure.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-basic-text.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-clip.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-conditional.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-container-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-core-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-cursor.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-datatypes.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-docevents-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-extensibility.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-extresources-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-filter.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-font.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-gradient.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-graphevents-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-graphics-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-hyperlink.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-image.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-marker.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-mask.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-opacity-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-paint-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-pattern.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-profile.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-qname.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-script.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-shape.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-structure.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-style.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-text.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-view.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-viewport-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg-xlink-attrib.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg11-basic.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg11-tiny.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rnc/svg/svg11.rnc
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/LaTeXML-bib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/LaTeXML-block.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/LaTeXML-common.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/LaTeXML-inline.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/LaTeXML-math.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/LaTeXML-para.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/LaTeXML-picture.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/LaTeXML-structure.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/LaTeXML-tabular.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/LaTeXML.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/MARCRelators.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/Makefile
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/creativecommons.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/dublincore.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/mathml3-cds-pragmatic.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/mathml3-common.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/mathml3-content.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/mathml3-pragmatic.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/mathml3-presentation.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/mathml3-strict-content.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/mathml3-strict.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/mathml3.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/metadata.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdoc+ltxml.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdoc-common.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdoc-xhtml.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdoc.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdocadt.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdocattribs.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdoccc.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdoccth.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdocdc.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdocdg.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdocdoc.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdocext.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdocmeta.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdocmobj.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdocmtxt.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdocpf.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdocpres.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdocquiz.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdocrt.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/omdocst.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/openmath2.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/openmath3.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/owl.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/owl2+ltxml.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/owl2-xml.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/owl2xml.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/pxhtml.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/statements.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-animation.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-animevents-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-basic-clip.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-basic-filter.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-basic-font.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-basic-graphics-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-basic-structure.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-basic-text.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-clip.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-conditional.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-container-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-core-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-cursor.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-datatypes.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-docevents-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-extensibility.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-extresources-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-filter.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-font.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-gradient.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-graphevents-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-graphics-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-hyperlink.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-image.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-marker.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-mask.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-opacity-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-paint-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-pattern.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-profile.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-script.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-shape.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-structure.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-style.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-text.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-view.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-viewport-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg-xlink-attrib.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/svg11.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/xhtml-applet.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/xhtml-attribs.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/xhtml-base.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/xhtml-basic-table.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/xhtml-bdo.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/xhtml-datatypes.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/xhtml-hypertext.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/xhtml-image.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/xhtml-inlstyle.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/xhtml-link.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/xhtml-list.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/xhtml-object.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/xhtml-param.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/xhtml-table.rng
%doc %{_texmfdistdir}/source/latex/stex/schema/rng/xhtml-text.rng
%doc %{_texmfdistdir}/source/latex/stex/sproof/sproof.dtx
%doc %{_texmfdistdir}/source/latex/stex/sproof/sproof.ins
%doc %{_texmfdistdir}/source/latex/stex/sref/sref.dtx
%doc %{_texmfdistdir}/source/latex/stex/sref/sref.ins
%doc %{_texmfdistdir}/source/latex/stex/statements/statements.dtx
%doc %{_texmfdistdir}/source/latex/stex/statements/statements.ins
%doc %{_texmfdistdir}/source/latex/stex/workaddress/workaddress.dtx
%doc %{_texmfdistdir}/source/latex/stex/workaddress/workaddress.ins
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-bib-xhtml.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-block-xhtml.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-common.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-html.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-html5.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-inline-xhtml.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-math-image.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-math-mathml-html5.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-math-mathml.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-para-html5.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-para-xhtml.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-picture-image.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-picture-svg-html5.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-picture-svg.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-structure-html5.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-structure-xhtml.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-tabular-xhtml.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-webpage-html5.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-webpage-xhtml.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/LaTeXML-xhtml.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/amsart.css
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/closedbib.css
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/core.css
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/marginpar.css
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/navbar-left.css
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/navbar-right.css
%doc %{_texmfdistdir}/source/latex/stex/xsl/LaTeXML/theme-blue.css
%doc %{_texmfdistdir}/source/latex/stex/xsl/Makefile
%doc %{_texmfdistdir}/source/latex/stex/xsl/doc.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/graphics.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/listings.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/ltxml2cnx.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/math.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/notations.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/omdocpost.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/owl2post.xsl
%doc %{_texmfdistdir}/source/latex/stex/xsl/symbols.xsl

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
