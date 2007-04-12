%define module	MARC-Charset
%define name	perl-%{module}
%define version 0.95
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{module} module for perl
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp.perl.org/pub/CPAN/modules/by-module/MARC/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-root
Buildrequires:  perl(Class::Accessor)
Buildrequires:  perl(XML::SAX)

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

