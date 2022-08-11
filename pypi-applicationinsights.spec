#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-applicationinsights
Version  : 0.11.10
Release  : 24
URL      : https://files.pythonhosted.org/packages/d3/f2/46a75ac6096d60da0e71a068015b610206e697de01fa2fb5bba8564b0798/applicationinsights-0.11.10.tar.gz
Source0  : https://files.pythonhosted.org/packages/d3/f2/46a75ac6096d60da0e71a068015b610206e697de01fa2fb5bba8564b0798/applicationinsights-0.11.10.tar.gz
Summary  : This project extends the Application Insights API surface to support Python.
Group    : Development/Tools
License  : MIT
Requires: pypi-applicationinsights-license = %{version}-%{release}
Requires: pypi-applicationinsights-python = %{version}-%{release}
Requires: pypi-applicationinsights-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
This SDK is no longer maintained or supported by Microsoft. Check out the `Python OpenCensus SDK <https://docs.microsoft.com/azure/azure-monitor/app/opencensus-python>`_ for Azure Monitor's latest Python investments. Azure Monitor only provides support when using the `supported SDKs <https://docs.microsoft.com/en-us/azure/azure-monitor/app/platforms#unsupported-community-sdks>`_. We’re constantly assessing opportunities to expand our support for other languages, so follow our `GitHub Announcements <https://github.com/microsoft/ApplicationInsights-Announcements/issues>`_ page to receive the latest SDK news.

%package license
Summary: license components for the pypi-applicationinsights package.
Group: Default

%description license
license components for the pypi-applicationinsights package.


%package python
Summary: python components for the pypi-applicationinsights package.
Group: Default
Requires: pypi-applicationinsights-python3 = %{version}-%{release}

%description python
python components for the pypi-applicationinsights package.


%package python3
Summary: python3 components for the pypi-applicationinsights package.
Group: Default
Requires: python3-core
Provides: pypi(applicationinsights)

%description python3
python3 components for the pypi-applicationinsights package.


%prep
%setup -q -n applicationinsights-0.11.10
cd %{_builddir}/applicationinsights-0.11.10
pushd ..
cp -a applicationinsights-0.11.10 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656355779
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-applicationinsights
cp %{_builddir}/applicationinsights-0.11.10/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-applicationinsights/64fd6ac4ad1ace96d613b150dcf16e3b25e65f7b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-applicationinsights/64fd6ac4ad1ace96d613b150dcf16e3b25e65f7b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
