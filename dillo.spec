Summary:	DILLO - The GTK Web Browser
Summary(pl):	DILLO - przegladarka web
Name:		dillo
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	libjpeg-devel
BuildRequires:	gtk+-devel >= 1.2.0
Buildrequires:	libpng-devel >= 1.0.9
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Dillo is small, fast, based on GTK+ library web browser written in C.

%description -l pl
Dillo jest mala, szybka, bazujaca na bibliotece GTK+ przegladarka
sieci.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/dillo
