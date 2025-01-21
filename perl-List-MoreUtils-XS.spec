#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : perl-List-MoreUtils-XS
Version  : 0.430
Release  : 33
URL      : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/List-MoreUtils-XS-0.430.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/List-MoreUtils-XS-0.430.tar.gz
Summary  : 'Provide the stuff missing in List::Util in XS'
Group    : Development/Tools
License  : Apache-2.0
Requires: perl-List-MoreUtils-XS-license = %{version}-%{release}
Requires: perl-List-MoreUtils-XS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Storable)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# NAME
List::MoreUtils::XS - Provide compiled List::MoreUtils functions
# SYNOPSIS

%package dev
Summary: dev components for the perl-List-MoreUtils-XS package.
Group: Development
Provides: perl-List-MoreUtils-XS-devel = %{version}-%{release}
Requires: perl-List-MoreUtils-XS = %{version}-%{release}

%description dev
dev components for the perl-List-MoreUtils-XS package.


%package license
Summary: license components for the perl-List-MoreUtils-XS package.
Group: Default

%description license
license components for the perl-List-MoreUtils-XS package.


%package perl
Summary: perl components for the perl-List-MoreUtils-XS package.
Group: Default
Requires: perl-List-MoreUtils-XS = %{version}-%{release}

%description perl
perl components for the perl-List-MoreUtils-XS package.


%prep
%setup -q -n List-MoreUtils-XS-0.430
cd %{_builddir}/List-MoreUtils-XS-0.430

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-List-MoreUtils-XS
cp %{_builddir}/List-MoreUtils-XS-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-List-MoreUtils-XS/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
cp %{_builddir}/List-MoreUtils-XS-%{version}/t/LICENSE %{buildroot}/usr/share/package-licenses/perl-List-MoreUtils-XS/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/List::MoreUtils::XS.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-List-MoreUtils-XS/92170cdc034b2ff819323ff670d3b7266c8bffcd

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
