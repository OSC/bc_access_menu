# Disable debuginfo as it causes issues with bundled gems that build libraries
%global debug_package %{nil}
%global repo_name bc_access_menu
%global app_name1 bc_access_menu_operations
%global app_name2 bc_access_menu_allocations
%global app_name3 bc_access_menu_support
%global app_name4 bc_access_menu_metrics

%{!?package_version: %define package_version %{major}.%{minor}.%{patch}}
%{!?package_release: %define package_release 1}
%{!?git_tag: %define git_tag v%{package_version}}
%define git_tag_minus_v %(echo %{git_tag} | sed -r 's/^v//')

Name:     ondemand-%{app_name1}
Version:  %{package_version}
Release:  %{package_release}%{?dist}
Summary:  Batch Connect - ACCESS Menu

Group:    System Environment/Daemons
License:  MIT
URL:      https://github.com/OSC/%{repo_name}
Source0:  https://github.com/OSC/%{repo_name}/archive/%{git_tag}.tar.gz

Requires: ondemand

# Disable automatic dependencies as it causes issues with bundled gems and
# node.js packages used in the apps
AutoReqProv: no

%description
A single deployment for ACCESS Service Providers to install ACCESS related links.


%prep
%setup -q -n %{repo_name}-%{git_tag_minus_v}


%build


%install
%__mkdir_p %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name1}
%__cp -a ./. %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name1}/
echo v%{version} > %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name1}/VERSION
%__mkdir_p %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name2}
%__cp -a ./. %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name2}/
echo v%{version} > %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name2}/VERSION
%__mkdir_p %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name3}
%__cp -a ./. %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name3}/
echo v%{version} > %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name3}/VERSION
%__mkdir_p %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name4}
%__cp -a ./. %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name4}/
echo v%{version} > %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name4}/VERSION


%files
%defattr(-,root,root)
%{_localstatedir}/www/ood/apps/sys/%{app_name1}
%{_localstatedir}/www/ood/apps/sys/%{app_name1}/manifest.yml
%{_localstatedir}/www/ood/apps/sys/%{app_name2}
%{_localstatedir}/www/ood/apps/sys/%{app_name2}/manifest.yml
%{_localstatedir}/www/ood/apps/sys/%{app_name3}
%{_localstatedir}/www/ood/apps/sys/%{app_name3}/manifest.yml
%{_localstatedir}/www/ood/apps/sys/%{app_name4}
%{_localstatedir}/www/ood/apps/sys/%{app_name4}/manifest.yml
