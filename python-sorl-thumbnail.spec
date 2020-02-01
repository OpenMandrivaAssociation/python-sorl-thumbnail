%bcond_without python2

Summary:	Thumbnail engine for the Django webapp system

Name:		python-sorl-thumbnail
Version:	12.6.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/a1/06/fd428d34c1138682a55f2585a101e088246402f075792f0d856a3c2c8123/sorl-thumbnail-12.6.2.tar.gz
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

%if %{with python2}
%package -n python2-sorl-thumbnail
Summary:	Thumbnail engine for the Django webapp system
Group:		Development/Python
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
Requires:	python2-django

%description -n python2-sorl-thumbnail
Thumbnail engine for the Django webapp system
%endif

%prep
%setup -qc -b 0
mv sorl-thumbnail-%{version} python3

%if %{with python2}
cp -r python3 python2
%endif

%build
%if %{with python2}
cd python2
python2 setup.py build
cd ..
%endif

cd python3
python setup.py build
cd ..

%install
%if %{with python2}
cd python2
python2 setup.py install --skip-build --root %{buildroot}
cd ..
%endif

cd python3
python setup.py install --skip-build --root=%{buildroot} 
cd ..

%files
%{py_puresitedir}/*

%if %{with python2}
%files -n python2-sorl-thumbnail
%{py2_puresitedir}/*
%endif
