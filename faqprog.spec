Summary:	A FAQ documentation compiler
Summary(pl.UTF-8):   Kompilator dokumentacji FAQ
Name:		faqprog
Version:	1.22
Release:	1
License:	Freeware
Group:		Applications/Publishing
Source0:	ftp://ftp.gnupg.org/pub/gcrypt/contrib/%{name}.pl
# Source0-md5:	a800102afcc7a5bf826088e6001f8aa6
Requires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
faqprog is a program converting raw FAQ files into text and HTML
format.

%description -l de.UTF-8
faqprog ist ein Programm, der konvertiert raue FAQ-Dateien ins Text-
und HTML-Format.

%description -l pl.UTF-8
faqprog jest programem konwertującym surowe pliki FAQ do formatu
tekstowego i HTML.

%prep
%setup -qcT
cp %{SOURCE0} .

%install
rm -rf $RPM_BUILD_ROOT
install -D faqprog.pl $RPM_BUILD_ROOT%{_bindir}/faqprog.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
