%define upstream_name    MARC-Charset
%define upstream_version 1.33

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:	Convert MARC-8 encoded strings to UTF-8
License:	GPL or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MARC/%{upstream_name}-%{upstream_version}.tar.gz
Buildrequires:  perl(Class::Accessor)
Buildrequires:  perl(XML::SAX)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
MARC::Charset is a package to assist you in converting converting data encoded
using MARC-8 character sets to Unicode (UTF-8).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

