# TODO gettext support
Summary:	DILLO - The GTK Web Browser
Summary(pl):	DILLO - przegl±darka web
Name:		dillo
Version:	0.7.2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dillo.auriga.wearlab.de/download/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-gzip_fallback.patch
Patch1:		%{name}-0.7.0-alt-asp-charset-encodings-sysconfdir.patch
URL:		http://dillo.auriga.wearlab.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libjpeg-devel
Buildrequires:	libpng-devel >= 1.0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/dillo

%description
Dillo is small, fast, based on GTK+ library web browser written in C.

%description -l pl
Dillo jest ma³±, szybk±, bazuj±c± na bibliotece GTK+ przegl±dark±
sieci.

%prep
%setup  -q 
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-cookies \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/WWW,%{_pixmapsdir},%{_sysconfdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/WWW
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

#%%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

#%%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog dillorc encodings doc/{*.txt,README}
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/WWW/*
%{_pixmapsdir}/*
%dir %{_sysconfdir}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
