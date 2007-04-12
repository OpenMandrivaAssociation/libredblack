%define	major 0
%define libname	%mklibname redblack %{major}

Summary:	Library for handling red-black tree searching algorithm
Name:		libredblack
Version:	1.3
Release:	%mkrel 4
Group:		System/Libraries
License:	GPL
URL:		http://libredblack.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	python-devel
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description 
This implements the redblack balanced tree algorithm.

%package -n	%{libname}
Summary:	Library for handling red-black tree searching algorithm
Group:          System/Libraries

%description -n	%{libname}
This implements the redblack balanced tree algorithm.

%package -n	%{libname}-devel
Summary:	Libraries and header files for the %{libname} library
Group:		Development/C
Provides:	%{libname}-devel = %{version}
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
To develop programs based upon the libredblack library, the system needs to 
have these header and object files available for creating the executables.

%prep

%setup -q -n %{name}-%{version}

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc example*.c example*.rb
%{_bindir}/rbgen
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_datadir}/libredblack


