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
Version:        2.5.2
Release:        0
License:        BSD-2-Clause
Summary:	Network config for BLINUX
Group:          System Environment/Base

Requires(post):	systemd
Requires(preun):	systemd
BuildRequires:	hwinfo
BuildArch:      noarch
Source0:        wpa_switch
Source1:        wpa_watch
Source2:        network-config-generate
Source3:        wpa_watch.service
Source4:        wpa_supplicant.service
Source5:        wpa_supplicant.conf
Source6:        dhcp

Requires:	wpa_supplicant-gui
Requires:	hwinfo

Url:            http://www.blinux.fr
Packager:       Emmanuel Vadot <elbarto@bocal.org>
Vendor:		Blinux

%description
Network config and scripts for BLINUX

%prep

%build

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}/usr/lib/systemd/system/
mkdir -p %{buildroot}%{_sysconfdir}/wpa_supplicant
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/network
install -D -m 755 %{SOURCE0} %{buildroot}%{_sbindir}
install -D -m 755 %{SOURCE1} %{buildroot}%{_sbindir}
install -D -m 755 %{SOURCE2} %{buildroot}%{_sbindir}
install -D -m 644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/
install -D -m 644 %{SOURCE4} %{buildroot}/usr/lib/systemd/system/wpa_supp.service.tpl
install -D -m 644 %{SOURCE5} %{buildroot}/%{_sysconfdir}/wpa_supplicant/wpa_supplicant.conf.tpl
install -D -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/sysconfig/network/

%post
/usr/sbin/network-config-generate

%postun
case "$*" in
  0)  
  /usr/bin/systemctl disable wpa_watch.service
  /usr/bin/systemctl disable wpa_supp.service
  /usr/bin/systemctl enable wpa_supplicant.service
  ;;
  esac

%files
%defattr(-,root,root)
/etc/wpa_supplicant
%{_sbindir}/wpa_switch
%{_sbindir}/wpa_watch
%{_sbindir}/network-config-generate
/usr/lib/systemd/system/wpa_watch.service
/usr/lib/systemd/system/wpa_supp.service.tpl
%config(noreplace) %{_sysconfdir}/wpa_supplicant/wpa_supplicant.conf.tpl
%config(noreplace) %{_sysconfdir}/sysconfig/network/dhcp

%changelog
* Mon Aug 11 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.5
- Uses SOURCE* directly

* Mon Aug 04 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.4
- Typo in network-config-generate

* Mon Aug 04 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.3
- Handle case where no wlans is found

* Mon Aug 04 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.2
- Generate config files and service at install

* Sun May 18 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.1
- Add wpa_watch
- Remove wpa_switch service

* Sat May 03 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.0-1
- Copy original file of wpa_supplicant in .orig
- Add wpa_supplicant-gui as Requires

* Sat May 03 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.0-0
- Bump to 1.4.4

* Tue Apr 01 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.4.4-0
- Bump to 1.4.4

* Tue Apr 01 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.4.3-0
- Bump to 1.4.3

* Sun Mar 30 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.4.2-0
- Bump to 1.4.2

* Sun Mar 30 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.4.1-0
- Bump to 1.4.1

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
