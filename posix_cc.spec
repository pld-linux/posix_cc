Name:		posix_cc
Summary:	POSIX 1003.2 and 1003.1 2001 C language compilers
Summary(pl):	Zgodne z POSIX 1003.2 i 1003.1 2001 kompilatory C
Version:	1.4
Release:	1
License:	BSD
Group:		Development/Languages
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	c92d41039d8057a7479f968360738a96
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	gcc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
c89 is the name of the C language compiler as required by the POSIX
1003.2 standard, while c99 is the name required by the POSIX 1003.1
2001 standard. Both are actually wrappers for gcc, passing it the
options required to make it conform to said standards in addition to
the options passed via the command line.

Both will only accept those options mandated by the respective
standards.

Authors: Jens Schweikhardt

%description -l pl
c89 jest nazw± kompilatora C zgodnego z standardem POSIX 1003.2,
natomiast c99 jest nazwê kompilatora zgodnego z standardem POSIX
1003.1 2001. Oba kompilatory s± nak³adkami na gcc, sprawdzaj± czy
przekazywane opcje odpowiadaj± standardom.

Oba akceptuj± wy³±cznie opcje przewidziane w odpowiednich standardach.

Autor: Jens Schweikhardt

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/c?9
%{_mandir}/man?/*
