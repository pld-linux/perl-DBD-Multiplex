#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	Multiplex
Summary:	DBD::Multiplex - A multiplexing driver for the DBI
Summary(pl):	DBD::Multiplex - sterownik zwielokrotniaj�cy dla DBI
Name:		perl-DBD-Multiplex
Version:	1.96
Release:	0.2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	226fd4ea2dbecf1d0353beb95ce9c9d6
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::Multiplex is a Perl module which works with the DBI allowing you
to work with multiple datasources using a single DBI handle.

Basically, DBD::Multiplex database and statement handles are parents
that contain multiple child handles, one for each datasource. Method
calls on the parent handle trigger corresponding method calls on each
of the children.

One use of this module is to mirror the contents of one datasource
using a set of alternate datasources. For that scenario it can write
to all datasources, but read from only from one datasource.

Alternatively, where a database already supports replication,
DBD::Multiplex can be used to direct writes to the master and spread
the selects across multiple slaves.

%description -l pl
DBD::Multiplex to modu� Perla, kt�ry wsp�pracuje z DBI pozwalaj�c
pracowa� z wieloma �r�d�ami danych przy u�yciu pojedynczego uchwytu
DBI.

Zasadniczo baza danych i uchwyty rozkaz�w DBD::Multiplex s� rodzicami
zawieraj�cymi wiele uchwyt�w potomnych, po jednym dla ka�dego �r�d�a
danych. Wywo�ania metod w g��wnym uchwycie wyzwalaj� odpowiednie
wywo�ania metod w ka�dym z potomk�w.

Jedno z zastosowa� tego modu�u to mirroring zawarto�ci jednego
�r�d�a danych przy u�yciu zbioru alternatywnych �r�de�. W tym
scenariuszu mo�na zapisywa� do wszystkich �r�de� danych, ale czyta�
tylko z jednego �r�d�a.

Alternatywnie, je�li baza danych ju� obs�uguje replikacj�,
DBD::Multiplex mo�e s�u�y� do bezpo�redniego zapisu do g��wnej bazy i
rozprowadzania zapyta� po wielu bazach podrz�dnych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/%{pdir}/%{pnam}/.packlist

mv $RPM_BUILD_ROOT{%{perl_vendorlib}/%{pdir}/example.pl,%{_examplesdir}/%{name}-%{version}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
