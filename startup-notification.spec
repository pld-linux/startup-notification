Summary:	Startup Notification Library
Summary(pl):	Biblioteka Startup Notification
Name:		startup-notification
Version:	0.6
Release:	1
Group:		Libraries
License:	LGPL
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	d53172f761ea974e5d5f73f9b785294c
URL:		http://www.gnome.org/
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Startup Notification Library implements a mechanism allowing a
desktop environment to track application startup, to provide user
feedback and other features.

%description -l pl
Biblioteka Startup Notification jest implementacj± mechanizmu
pozwalaj±cego ¶rodowisku graficznemu na ¶ledzenie uruchamiania
aplikacji, dostarczanie odpowiedzi u¿ytkownika oraz inne rzeczy.

%package devel
Summary:	Startup Notification Library development files
Summary(pl):	Pliki programistyczne biblioteki Startup Notification
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	XFree86-devel

%description devel
Startup Notification Library development files.

%description devel -l pl
Pliki programistyczne biblioteki Startup Notification.

%package static
Summary:	Static Startup Notification Library library
Summary(pl):	Statyczna biblioteka Startup Notification
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Startup Notification Library library.

%description static -l pl
Statyczna biblioteka Startup Notification.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
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
