# Access OnDemand Menu

![GitHub Release](https://img.shields.io/github/release/osc/bc_access_menu.svg)
[![GitHub License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

This is a menu to display links back to sections of the main ACCESS web page.

## Requirements
**The ACCESS OnDemand menu depends on your having Open OnDemand 2.x installed.**
<p>To install Open OnDemand 2.x, please use https://osc.github.io/ood-documentation/latest/installation.html</p>

## Install
On your OnDemand host, run<br /><br />
#### For RHEL8 or equivalent
```sudo dnf install https://yum.osc.edu/ondemand/latest/web/el8/x86_64/ondemand-bc_access_menu-1.0.2-1.el8.x86_64.rpm```

#### For RHEL7 or equivalent
```sudo yum install https://yum.osc.edu/ondemand/latest/web/el8/x86_64/ondemand-bc_access_menu-1.0.2-1.el8.x86_64.rpm```

#### Ubuntu
COMING SOON...

## Post Install
You have installed the menu, now you need to make it visible in the Navbar.

### If you **HAVE NOT** customized your OnDemand navbar, you will need to
Add
```NavConfig.categories=['Files','Jobs','Clusters','Interactive Apps','Reports','ACCESS'] ``` 
<br />
to **/etc/ood/config/apps/dashboard/initializers/ood.rb** on your OnDemand host.

### If you **HAVE** customized your OnDemand navbar, you will need to
Modify **/etc/ood/config/apps/dashboard/initializers/ood.rb** and add 'ACCESS' to your NavConfig.categories array.


### Your users will see the "ACCESS" menu the next time they login to OnDemand.

![ACCESS OnDemand Menu](https://github.com/OSC/bc_access_menu/blob/main/access_ondemand.PNG)

## License

* Documentation, website content, and logo is licensed under
  [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
* Code is licensed under MIT (see LICENSE.txt)


