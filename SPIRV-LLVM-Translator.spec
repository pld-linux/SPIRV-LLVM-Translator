
%define llvm_version 18.1.0

Summary:	LLVM/SPIR-V Bi-Directional Translator
Summary(pl.UTF-8):	Dwustronny translator LLVM/SPIR-V
Name:		SPIRV-LLVM-Translator
Version:	18.1.3
Release:	1
License:	University of Illinois/NCSA Open Source License
Group:		Libraries
#Source0Download: https://github.com/KhronosGroup/SPIRV-LLVM-Translator/releases
Source0:	https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	094ff60909ada1e76e87da90df053be6
URL:		https://github.com/KhronosGroup/SPIRV-LLVM-Translator/
BuildRequires:	cmake >= 3.13.4
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	llvm-devel >= %{llvm_version}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	spirv-headers >= 1.6.1-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LLVM/SPIR-V Bi-Directional Translator - a library and tool for
translation between LLVM IR and SPIR-V.

%description -l pl.UTF-8
Dwustronny translator LLVM/SPIR-V - biblioteka i narzędzie do
tłumaczenia między IR LLVM a SPIR-V.

%package devel
Summary:	Header files for LLVMSPIRVLib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LLVMSPIRVLib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:4.7
Requires:	llvm-devel >= %{llvm_version}

%description devel
Header files for LLVMSPIRVLib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki LLVMSPIRVLib.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR=/usr/include/spirv/unified1

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_libdir}/libLLVMSPIRVLib.so.18.1 $RPM_BUILD_ROOT%{_libdir}/libLLVMSPIRVLib.so.%{version}
ln -s libLLVMSPIRVLib.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libLLVMSPIRVLib.so.18.1
ln -sf libLLVMSPIRVLib.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libLLVMSPIRVLib.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md LICENSE.TXT
%attr(755,root,root) %{_bindir}/llvm-spirv
%attr(755,root,root) %{_libdir}/libLLVMSPIRVLib.so.18.*.*
%ghost %attr(755,root,root) %{_libdir}/libLLVMSPIRVLib.so.18.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libLLVMSPIRVLib.so
%{_includedir}/LLVMSPIRVLib
%{_pkgconfigdir}/LLVMSPIRVLib.pc
