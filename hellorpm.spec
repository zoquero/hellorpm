#
# Quick tutorial for building RPM on Ubuntu:
#
# $ apt-get install rpm
# $ mkdir -p ~/rpmbuild/SOURCES ~/rpmbuild/SPECS
# $ cp ....tar.gz ~/rpmbuild/SOURCES 
# $ rpmbuild -ba hellorpm.spec 
#

Summary: The "Hello RPM" program
Name: hellorpm
Version: 1.0
Release: 1%{?dist}
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
License: GPLv3+
Group: Development/Tools

# Requires(post): info
# Requires(preun): info

%description 
The "Hello RPM" program.
Is-a-must, absolutely.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/usr/bin

# %make_install
# %find_lang %{name}
# rm -f %{buildroot}/%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post
# /sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun
# if [ $1 = 0] ; then
# /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
# fi

%files
%defattr(755,root,root,755)
/usr/bin/hellorpm

# %files -f %{name}.lang
# %doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
# %{_mandir}/man1/hellorpm.1.gz
# %{_infodir}/%{name}.info.gz
# %{_bindir}/hellorpm

%changelog
* Sun Nov 13 2016 Angel <zoquero@gmail.com> 1.0
- Initial version of the package
# ORG-LIST-END-MARKER
