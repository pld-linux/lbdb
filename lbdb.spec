#
# Conditional build:
%bcond_without	tests		# build without tests
#
Summary:	The Little Brother's Database
Name:		lbdb
Version:	0.29
Release:	0.1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://www.spinnaker.de/debian/%{name}_%{version}.tar.gz
# Source0-md5:	1b29222036f564f45d22ce86284c0611
URL:		http://www.spinnaker.de/lbdb/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lbdbq is the client program for the little brother's database. It will
attempt to invoke various modules to gather information about persons
matching something. E.g., it may look at a list of addresses from which you
have received mail, it may look at YP maps, or it may try to finger
something@<various hosts>.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure --libdir=%{_libdir}/lbdb
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	install_prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*

%dir %{_libdir}/lbdb
%attr(755,root,root) %{_libdir}/lbdb/fetchaddr
%attr(755,root,root) %{_libdir}/lbdb/lbdb-munge
%attr(755,root,root) %{_libdir}/lbdb/lbdb_lib
%attr(755,root,root) %{_libdir}/lbdb/m*
%attr(755,root,root) %{_libdir}/lbdb/p*
%attr(755,root,root) %{_libdir}/lbdb/q*
%{_libdir}/lbdb/*.el
%{_mandir}/man1/*
