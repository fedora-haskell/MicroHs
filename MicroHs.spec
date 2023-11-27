# generated by cabal-rpm-2.1.5
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

# workaround Empty %files file BUILD/MicroHs-0.8.4.0/debugsourcefiles.list
%define debug_package %{nil}

%bcond ghc 0
%ifnarch %{ix86}
%bcond compiler_bootstrap 1
%endif

Name:           MicroHs
Version:        0.8.4.0
Release:        1%{?dist}
Summary:        A compiler for a subset of Haskell

License:        Apache-2.0
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
# End cabal-rpm sources
Source1:        mhs.in

# Begin cabal-rpm deps:
%if %{with ghc}
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-time-devel
%else
BuildRequires:  gcc
BuildRequires:  make
%endif
# End cabal-rpm deps

%description
A compiler for a subset of Haskell. The compiler translates to combinators and
can compile itself.


%prep
%setup -q


%build
make %{?with_compiler_bootstrap:bootstrap}


%install
%define mhsdir %{_libdir}/mhs-%{version}
make install PREFIX=%{buildroot}%{mhsdir}

mkdir %{buildroot}%{_bindir}
install %{SOURCE1} %{buildroot}%{_bindir}/mhs
sed -i -e 's!@PREFIX@!%{mhsdir}!' %{buildroot}%{_bindir}/mhs


%check
MHS_PREFIX=%{buildroot}%{mhsdir} %{buildroot}%{_bindir}/mhs Example -oEx
./Ex
MHS_PREFIX=%{buildroot}%{mhsdir} %{buildroot}%{_bindir}/mhs Example -r
#missing /bin/sh: line 1: errmsg.test: No such file or directory
# make runtest


%files
# Begin cabal-rpm files:
%license LICENSE
%doc Example.hs README.md
%{_bindir}/mhs
%{mhsdir}
# End cabal-rpm files


%changelog
* Sun Nov 26 2023 Jens Petersen <petersen@redhat.com> - 0.8.4.0-1
- spec file generated by cabal-rpm-2.1.5