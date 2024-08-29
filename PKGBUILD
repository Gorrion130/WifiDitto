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
depends=('aircrack-ng' 'python3' 'macchanger' 'dnsmasq' 'gtk3' 'hostapd' 'qrencode' 'libpng')
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
sha256sum=$(git -c core.abbrev=no -C "$dir" archive --format tar "$fragval" | "${integ}sum" 2>&1)

prepare() {
	cd linux-wifi-hotspot
	make
}


package() {
	install -Dm644 ./clearmacs.sh "/bin/harvested/clearmacs.sh"
 	install -Dm644 ./change_mac "/bin/modules/change_mac"
  	install -Dm644 ./check_macs "/bin/modules/check_macs"
   	install -Dm644 ./stripmacs.py "/bin/modules/stripmacs.py"
 	install -Dm644 ./wifiditto "/bin/wifiditto"
	sudo cp -r harvested modules /bin
	cd linux-wifi-hotspot
	make install
}
