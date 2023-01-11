# Disable debuginfo as it causes issues with bundled gems that build libraries
%global debug_package %{nil}
%global repo_name bc_access_menu
%global app_about bc_access_menu_about
%global app_allocations bc_access_menu_allocations
%global app_support bc_access_menu_support
%global app_metrics bc_access_menu_metrics

%{!?package_version: %define package_version %{major}.%{minor}.%{patch}}
%{!?package_release: %define package_release 1}
%{!?git_tag: %define git_tag v%{package_version}}
%define git_tag_minus_v %(echo %{git_tag} | sed -r 's/^v//')

Name:     ondemand-%{repo_name}
Version:  %{package_version}
Release:  %{package_release}%{?dist}
Summary:  Batch Connect - ACCESS Menu

Group:    System Environment/Daemons
License:  MIT
URL:      https://github.com/OSC/%{repo_name}
Source0:  https://github.com/OSC/%{repo_name}/archive/%{git_tag}.tar.gz

Requires: ondemand => 2.0.0

# Disable automatic dependencies as it causes issues with bundled gems and
# node.js packages used in the apps
AutoReqProv: no

%description
A single deployment for ACCESS Service Providers to install ACCESS related links.


%prep
%setup -q -n %{repo_name}-%{git_tag_minus_v}


%build


%install
# process the about menu item 
%__mkdir_p %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_about}
%__cp -Rf ./%{app_about}/. %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_about}
echo v%{version} > %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_about}/VERSION

# process the allocations menu item 
%__mkdir_p %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_allocations}
%__cp -Rf ./%{app_allocations}/. %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_allocations}
echo v%{version} > %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_allocations}/VERSION

# process the support menu item 
%__mkdir_p %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_support}
%__cp -Rf ./%{app_support}/. %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_support}
echo v%{version} > %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_support}/VERSION

# process the metrics menu item 
%__mkdir_p %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_metrics}
%__cp -Rf ./%{app_metrics}/. %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_metrics}
echo v%{version} > %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_metrics}/VERSION


%files
%defattr(-,root,root)
%{_localstatedir}/www/ood/apps/sys/%{app_about}
%{_localstatedir}/www/ood/apps/sys/%{app_about}/manifest.yml
%{_localstatedir}/www/ood/apps/sys/%{app_allocations}
%{_localstatedir}/www/ood/apps/sys/%{app_allocations}/manifest.yml
%{_localstatedir}/www/ood/apps/sys/%{app_support}
%{_localstatedir}/www/ood/apps/sys/%{app_support}/manifest.yml
%{_localstatedir}/www/ood/apps/sys/%{app_metrics}
%{_localstatedir}/www/ood/apps/sys/%{app_metrics}/manifest.yml
