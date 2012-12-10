Summary: Mobln Installer
Name: moblin-installer
Version: 0.01
Release: %mkrel 6.1.3
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
/usr/lib/moblin-installer/*



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.01-6.1.3mdv2011.0
+ Revision: 620379
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.01-6.1.2mdv2010.0
+ Revision: 440050
- rebuild

* Thu Oct 16 2008 Thierry Vignaud <tv@mandriva.org> 0.01-6.1.1mdv2009.1
+ Revision: 294267
- fix path on x86_64
- import moblin-installer


* Thu Oct 16 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.01-6.1mdv2009.1
- adapt for Mandriva

* Sat Sep 27 2008 Anas Nashif <anas.nashif@intel.com> 0.01
- fixed grubby call
* Sat Sep 27 2008 Anas Nashif <anas.nashif@intel.com> 0.01
- fixed grubby, ask for confirmation
* Sat Sep 27 2008 Anas Nashif <anas.nashif@intel.com> 0.01
- Fix bootloader configuration
* Sat Sep 27 2008 Anas Nashif <anas.nashif@intel.com> 0.01
- initial import
