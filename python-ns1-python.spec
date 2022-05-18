%global _empty_manifest_terminate_build 0
Name:		python-ns1-python
Version:	0.16.0
Release:	2
Summary:	Python SDK for the NS1 DNS platform
License:	MIT
URL:		https://github.com/ns1/ns1-python
Source0:	https://files.pythonhosted.org/packages/93/5a/7024d3f35170c83f9e83945d7c8ab85eefc547dfc7c5854748c1bc719b1b/ns1-python-0.16.0.tar.gz
BuildArch:	noarch
BuildRequires:  python3-pip python3-pytest-runner
%global _description %{expand:
This package provides a python SDK for accessing the NS1 DNS platform
and includes both a simple NS1 REST API wrapper as well as a higher level
interface for managing zones, records, data feeds, and more.
It supports synchronous and asynchronous transports.}

%description %{_description}


%package -n python3-ns1-python
Summary:	Python SDK for the NS1 DNS platform
Provides:	python-ns1-python
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-ns1-python %{_description}
Python 3 version.

%package help
Summary:	Development documents and examples for ns1-python
Provides:	python3-ns1-python-doc
%description help
Development documents and examples for ns1-python

%prep
%autosetup -n ns1-python-0.16.0

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-ns1-python -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Wed May 18 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn>
- add necessary BuildRequires

* Sun May 23 2021 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
