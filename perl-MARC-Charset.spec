%define upstream_name    MARC-Charset
%define upstream_version 1.34

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.34
Release:	1
Summary:	Convert MARC-8 encoded strings to UTF-8
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MARC/MARC-Charset-1.34.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(XML::SAX)
BuildArch:	noarch

%description
MARC::Charset is a package to assist you in converting converting data encoded
using MARC-8 character sets to Unicode (UTF-8).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/MARC
%{_mandir}/*/*

%changelog
* Mon Sep 05 2011 StÃ©phane TÃ©letchÃ©a <steletch@mandriva.org> 1.330.0-1mdv2012.0
+ Revision: 698311
- update to new version 1.33

* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.320.0-1
+ Revision: 688751
- update to new version 1.32

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.310.0-1mdv2011.0
+ Revision: 601984
- normalize perl version

* Fri Oct 22 2010 StÃ©phane TÃ©letchÃ©a <steletch@mandriva.org> 1.31-1mdv2011.0
+ Revision: 587323
- Update to 1.31

* Fri Jun 04 2010 StÃ©phane TÃ©letchÃ©a <steletch@mandriva.org> 1.2-1mdv2011.0
+ Revision: 547080
- Update to 1.2

* Wed Jul 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-1mdv2010.0
+ Revision: 391185
- update to new version 1.1

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.0-2mdv2009.0
+ Revision: 268541
- rebuild early 2009.0 package (before pixel changes)

* Wed May 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdv2009.0
+ Revision: 212215
- update to new version 1.0

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.98-1mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 08 2007 Funda Wang <fwang@mandriva.org> 0.98-1mdv2008.0
+ Revision: 60483
- New version 0.98

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.97-1mdv2008.0
+ Revision: 56109
- update to new version 0.97
- spec cleanup

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 0.96-1mdv2008.0
+ Revision: 20277
- 0.96


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.95-2mdk
- Fix According to perl Policy
	- BuildRequires 
	- Source URL

* Tue May 02 2006 Jerome Soyer <saispo@mandriva.org> 0.95-1mdk
- From Stéphane Téletchéa <steletch@free.fr>
- Initial Mandriva release


