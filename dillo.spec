Summary:	DILLO - The GTK Web Browser
Summary(pl):	DILLO - przegl�darka web
Name:		dillo
Version:	0.6.6
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dillo.cipsga.org.br/download/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://dillo.cipsga.org.br/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	gtk+-devel >= 1.2.0
Buildrequires:	libpng-devel >= 1.0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Dillo is small, fast, based on GTK+ library web browser written in C.

%description -l pl
Dillo jest ma��, szybk�, bazuj�c� na bibliotece GTK+ przegl�dark�
sieci.

%prep
%setup -q

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
	CPPFLAGS="`pkg-config libpng12 --cflags`"
fi
%configure CPPFLAGS="$CPPFLAGS"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/WWW,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/WWW
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog dillorc doc/{*.txt,README}
%attr(755,root,root) %{_bindir}/dillo
%{_applnkdir}/Network/WWW/*
%{_pixmapsdir}/*
