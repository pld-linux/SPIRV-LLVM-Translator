
%define llvm_version 7.0.1

Summary:	LLVM/SPIR-V Bi-Directional Translator
Name:		SPIRV-LLVM-Translator
Version:	7.0.1
Release:	1
License:	University of Illinois/NCSA Open Source License
Group:		Libraries
Source0:	https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/%{version}-1/%{name}-%{version}-1.tar.gz
# Source0-md5:	e73c5ebffb4fc5dc606cd217f69ec97c
# from Intel opencl-clang
Patch0:		0001-Update-LowerOpenCL-pass-to-handle-new-blocks-represn.patch
URL:		https://github.com/KhronosGroup/SPIRV-LLVM-Translator/
BuildRequires:	cmake >= 3.3
BuildRequires:	llvm-devel >= %{llvm_version}
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LLVM/SPIR-V Bi-Directional Translator - a library and tool for
translation between LLVM IR and SPIR-V.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -qn %{name}-%{version}-1

%build

install -d build
cd build
%cmake \
	../
%{__make}

cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_libdir}/libLLVMSPIRVLib.so.7 $RPM_BUILD_ROOT%{_libdir}/libLLVMSPIRVLib.so.%{version}
ln -s libLLVMSPIRVLib.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libLLVMSPIRVLib.so.7
ln -sf libLLVMSPIRVLib.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libLLVMSPIRVLib.so


%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md LICENSE.TXT
%attr(755,root,root) %{_libdir}/libLLVMSPIRVLib.so.7.*.*
%ghost %attr(755,root,root) %{_libdir}/libLLVMSPIRVLib.so.7

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libLLVMSPIRVLib.so
%{_includedir}/LLVMSPIRVLib
%{_pkgconfigdir}/LLVMSPIRVLib.pc
