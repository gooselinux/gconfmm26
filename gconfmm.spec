Name:           gconfmm26
Version:        2.28.0
Release:        1%{?dist}

Summary:        C++ wrapper for GConf2

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://gtkmm.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gconfmm/2.28/gconfmm-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  glibmm24-devel >= 2.6.4
BuildRequires:  gtkmm24-devel >= 2.4.0
BuildRequires:  GConf2-devel >= 2.4.0

%description
This package provides a C++ interface for GConf2. It is a subpackage
of the GTKmm project.  The interface provides a convenient interface
for C++ programmers to create Gnome GUIs with GTK+'s flexible
object-oriented framework.

%package devel
Summary:        Headers for developing programs that will use gconfmm
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       glibmm24-devel
Requires:       gtkmm24-devel
Requires:       GConf2-devel

%description devel
This package contains the headers that programmers will need to
develop applications which will use gconfmm, part of GTKmm, the C++
interface to the GTK+.


%prep
%setup -q -n gconfmm-%{version}

%build
%configure --disable-static --enable-shared
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig


%postun
/sbin/ldconfig


%files
%defattr(-, root, root, -)
%doc AUTHORS ChangeLog COPYING NEWS README INSTALL
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, -)
%{_includedir}/gconfmm-2.6
%{_libdir}/gconfmm-2.6
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Sep 25 2009 Denis Leroy <denis@poolshark.org> - 2.28.0-1
- Update to upstream 2.28.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Denis Leroy <denis@poolshark.org> - 2.24.0-1
- Update to upstream 2.24.0

* Wed Mar 12 2008 Denis Leroy <denis@poolshark.org> - 2.22.0-1
- Update to upstream 2.22.0

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.20.0-2
- Autorebuild for GCC 4.3

* Mon Sep 17 2007 Denis Leroy <denis@poolshark.org> - 2.20.0-1
- Update to new stable 2.20.0

* Thu Mar 15 2007 Denis Leroy <denis@poolshark.org> - 2.18.0-1
- Update to Gnome 2.18, to follow GConf2 version

* Mon Aug 28 2006 Denis Leroy <denis@poolshark.org> - 2.16.0-2
- FE6 Rebuild

* Mon Aug 21 2006 Denis Leroy <denis@poolshark.org> - 2.16.0-1
- Update to 2.16.0

* Sun Jun 25 2006 Denis Leroy <denis@poolshark.org> - 2.14.2
- Update to 2.14.2
- Added dist postfix to release field

* Mon Mar 20 2006 Denis Leroy <denis@poolshark.org> - 2.14.0-1
- Update to 2.14.0

* Tue Feb 28 2006 Denis Leroy <denis@poolshark.org> - 2.12.0-3
- Rebuild

* Fri Nov 25 2005 Denis Leroy <denis@poolshark.org> - 2.12.0-2
- Removed static libraries

* Mon Sep 19 2005 Denis Leroy <denis@poolshark.org> - 2.12.0-1
- Update to 2.12.0

* Sat May  7 2005 Denis Leroy <denis@poolshark.org> - 2.10.0-2
- Added patch to fix x86_64 compile

* Thu Apr 28 2005 Denis Leroy <denis@poolshark.org> - 2.10.0-1
- Upgrade to 2.10.0
- Added patch to fix gcc4 warning

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Jun 27 2004 Denis Leroy <denis@poolshark.org> - 0:2.6.1-0.fdr.1
- Upgrade to 2.6.1

* Fri Oct 31 2003 Michael Koziarski <michael@koziarski.org> - 2.0.1-0.fdr.2
- Fix BuildRequires
- Add specific version numbers to GConf dependency.

* Sat Oct 18 2003 Michael Koziarski <michael@koziarski.org> - 2.0.1-0.fdr.1
- Initial RPM creation
