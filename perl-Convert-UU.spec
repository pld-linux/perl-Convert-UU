#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Convert
%define		pnam	UU
Summary:	Convert::UU - Perl module for uuencode and uudecode
Summary(pl):	Convert::UU - modu³ Perla zastêpuj±cy uuencode i uudecode
Name:		perl-Convert-UU
Version:	0.52
Release:	3
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1a52e65a9459e4deafd5b2fdf932d0ba
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::UU is a Perl module for uuencode and uudecode.

%description -l pl
Convert::UU jest modu³em Perla zastêpuj±cym uuencode i uudecode.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Convert/UU.pm
%{_mandir}/man[13]/*
