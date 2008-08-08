%define module	MARC-Charset
%define name	perl-%{module}
%define version 1.0
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Convert MARC-8 encoded strings to UTF-8
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/MARC/%{module}-%{version}.tar.bz2
Buildrequires:  perl(Class::Accessor)
Buildrequires:  perl(XML::SAX)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
MARC::Charset is a package to assist you in converting converting data encoded
using MARC-8 character sets to Unicode (UTF-8).

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/MARC
%{_mandir}/*/*

