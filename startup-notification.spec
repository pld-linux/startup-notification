Summary:	Startup Notification Library
Summary(pl.UTF-8):	Biblioteka Startup Notification
Name:		startup-notification
Version:	0.9
Release:	1
Group:		Libraries
License:	LGPL
Source0:	http://ftp.gnome.org/pub/gnome/sources/startup-notification/0.8/%{name}-%{version}.tar.bz2
# Source0-md5:	624b42f1fac5a12c543a079e2cd3b366
Patch0:		%{name}-link.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Startup Notification Library implements a mechanism allowing a
desktop environment to track application startup, to provide user
feedback and other features.

%description -l pl.UTF-8
Biblioteka Startup Notification jest implementacją mechanizmu
pozwalającego środowisku graficznemu na śledzenie uruchamiania
aplikacji, dostarczanie odpowiedzi użytkownika oraz inne rzeczy.

%package devel
Summary:	Startup Notification Library development files
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Startup Notification
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel

%description devel
Startup Notification Library development files.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki Startup Notification.

%package static
Summary:	Static Startup Notification Library library
Summary(pl.UTF-8):	Statyczna biblioteka Startup Notification
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Startup Notification Library library.

%description static -l pl.UTF-8
Statyczna biblioteka Startup Notification.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
