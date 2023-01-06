# Access OnDemand Menu

![GitHub Release](https://img.shields.io/github/release/osc/bc_access_menu.svg)
[![GitHub License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

This is a menu item to display links back to the Access OnDemand Web portal within your OnDemand navigation bar.

## Pre-Install Configuration
Prior to installing the menu, you will need to allow the menu to be displayed on the OnDemand NavBar.
To do so, you will need to follow these instructions.

* ssh to the server that your ondemand instance is running on.
* Run vi /etc/ood/config/apps/dashboard/initializers/ood.rb and modify the file as explained below.
* Ensure that the following line is placed in the file.<br />
  ```NavConfig.categories=['Files','Jobs','Clusters','Interactive Apps','Reports','ACCESS'] ```
* Save the file and exit vi.

That's it for the prep work.

## Install
If you have not completed the Pre-Install Configuration, please do so now.

Once the Pre-Install Configuration is completed do the following.


* ssh to the server that your ondemand instance is running on.
* sudo rpm -Uvh https://yum.osc.edu/ondemand/latest/web/el8/x86_64/ondemand-bc_access_menu-1.0.2-1.el8.x86_64.rpm
* Once the install is completed, continue.
* Launch or Restart your OnDemand Dashboard
* Your ACCESS menu should now be a part of your OnDemand NavBar.

## License

* Documentation, website content, and logo is licensed under
  [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
* Code is licensed under MIT (see LICENSE.txt)
