Summary:	DILLO - The GTK Web Browser.
Summary(pl):	DILLO - Przegladarka sieci.
Name:		dillo
Version:	0.3.2
Release:	1
Copyright:	GPL
Group:		X11/Application/Networking	
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tag.gz
#BuildRequires:	
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description

%description -l pl

%prep
%setup -q

#%patch

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
%doc
%attr(,,)
