%define		_snap	20050409
Summary:	Reimplemntation of the classic real time strategy hit Command & Conquer
Summary(pl):	Reimplementacja strategii czasu rzeczywistego Command & Conquer
Name:		freecnc
Version:	0.1
Release:	0.%{_snap}
License:	GPL
Group:		X11/Applications/Games
# taken from cvs://anonymous@cvs.FreeCNC.sourceforge.net:/cvsroot/freecnc
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	0458576aa3386292ab9dc8caf6341b02
Patch0:		%{name}-paths.patch
URL:		http://freecnc-sf.holarse.net/
BuildRequires:	SDL-devel
BuildRequires:	boost-conversion-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreeCNC will be a free implementation of the Command & Conquer Game
Engine written in SDL. It will support the original C&C graphics and
audio, as well as Red Alert's data files.

%description -l pl
FreeCNC bêdzie wolnodostêpn±, napisan± w SDL implementacj± silnika gry
Command & Conquer. Bêdzie wspieraæ grafikê i efekty d¼wiêkowe zarówno
z plików gry Command & Conquer jak i Red Alert.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAFS="%{rpmcflags} `sdl-config --cflags`" \
	CXXFLAGS="%{rpmcflags} `sdl-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
install freecnc shpview tmpinied $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.txt INSTALL.txt README.txt TODO.txt
%attr(755,root,root) %{_bindir}/*
# empty for now
%{_datadir}/%{name}
