Summary:	Startup Notification Library
Name:		startup-notification
Version:	0.4
Release:	1
Group:		Libraries
License:	LGPL
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.4/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Startup Notification Library.

%package devel
Summary:	Startup Notification Library development files
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Startup Notification Library development files.

%package static
Summary:	Static Startup Notification Library library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Startup Notification Library library.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
