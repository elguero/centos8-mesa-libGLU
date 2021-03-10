#define gitdate 20120904

Name:           mesa-libGLU
Version:        9.0.0
Release:        15%{?dist}
Summary:        Mesa libGLU library

License:        MIT
URL:            http://mesa3d.org/
Source0:        ftp://ftp.freedesktop.org/pub/mesa/glu/glu-%{version}.tar.bz2
Source2:        make-git-snapshot.sh

Patch1: 0001-glu-initialize-PriorityQ-order-field-to-NULL-in-pqNe.patch
Patch2: 0002-Add-D-N-DEBUG-to-CFLAGS-dependent-on-enable-debug.patch
# https://gitlab.freedesktop.org/mesa/glu/-/commit/b293e7e843cff28c4b925fb0db988395c040d0ef#2d2a81b810dc90f672da760971fb984868f4529d
Patch3: 0003-Fix-build-error.patch

BuildRequires:  autoconf automake libtool
BuildRequires:  mesa-libGL-devel
#Requires:       
Provides: libGLU

%description
Mesa implementation of the standard GLU OpenGL utility API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gl-manpages
Provides:	libGLU-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n glu-%{?gitdate:%{gitdate}}%{?!gitdate:%{version}}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -v -i -f
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT%{_datadir}/man/man3/gl[A-Z]*

%ldconfig_post

%ldconfig_postun

%files
%{_libdir}/libGLU.so.1
%{_libdir}/libGLU.so.1.3.*

%files devel
%{_includedir}/GL/glu*.h
%{_libdir}/libGLU.so
%{_libdir}/pkgconfig/glu.pc

%changelog
* Fri Jun 29 2018 Adam Jackson <ajax@redhat.com> - 9.0.0-15
- Use ldconfig scriptlet macros

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 9.0.0-8
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Adam Jackson <ajax@redhat.com> 9.0.0-5
- Always autoreconf to pick up patch changes (#1070602)

* Mon Dec 09 2013 Adam Jackson <ajax@redhat.com> 9.0.0-4
- Sync with git (#1011823)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 18 2012 Adam Jackson <ajax@redhat.com> 9.0.0-1
- libGLU 9.0

* Mon Sep 10 2012 Dave Airlie <airlied@redhat.com> 9.0-0.2
- add back libGLU provides for now

* Tue Sep 04 2012 Adam Jackson <ajax@redhat.com> 9.0-0.1
- Initial packaging for split libGLU

