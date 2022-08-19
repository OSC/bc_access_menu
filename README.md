# Batch Connect - Access OnDemand Menu

![GitHub Release](https://img.shields.io/github/release/osc/bc_access_menu.svg)
[![GitHub License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

This is a menu item to display a link back to the Access OnDemand Web portal on the Navigation Bar of Open OnDemand.

## Install

Use Git to clone this app and checkout the desired branch/version you want to
use:

```sh
git clone git@github.com:OSC/bc_access_menu.git
cd bc_access_menu
git tag
git checkout <vN.N.N>
```

To activate this menu item on your Open OnDemand Portal, you need to:
```cd bc_access_menu
sudo cp -Rf bc_access_menu_about /var/www/ood/apps/sys/
sudo cp -Rf bc_access_menu_allocations /var/www/ood/apps/sys/
sudo cp -Rf bc_access_menu_metrics /var/www/ood/apps/sys/
sudo cp -Rf bc_access_menu_support /var/www/ood/apps/sys/
```

To update the app you would:

```sh
cd bc_access_menu
git fetch
git checkout <tag/branch>
```

Again, you do not need to restart the app as it isn't a Passenger app.

## Contributing

1. Fork it ( https://github.com/OSC/bc_access_menu/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## License

* Documentation, website content, and logo is licensed under
  [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
* Code is licensed under MIT (see LICENSE.txt)


