# TODO gettext support
Summary:	DILLO - The GTK+ Web Browser
Summary(pl):	DILLO - przegl±darka web
Name:		dillo
Version:	0.8.2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.dillo.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	4322f339aa4a4a2a4ba9a11444df9c67
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-gzip_fallback.patch
Patch1:		%{name}-0.7.0-alt-asp-charset-encodings-sysconfdir.patch
URL:		http://www.dillo.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/dillo

%description
Dillo is a small GTK+ based (GNOME is NOT required!) web browser.
Dillo aims to be a multi-platform browser alternative that's small, 
stable, developer-friendly, usable, fast, and extensible.

%description -l pl
Dillo jest ma³±, bazuj±c± na bibliotece GTK+ (GNOME nie jest wymagany)
przegl±dark± sieci. Dillo ma byæ wieloplatformow± alternatywn±
przegl±dark±, która jest ma³a, stabilna, przyjazna dla developerów,
u¿yteczna, szybka i rozszerzalna.

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
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install encodings  $RPM_BUILD_ROOT%{_sysconfdir}

#%%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

#%%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog dillorc encodings doc/{*.txt,README}
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/*
%dir %{_libdir}/dillo
%attr(755,root,root) %{_libdir}/dillo/*
%dir %{_sysconfdir}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
