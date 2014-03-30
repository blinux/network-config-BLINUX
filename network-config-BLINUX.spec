#-
# Copyright 2013-2014 Emmanuel Vadot <elbarto@bocal.org>
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions 
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

Name:		network-config-BLINUX
Version:        1.4
Release:        0
License:        BSD-2-Clause
Summary:	Network config for BLINUX
Requires(post):	systemd
Requires(preun):	systemd
BuildArch:      noarch
Source0:        %{name}-%{version}.tgz
Vendor:		Bocal
Url:            http://www.bocal.org
Group:          System Environment/Base
Packager:       Emmanuel Vadot <elbarto@bocal.org>

%description
Network config and scripts for BLINUX

%prep
%setup

%build

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}/usr/lib/systemd/system/
mkdir -p %{buildroot}%{_sysconfdir}/wpa_supplicant
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/network
cp wpa_switch %{buildroot}%{_sbindir}
cp wpa_switch.service %{buildroot}/usr/lib/systemd/system/
cp wpa_supplicant.service %{buildroot}/usr/lib/systemd/system/
cp wpa_supplicant.conf %{buildroot}/%{_sysconfdir}/wpa_supplicant/
cp ifcfg-enp0s25 %{buildroot}%{_sysconfdir}/sysconfig/network/
cp ifcfg-wlo1 %{buildroot}%{_sysconfdir}/sysconfig/network/
cp ifcfg-eno1 %{buildroot}%{_sysconfdir}/sysconfig/network/

%post
/usr/bin/systemctl enable wpa_switch.service

%postun
case "$*" in
  0)  
  /usr/bin/systemctl disable wpa_switch.service
  ;;
  esac

%files
%attr(755,root,root) %{_sbindir}/wpa_switch
%attr(644,root,root) /usr/lib/systemd/system/wpa_switch.service
%attr(644,root,root) /usr/lib/systemd/system/wpa_supplicant.service
%attr(644,root,root) %{_sysconfdir}/wpa_supplicant/wpa_supplicant.conf
%attr(644,root,root) %{_sysconfdir}/sysconfig/network/ifcfg-enp0s25
%attr(644,root,root) %{_sysconfdir}/sysconfig/network/ifcfg-wlo1
%attr(644,root,root) %{_sysconfdir}/sysconfig/network/ifcfg-eno1

%changelog
* Sun Mar 30 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.4-0
- Bump to 1.4

* Sun Mar 30 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.3-0
- Bump to 1.3

* Sun Mar 14 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.2-0
- Bump to 1.2

* Sun Mar 02 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.1-0
- Bump to 1.1

* Sun Mar 02 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.0-1
- Add wpa_supplicant configuration

* Sat Mar 01 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.0-0
- Package creation
