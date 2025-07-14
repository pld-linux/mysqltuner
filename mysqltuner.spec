# TODO
# - perlish which(1) or hardcode mysqladmin path in patch0
Summary:	High Performance MySQL Tuning Script
Name:		mysqltuner
Version:	1.2.0
Release:	1
License:	GPL v3+
Group:		Applications
Source0:	https://github.com/rackerhacker/MySQLTuner-perl/archive/v%{version}.tar.gz?/%{name}-%{version}.tgz
# Source0-md5:	036c0e0254c66016ef87cb5ddff4b8e1
Patch0:		%{name}.patch
URL:		https://github.com/rackerhacker/MySQLTuner-perl
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	mysql-client
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySQLTuner is a high-performance MySQL tuning script written in Perl
that will provide you with a snapshot of a MySQL server's health.
Based on the statistics gathered, specific recommendations will be
provided that will increase a MySQL server's efficiency and
performance. The script gives you automated MySQL tuning that is on
the level of what you would receive from a MySQL DBA.

This script has been derived from many of the ideas in Matthew
Montgomery's MySQL tuning primer script.

%prep
%setup -q -n MySQLTuner-perl-%{version}
%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install -p %{name}.pl $RPM_BUILD_ROOT%{_sbindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/%{name}
