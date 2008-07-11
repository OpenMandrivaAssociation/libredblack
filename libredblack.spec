%define	major 0
%define libname %mklibname redblack %{major}
%define develname %mklibname redblack -d

Summary:	Library for handling red-black tree searching algorithm
Name:		libredblack
Version:	1.3
Release:	%mkrel 7
Group:		System/Libraries
License:	GPL
URL:		http://libredblack.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		libredblack-typo.diff
BuildRequires:	python-devel
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Provides:	%{name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname redblack 0 -d}

%description -n	%{develname}
To develop programs based upon the libredblack library, the system needs to 
have these header and object files available for creating the executables.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0

%build

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_libdir}/*.so.*

%files -n %{develname}
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
