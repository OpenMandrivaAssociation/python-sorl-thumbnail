
Summary:	Thumbnail engine for the Django webapp system

Name:		python-sorl-thumbnail
Version:	12.7.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/92/f7/3d9583bf7a5acf37d6609b8764cc979df1e17d00878538a69a5988e867fc/sorl-thumbnail-12.7.0.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://pypi.python.org/pypi/sorl-thumbnail
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3-distribute
Requires:	python-django

%description
Thumbnail engine for the Django webapp system

%prep
%setup -qc -b 0
mv sorl-thumbnail-%{version} python3

%build
cd python3
python setup.py build
cd ..

%install
cd python3
python setup.py install --skip-build --root=%{buildroot} 
cd ..

%files
%{py_puresitedir}/*
