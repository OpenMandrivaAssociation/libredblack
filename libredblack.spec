%define	major 0
%define libname %mklibname redblack %{major}
%define develname %mklibname redblack -d

Summary:	Library for handling red-black tree searching algorithm
Name:		libredblack
Version:	1.3
Release:	12
Group:		System/Libraries
License:	LGPLv2+
URL:		http://libredblack.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		libredblack-typo.diff

%description 
This implements the redblack balanced tree algorithm.

%package -n	%{libname}
Summary:	Library for handling red-black tree searching algorithm
Group:          System/Libraries

%description -n	%{libname}
This implements the redblack balanced tree algorithm.

%package -n	%{develname}
Summary:	Libraries and header files for the %{libname} library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{mklibname redblack 0 -d}

%description -n	%{develname}
To develop programs based upon the libredblack library, the system needs to 
have these header and object files available for creating the executables.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS ChangeLog README
%{_libdir}/*.so.*

%files -n %{develname}
%doc example*.c example*.rb
%{_bindir}/rbgen
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_datadir}/libredblack


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3-10mdv2011.0
+ Revision: 620221
- the mass rebuild of 2010.0 packages

* Sun Sep 13 2009 Thierry Vignaud <tv@mandriva.org> 1.3-9mdv2010.0
+ Revision: 438733
- rebuild

* Wed Mar 25 2009 Funda Wang <fwang@mandriva.org> 1.3-8mdv2009.1
+ Revision: 360977
- fix license

* Fri Jul 11 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3-7mdv2009.0
+ Revision: 233731
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.3-6mdv2008.1
+ Revision: 140928
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 01 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3-6mdv2008.0
+ Revision: 94143
- rebuilt due to missing packages

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3-5mdv2008.0
+ Revision: 83667
- fix typo (P0)
- new devel naming


* Fri Nov 17 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3-4mdv2007.0
+ Revision: 85291
- Import libredblack

* Fri Nov 17 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3-4mdv2007.1
- rebuild

* Sat Sep 03 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3-3mdk
- rebuilt due new rpm

* Sat Jun 04 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3-2mdk
- rebuild

* Mon May 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.3-1mdk
- 1.3
- merge the static-devel sub package into the devel sub package
- use macros
- the major changed from 1 to 0 (!)

