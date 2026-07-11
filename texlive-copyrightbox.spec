%global tl_name copyrightbox
%global tl_revision 24829

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Provide copyright notices for images in a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/copyrightbox
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/copyrightbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/copyrightbox.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package command \copyrightbox[<placement>]{<image command>}{<text>},
which places the text as a copyright notice relating to the matter
created by the image command.

