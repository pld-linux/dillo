Summary:	DILLO - The GTK Web Browser.
Summary(pl):	DILLO - Przegladarka sieci.
Name:		dillo
Version:	0.3.2
Release:	1
Copyright:	GPL
Group:		X11/Application/Networking	
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	libjpeg-devel
BuildRequires:	gtk+-devel >= 1.2.0
Buildrequires:	libpng-devel >= 1.0.9
#Requires:	
Patch0:		%{name}-RPM_OPT_FLAGS.patch
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description
Dillo is small, fast, based on GTK+ library web browser written in C.

%description -l pl
Dillo jest mala, szybka, bazujaca na bibliotece GTK+ przegladarka sieci.

%prep
%setup -q

%patch0 -p0

%build
./configure --prefix=%{_prefix}
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/dillo
