Name:       pod2pdf
Version:    0.42
Release:    3
License:    Artistic
Group:      Publishing
Summary:    Converts Pod to PDF format
Url:        http://perl.jonallen.info/projects/pod2pdf
Source:     http://perl.jonallen.info/attachment/24/pod2pdf-%{version}.tar.gz
Requires: perl(PDF::API2)
BuildRequires: perl-devel
BuildRequires: perl(PDF::API2)
BuildRequires: perl(Getopt::ArgvFile)
BuildArch: noarch

%description
Converts Pod to PDF format with extensions to include inline images.

%prep
%setup -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/pod2pdf
%{_mandir}/man1/pod2pdf.1*
%{perl_vendorlib}/App



%changelog
* Fri Aug 06 2010 Funda Wang <fwang@mandriva.org> 0.42-2mdv2011.0
+ Revision: 566712
- Add BR for test

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - fix dependencies
    - import pod2pdf


* Fri Aug 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.42-1mdv2011.0
- initial mdv release
