#
# Conditional build:
%bcond_with	fltk14	# experimental FLTK 1.4.x support (known graphical issues)

Summary:	DILLO - The FLTK Web Browser
Summary(pl.UTF-8):	DILLO - przeglądarka WWW
Name:		dillo
Version:	3.3.0
Release:	1
License:	GPL v3+
Group:		X11/Applications/Networking
Source0:	https://dillo-browser.org/release/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	14b7a0e6a8ce4888423a7acbc0e6c906
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		https://dillo-browser.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	fltk-devel >= 1.3.0
%if %{with fltk14}
BuildRequires:	fltk-devel >= 1.4.0
%else
BuildRequires:	fltk-devel < 1.4.0
%endif
BuildRequires:	libbrotli-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 2:1.6.0
BuildRequires:	libstdc++-devel
BuildRequires:	libwebp-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
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

%{__sed} -i -e '1s,.*env perl,#!%{__perl},' dillo-install-hyphenation

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-cookies \
	%{?with_fltk14:--enable-experimental-fltk} \
	--enable-ipv6 \
	--enable-tls
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/dillo
%attr(755,root,root) %{_bindir}/dillo-install-hyphenation
%attr(755,root,root) %{_bindir}/dilloc
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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dillo/hsts_preload
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dillo/keysrc
%{_desktopdir}/dillo.desktop
%{_iconsdir}/hicolor/*x*/apps/dillo.png
%{_pixmapsdir}/dillo.png
%{_mandir}/man1/dillo.1*
