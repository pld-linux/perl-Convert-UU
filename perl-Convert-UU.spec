#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Convert
%define		pnam	UU
Summary:	Convert::UU - Perl module for uuencode and uudecode
Summary(pl.UTF-8):	Convert::UU - moduł Perla zastępujący uuencode i uudecode
Name:		perl-Convert-UU
Version:	0.5201
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f60f49d15770503efa5ed0c81296ef2f
URL:		http://search.cpan.org/dist/Convert-UU/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::UU is a Perl module for uuencode and uudecode.

%description -l pl.UTF-8
Convert::UU jest modułem Perla zastępującym uuencode i uudecode.

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
