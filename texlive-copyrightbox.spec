# revision 24829
# category Package
# catalog-ctan /macros/latex/contrib/copyrightbox
# catalog-date 2011-12-11 19:15:48 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-copyrightbox
Version:	0.1
Release:	2
Summary:	Provide copyright notices for images in a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/copyrightbox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/copyrightbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/copyrightbox.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package command \copyrightbox[<placement>]{<image
command>}{<text>}, which places the text as a copyright notice
relating to the matter created by the image command.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/copyrightbox/copyrightbox.sty
%doc %{_texmfdistdir}/doc/latex/copyrightbox/README
%doc %{_texmfdistdir}/doc/latex/copyrightbox/coin.jpg
%doc %{_texmfdistdir}/doc/latex/copyrightbox/copyrightbox.pdf
%doc %{_texmfdistdir}/doc/latex/copyrightbox/copyrightbox.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
