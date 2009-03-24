# TODO gettext support
Summary:	DILLO - The GTK+ Web Browser
Summary(pl.UTF-8):	DILLO - przeglądarka WWW
Name:		dillo
Version:	2.0
Release:	0.1	
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.dillo.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	bb9999cabeb4db3d915687de465dbeb0
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-gzip_fallback.patch
Patch1:		%{name}-ac.patch
URL:		http://www.dillo.org/
BuildRequires:	autoconf
BuildRequires:	automake
# dillo 2.x needs fltk2 to work, be careful with it since its status is
# experimental
#BuildRequires:	fltk2-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/dillo

%description
Dillo is a small GTK+ based (GNOME is NOT required!) web browser.
Dillo aims to be a multi-platform browser alternative that's small,
stable, developer-friendly, usable, fast, and extensible.

%description -l pl.UTF-8
Dillo jest małą, opartą na bibliotece GTK+ (GNOME nie jest wymagany)
przeglądarką WWW. Dillo ma być wieloplatformową alternatywną
przeglądarką, która jest mała, stabilna, przyjazna dla developerów,
użyteczna, szybka i rozszerzalna.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
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

#%%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

#%%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog dillorc NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%dir %{_libdir}/dillo
%attr(755,root,root) %{_libdir}/dillo/*
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
