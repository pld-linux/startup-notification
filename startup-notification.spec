Summary:	startup-notification
Name:		startup-notification
Version:	0.4
Release:	0.9
Group:		Libraries
License:	LGPL
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.4/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
startup-notification

%package devel
Summary:	Header files for startup-notification
Group:		Libraries

%description devel
Header files for startup-notification

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
%{_libdir}/*.so*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.la
%{_includedir}/*
%{_pkgconfigdir}/*
