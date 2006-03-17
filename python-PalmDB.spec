
%define		module	PalmDB

Summary:	Pure Python library to read/write/modify Palm PDB and PRC format databases
Name:		python-%{module}
Version:	1.4.1
Release:	1
License:	GNU
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pythonpalmdb/%{module}-%{version}.zip
# Source0-md5:	c7414dcef1b5b24e79da97ce883aa44b
URL:		http://id3-py.sourceforge.net/
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows access to Palm OS(tm) database files on the desktop
in pure Python. It is as simple as possible without (hopefully) being
too simple. As much as possible Python idioms have been used to make
it easier to use and more versatile.

This code is based on code from the Pyrite Project, available I believe
from SourceForge. However the code has been modified so extensively it's
hardly recognizable. But without the Pyrite code, PalmDB would not be here
today.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{py_sitescriptdir}/*.py[co]
