
%define		module	PalmDB

Summary:	Pure Python library to read/write/modify Palm PDB and PRC format databases
Summary(pl.UTF-8):	Czysto pythonowa biblioteka do odczytu/zapisu/modyfikowania palmowych baz PDB i PRC
Name:		python-%{module}
Version:	1.4.1
Release:	4
License:	GNU
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pythonpalmdb/%{module}-%{version}.zip
# Source0-md5:	c7414dcef1b5b24e79da97ce883aa44b
URL:		http://id3-py.sourceforge.net/
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows access to Palm OS(tm) database files on the desktop
in pure Python. It is as simple as possible without (hopefully) being
too simple. As much as possible Python idioms have been used to make
it easier to use and more versatile.

This code is based on code from the Pyrite Project. However the code
has been modified so extensively it's hardly recognizable. But without
the Pyrite code, PalmDB would not be here today.

%description -l pl.UTF-8
Ten moduł umożliwia dostęp do plików baz danych PalmOS(TM) z poziomu
czystego Pythona. Jest tak prosty jak to tylko możliwe nie będąc
(miejmy nadzieję) zbyt prostym. Użyto jak najwięcej pythonowych
idiomów, aby uczynić go łatwiejszym w użyciu i bardziej elastycznym.

Ten kod jest oparty na kodzie z projektu Pyrite. Jednak kod został na
tyle zmieniony, że jest trudno rozpoznawalny. Lecz bez kodu Pyrite
PalmDB nie zaszedłby jeszcze tak daleko.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

%py_install

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{py_sitescriptdir}/*.py[co]
