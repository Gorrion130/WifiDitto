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
source=('linux-wifi-hotspot::git+https://github.com/lakinduakash/linux-wifi-hotspot' 'wifiditto' 'clearmacs.sh' 'change_mac' 'check_macs' 'stripmacs.py')
noextract=()
sha256sums=('SKIP'
            '251c56dda0da9f6c3cf93d282ed25a7d44da09dc715ed1bcd6d8e6f2d991ac54'
            'f1c0528a7d0a5cc53bb7bc79ac2e66282198557120b6aece11a5589824ff759d'
            'bfb2fff69e216adecb0d48576c172fe841e3a92d5be67c3ff9fd00ecfcff150d'
            'd0eebd1152dc806dd4e543fb8a921d05a7ec946c4807066819068052e73def8a'
            '262edc2e565c1c5314d679e973808d07d6b66d2289aa25a364cec19ac3f87f42')

prepare() {
	cd linux-wifi-hotspot
	make
}


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
	cd linux-wifi-hotspot
	sudo make install
}
