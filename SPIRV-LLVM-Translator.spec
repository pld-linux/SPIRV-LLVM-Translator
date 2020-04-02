
%define llvm_version 10.0.0

Summary:	LLVM/SPIR-V Bi-Directional Translator
Summary(pl.UTF-8):	Dwustronny translator LLVM/SPIR-V
Name:		SPIRV-LLVM-Translator
Version:	10.0.0
Release:	1
License:	University of Illinois/NCSA Open Source License
Group:		Libraries
#Source0Download: https://github.com/KhronosGroup/SPIRV-LLVM-Translator/releases
Source0:	https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7c595d08c6b09947a2a73243b6fb8cbb
# from Intel opencl-clang
Patch0:		0001-Update-LowerOpenCL-pass-to-handle-new-blocks-represn.patch
URL:		https://github.com/KhronosGroup/SPIRV-LLVM-Translator/
BuildRequires:	cmake >= 3.3
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	llvm-devel >= %{llvm_version}
BuildRequires:	pkgconfig
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
%setup -qn %{name}-%{version}

%build

install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_libdir}/libLLVMSPIRVLib.so.10 $RPM_BUILD_ROOT%{_libdir}/libLLVMSPIRVLib.so.%{version}
ln -s libLLVMSPIRVLib.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libLLVMSPIRVLib.so.10
ln -sf libLLVMSPIRVLib.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libLLVMSPIRVLib.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md LICENSE.TXT
%attr(755,root,root) %{_libdir}/libLLVMSPIRVLib.so.10.*.*
%ghost %attr(755,root,root) %{_libdir}/libLLVMSPIRVLib.so.10

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libLLVMSPIRVLib.so
%{_includedir}/LLVMSPIRVLib
%{_pkgconfigdir}/LLVMSPIRVLib.pc
