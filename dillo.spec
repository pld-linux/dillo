Summary:	DILLO - The GTK Web Browser
Summary(pl):	DILLO - przegl±darka web
Name:		dillo
Version:	0.6.6
Release:	5
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dillo.cipsga.org.br/download/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-gzip_fallback.patch
Patch1:		http://matzar.republika.pl/stuff/%{name}-gettext.patch.gz
Patch2:		http://bobuk.ipost.ru/packages/dillo/files/%{name}-%{version}-charset.patch
Patch3:		%{name}-encodings.patch
Patch4:		%{name}-localedir.patch
URL:		http://dillo.cipsga.org.br/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libjpeg-devel
Buildrequires:	libpng-devel >= 1.0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Dillo is small, fast, based on GTK+ library web browser written in C.

%description -l pl
Dillo jest ma³±, szybk±, bazuj±c± na bibliotece GTK+ przegl±dark±
sieci.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure --enable-cookies

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/WWW,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/WWW
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog dillorc encodings doc/{*.txt,README}
%attr(755,root,root) %{_bindir}/dillo
%{_applnkdir}/Network/WWW/*
%{_pixmapsdir}/*
