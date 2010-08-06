Name:       pod2pdf
Version:    0.42
Release:    %mkrel 2
License:    Artistic
Group:      Publishing
Summary:    Converts Pod to PDF format
Url:        http://perl.jonallen.info/projects/pod2pdf
Source:     http://perl.jonallen.info/attachment/24/pod2pdf-%{version}.tar.gz
Requires: perl(PDF::API2)
BuildRequires: perl(PDF::API2)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/pod2pdf
%{_mandir}/man1/pod2pdf.1*
%{perl_vendorlib}/App

