# This is an example PKGBUILD file. Use this as a start to creating your own,
# and remove these comments. For more information, see 'man PKGBUILD'.
# NOTE: Please fill out the license field for your package! If it is unknown,
# then please put 'unknown'.

# Maintainer: Your Name <youremail@domain.com>
pkgname=wifiditto
pkgver=1.0
pkgrel=1
epoch=
pkgdesc="A script to bypass a whole bunch of WiFi captive portals (e.g. at hotels, cruise ships etc.)"
arch=(any)
url="https://github.com/Gorrion130/WifiDitto"
license=('GPL')
groups=()
depends=('aircrack-ng' 'python3' 'macchanger' 'dnsmasq' 'gtk3' 'hostapd' 'qrencode' 'libpng' 'dhclient')
makedepends=('git' 'gcc' 'make' 'pkgconf')
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=('linux-router::git+https://github.com/garywill/linux-router' 'wifiditto' 'clearmacs.sh' 'change_mac' 'check_macs' 'stripmacs.py')
noextract=()
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

package() {
	sudo mkdir -p /bin/harvested
 	sudo mkdir -p /bin/modules
	sudo install -Dm644 ./clearmacs.sh "/bin/harvested/clearmacs.sh"
 	sudo install -Dm644 ./change_mac "/bin/modules/change_mac"
  	sudo install -Dm644 ./check_macs "/bin/modules/check_macs"
   	sudo install -Dm644 ./stripmacs.py "/bin/modules/stripmacs.py"
 	sudo install -Dm644 ./wifiditto "/bin/wifiditto"
        sudo chmod +x /bin/wifiditto
	sudo chmod +x /bin/modules/check_macs
 	sudo chmod +x /bin/modules/change_mac
  	sudo chmod +x /bin/modules/stripmacs.py
	cd linux-router
	sudo install -Dm644 ./lnxrouter "/bin/lnxrouter"
 	sudo chmod +x /bin/lnxrouter
}
