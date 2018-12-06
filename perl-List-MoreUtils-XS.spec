#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-List-MoreUtils-XS
Version  : 0.428
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/List-MoreUtils-XS-0.428.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/List-MoreUtils-XS-0.428.tar.gz
Summary  : 'Provide the stuff missing in List::Util in XS'
Group    : Development/Tools
License  : Apache-2.0
Requires: perl-List-MoreUtils-XS-lib = %{version}-%{release}
Requires: perl-List-MoreUtils-XS-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
# NAME
List::MoreUtils::XS - Provide compiled List::MoreUtils functions
# SYNOPSIS

%package dev
Summary: dev components for the perl-List-MoreUtils-XS package.
Group: Development
Requires: perl-List-MoreUtils-XS-lib = %{version}-%{release}
Provides: perl-List-MoreUtils-XS-devel = %{version}-%{release}

%description dev
dev components for the perl-List-MoreUtils-XS package.


%package lib
Summary: lib components for the perl-List-MoreUtils-XS package.
Group: Libraries
Requires: perl-List-MoreUtils-XS-license = %{version}-%{release}

%description lib
lib components for the perl-List-MoreUtils-XS package.


%package license
Summary: license components for the perl-List-MoreUtils-XS package.
Group: Default

%description license
license components for the perl-List-MoreUtils-XS package.


%prep
%setup -q -n List-MoreUtils-XS-0.428

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-List-MoreUtils-XS
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-List-MoreUtils-XS/LICENSE
cp t/LICENSE %{buildroot}/usr/share/package-licenses/perl-List-MoreUtils-XS/t_LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/List/MoreUtils/XS.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/List::MoreUtils::XS.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/List/MoreUtils/XS/XS.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-List-MoreUtils-XS/LICENSE
/usr/share/package-licenses/perl-List-MoreUtils-XS/t_LICENSE
