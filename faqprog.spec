Summary:	A FAQ documentation compiler
Summary(pl):	Kompilator dokumentacji FAQ
Name:		faqprog
Version:	1.22
Release:	1
License:	Freeware
Source0:	ftp://ftp.gnupg.org/pub/gcrypt/contrib/%{name}.pl
Group:		Applications/Publishing
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	perl

%description
faqprog is a program converting raw FAQ files into text and HTML
format.

%description -l de
faqprog ist ein Programm, der konvertiert raue FAQ-Dateien ins Text-
und HTML-Format.

%description -l pl
faqprog jest programem konwertuj±cym surowe pliki FAQ do formatu
tekstowego i HTML.

%prep
%setup -qcT
cp %{SOURCE0} .

%install
rm -rf $RPM_BUILD_ROOT
install -D faqprog.pl $RPM_BUILD_ROOT%{_bindir}/faqprog.pl

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT
