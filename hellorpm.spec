#
# hello package
#

# The infamous SUSE matrix:
# -------------------------
#
#                      	is_opensuse 	suse_version	sle_version
# openSUSE_13.1				1310
# SLE_12				1315		120000
# SLE_12_SP1				1315		120100
# openSUSE_Leap_42.1	1		1315		120100
# openSUSE_13.2				1320
# openSUSE_Factory	1		1330
# openSUSE_Tumbleweed	1		1330



Name: hellorpm

# %if 0%{?centos_version} == 600 || 0%{?rhel_version} == 600 || 0%{?fedora_version} || "%{prerelease}" == ""
# %if 0%{?rhel_version} || 0%{?centos_version} || 0%{?suse_version} == 1110
# %if 0%{?rhel_version} >= 600 || 0%{?centos_version} >= 600 || 0%{?suse_version} == 1110 || 0%{?fedora_version} == 23
# %if 0%{?suse_version} == 1110
# %if 0%{?rhel_version} == 600 || 0%{?centos_version} == 600
# %if 0%{?is_opensuse} || 0%{?suse_version} == 1320
# %if 0%{?suse_has_qt5} || 0%{?fedora_version} > 20 || 0%{?rhel_version} >= 700 || 0%{?centos_version} >= 700
# %if 0%{?fedora_version} >= 21 || 0%{?centos_version} >= 700 || 0%{?rhel_version} == 700
# %if 0%{?rhel_version} == 600 || 0%{?centos_version} == 600

%define base_version 1.0

Version:       	%{base_version}
Release:        0
License:        GPL-2.0+
Summary:        Hello package
Url:            https://github.com/zoquero/hellorpm
Group:          Productivity/Networking/Other
Source0:        %{name}-%{version}.tar.gz

# BuildRequires:  cmake >= 2.8.11
# BuildRequires:  gcc gcc-c++
# Obsoletes: libocsync0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build


%description
The hello rpm program

This is just a test   https://github.com/zoquero/hellorpm

Author
=======
Angel Galindo Muñoz <zoquero@gmail.com>



%prep
%setup -q

%build
#%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/usr/bin


%clean
rm -rf $RPM_BUILD_ROOT

%post

%preun


### %make_install

%check

%post

%postun

%posttrans

%files

%files
%defattr(755,root,root,755)
# %attr(0755, root, root) /usr/bin/%{name}
%attr(0755, root, root) /usr/bin/hellorpm
# %{_bindir}/hellorpm

%changelog
