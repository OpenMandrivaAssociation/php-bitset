%define modname bitset
%define soname %{modname}.so
%define inifile A84_%{modname}.ini

Summary:	BITSET library
Name:		php-%{modname}
Version:	1.0.1
Release:	%mkrel 1
Group:		Development/PHP
License:	PHP License
URL:		http://pecl.php.net/package/bitset/
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
BuildRequires:	php-devel >= 3:5.2.0
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Sets of bits manipuliting library.

%prep

%setup -q -n %{modname}-%{version}
[ "../package*.xml" != "/" ] && mv -f ../package*.xml .

# lib64 fixes
perl -pi -e "s|/lib\b|/%{_lib}|g" config.m4

%build
%serverbuild

phpize
%configure2_5x --with-libdir=%{_lib} \
    --with-%{modname}=shared,%{_prefix}

%make
mv modules/*.so .

%install
rm -rf %{buildroot} 

install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m0755 %{soname} %{buildroot}%{_libdir}/php/extensions/

cat > %{buildroot}%{_sysconfdir}/php.d/%{inifile} << EOF
extension = %{soname}
EOF

%post
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}


%changelog
* Wed Jun 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdv2012.0
+ Revision: 806372
- 1.0.1

* Sun May 06 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0-20
+ Revision: 797138
- fix build
- rebuild for php-5.4.x

* Sun Jan 15 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0-19
+ Revision: 761202
- rebuild

* Wed Aug 24 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-18
+ Revision: 696395
- rebuilt for php-5.3.8

* Fri Aug 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-17
+ Revision: 695367
- rebuilt for php-5.3.7

* Sat Mar 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-16
+ Revision: 646614
- rebuilt for php-5.3.6

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-15mdv2011.0
+ Revision: 629767
- rebuilt for php-5.3.5

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-14mdv2011.0
+ Revision: 628069
- ensure it's built without automake1.7

* Wed Nov 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-13mdv2011.0
+ Revision: 600463
- rebuild

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-12mdv2011.0
+ Revision: 588745
- rebuild

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-11mdv2010.1
+ Revision: 514519
- rebuilt for php-5.3.2

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-10mdv2010.1
+ Revision: 485340
- rebuilt for php-5.3.2RC1

* Sat Nov 21 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0-9mdv2010.1
+ Revision: 468146
- rebuilt against php-5.3.1

* Wed Sep 30 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0-8mdv2010.0
+ Revision: 451255
- rebuild

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 1.0-7mdv2010.0
+ Revision: 397268
- Rebuild

* Mon May 18 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdv2010.0
+ Revision: 376975
- rebuilt for php-5.3.0RC2

* Sun Mar 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0-5mdv2009.1
+ Revision: 346397
- rebuilt for php-5.2.9

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0-4mdv2009.1
+ Revision: 341710
- rebuilt against php-5.2.9RC2

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-3mdv2009.1
+ Revision: 321705
- rebuild

* Fri Dec 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-2mdv2009.1
+ Revision: 310251
- rebuilt against php-5.2.7

* Tue Oct 28 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2009.1
+ Revision: 297926
- import php-bitset


* Tue Oct 28 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2009.0
- initial Mandriva package
