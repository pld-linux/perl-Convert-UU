%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	UU
Summary:	Convert::UU perl module
Summary(pl):	Modu³ perla Convert::UU
Name:		perl-Convert-UU
Version:	0.52
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1a52e65a9459e4deafd5b2fdf932d0ba
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::UU - perl module for uuencode and uudecode.

%description -l pl
Convert::UU - modu³ perla dla uuencode i uudecode.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Convert/UU.pm
%{_mandir}/man[13]/*
