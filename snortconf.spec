Summary:	A tool to ease configuring the OpenSource IDS tool Snort
Name:		snortconf
Version:	0.4.2
Release:	%mkrel 0.BETA.5
License:	GPL
Group:		System/Servers
Source0:	%{name}-%{version}.tar.bz2
Patch0:		snortconf-0.4.2-config.patch
URL:		https://www.xjack.org/snortconf
Requires:	snort
Requires:	ncurses
BuildRequires:	ncurses-devel
BuildRoot:	%{_tmppath}/%{name}-root

%description
SnortConf is a simple, intuitive menu based tool that provides a
more user friendly interface to creating a snort.conf file. It is
still in it's early days of development, but it is already fully
functional in most respects.

%prep

%setup -q
%patch0 -p1 -b .config

%build

%configure2_5x

make -C src CFLAGS="%{optflags} -DHAVE_CONFIG_H"

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/%{name}
install -d %{buildroot}%{_bindir}

install -m755 src/%{name} %{buildroot}%{_bindir}/%{name}
install -m644 conf/sc.conf %{buildroot}%{_sysconfdir}/%{name}/sc.conf

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
						
%files
%defattr(-,root,root)
%doc CHANGES CREDITS README README.BETA TODO USAGE
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/%{name}/sc.conf
%attr(0755,root,root) %{_bindir}/%{name}



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.4.2-0.BETA.5mdv2010.0
+ Revision: 433984
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.4.2-0.BETA.4mdv2008.1
+ Revision: 140829
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - import snortconf


* Fri Jul 14 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-0.BETA.4mdv2007.0
- rebuild

* Fri Jun 03 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-0.BETA.3mdk
- rebuild

* Sun May 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.4.2-0.BETA.2mdk
- use macros

* Wed Apr 23 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.4.2-0.BETA.1mdk
- initial cooker contrib
