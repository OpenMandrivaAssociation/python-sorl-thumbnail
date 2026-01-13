%define module sorl-thumbnail
%define oname sorl_thumbnail

Summary:	Thumbnail engine for the Django webapp system
Name:		python-sorl-thumbnail
Version:	13.0.0
Release:	1
License:	BSD
Group:		Development/Python
URL:		https://github.com/jazzband/sorl-thumbnail
Source0:	https://github.com/jazzband/sorl-thumbnail/archive/%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pillow)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	python%{pyver}dist(django)

%description
Thumbnail engine for the Django webapp system

%prep
%autosetup -p1 -n %{module}-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%py_build

%install
%py_install

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/sorl
%{python_sitelib}/%{oname}-%{version}.dist-info
