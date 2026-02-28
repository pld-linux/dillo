# TODO: gettext support (there was a patch for some archaic version)
Summary:	DILLO - The FLTK Web Browser
Summary(pl.UTF-8):	DILLO - przeglądarka WWW
Name:		dillo
Version:	3.0.5
Release:	2
License:	GPL v3+
Group:		X11/Applications/Networking
Source0:	http://www.dillo.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	554aad93b6107bba696f4da022c41561
Source1:	%{name}.desktop
Source2:	%{name}.png
# needs a review, disabled for now
Patch0:		%{name}-gzip_fallback.patch
URL:		http://www.dillo.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	fltk-devel >= 1.3.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 2:1.6.0
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dillo is a small FLTK based (GNOME is NOT required!) web browser.
Dillo aims to be a multi-platform browser alternative that's small,
stable, developer-friendly, usable, fast, and extensible.

%description -l pl.UTF-8
Dillo jest małą, opartą na bibliotece FLTK (GNOME nie jest wymagany)
przeglądarką WWW. Dillo ma być wieloplatformową alternatywną
przeglądarką, która jest mała, stabilna, przyjazna dla developerów,
użyteczna, szybka i rozszerzalna.

%prep
%setup -q
#%%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-cookies \
	--enable-ipv6 \
	--enable-ssl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

#%%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

#%%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/dillo
%attr(755,root,root) %{_bindir}/dillo-install-hyphenation
%attr(755,root,root) %{_bindir}/dpid
%attr(755,root,root) %{_bindir}/dpidc
%dir %{_libdir}/dillo
%dir %{_libdir}/dillo/dpi
%dir %{_libdir}/dillo/dpi/*
%attr(755,root,root) %{_libdir}/dillo/dpi/*/*.dpi
%dir %{_docdir}/dillo
%{_docdir}/dillo/user_help.html
%dir %{_sysconfdir}/dillo
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dillo/dillorc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dillo/domainrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dillo/dpidrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dillo/keysrc
%{_desktopdir}/dillo.desktop
%{_pixmapsdir}/dillo.png
%{_mandir}/man1/dillo.1*
