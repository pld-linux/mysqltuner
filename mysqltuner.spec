%include	/usr/lib/rpm/macros.perl
Summary:	High Performance MySQL Tuning Script
Name:		mysqltuner
Version:	0.9.9
Release:	0.3
License:	GPL v3+
Group:		Daemons
URL:		http://rackerhacker.com/mysqltuner/
Source0:	http://mysqltuner.com/%{name}.pl
Patch0:		%{name}.patch
# Source0-md5:	097ceed8577ff4dbed134970fd8781e4
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	mysql-client
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySQLTuner is a high-performance MySQL tuning script written in perl
that will provide you with a snapshot of a MySQL server's health.
Based on the statistics gathered, specific recommendations will be
provided that will increase a MySQL server's efficiency and
performance. The script gives you automated MySQL tuning that is on
the level of what you would receive from a MySQL DBA.

This script has been derived from many of the ideas in Matthew
Montgomery's MySQL tuning primer script.

%prep
%setup -q -c -T
%{__sed} -e 's,\r$,,' %{SOURCE0} > %{name}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install %{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/%{name}
