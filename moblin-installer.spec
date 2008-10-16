Summary: Mobln Installer
Name: moblin-installer
Version: 0.01
Release: %mkrel 6.1
License: GPLv2
Group: System/Configuration/Other
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)  

%description 
This is the Moblin Installer.

%prep
%setup -q

%build

%install
rm -fr $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT/usr/lib/moblin-installer/tasks/{hard,soft}
install -d  $RPM_BUILD_ROOT/usr/share/moblin-installer/wallpapers
install -m 744 tasks/hard/* $RPM_BUILD_ROOT/usr/lib/moblin-installer/tasks/hard
install -m 744 install_moblin.sh* $RPM_BUILD_ROOT/usr/lib/moblin-installer
#install -m 744 tasks/soft/* $RPM_BUILD_ROOT/usr/lib/moblin-installer/tasks/offline
install -m 644 images/wallpapers/* $RPM_BUILD_ROOT/usr/share/moblin-installer/wallpapers


%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}//moblin-installer/wallpapers/*
%{_libdir}/moblin-installer/*

