# Maintainer: Dan Johansen <strit@manjaro.org>
# Contributor: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

pkgname=waydroid
pkgver=1.2.0
pkgrel=1
pkgdesc="A container-based approach to boot a full Android system on a regular Linux system"
arch=('any')
url='https://github.com/waydroid'
license=('GPL')
depends=('lxc' 'python' 'python-gbinder' 'python-gobject' 'nftables' 'dnsmasq')
makedepends=('git')
optdepends=('waydroid-image: Android image for use with waydroid'
  'python-pyclip: share clipboard with container')
install=waydroid.install
_commit="9a87b10bbfd9cc04c8259207233fadad9acbf5d3" # tags/1.2.0
source=("waydroid::git+https://github.com/waydroid/waydroid.git#commit=$_commit"
         gbinder.conf
         0001-dont-display-files-in-phosh.patch
         id.waydro.setup-waydroid.policy
         setup-waydroid.py)

pkgver() {
  cd waydroid
  git describe --tags | sed 's/^v//;s/-/+/g'
}

prepare() {
  cd waydroid
  patch -p2 -i ../0001-dont-display-files-in-phosh.patch
}

package() {
  cd waydroid
  install -Dm755 ../setup-waydroid.py "$pkgdir/usr/bin/setup-waydroid"
  install -Dm755 waydroid.py -t "$pkgdir/usr/lib/waydroid"
  ln -s /usr/lib/waydroid/waydroid.py "$pkgdir/usr/bin/waydroid"
  install -Dm644 data/Waydroid.desktop -t "$pkgdir/usr/share/applications"
  echo "X-Purism-FormFactor=Workstation;Mobile;" >> \
      "$pkgdir/usr/share/applications/Waydroid.desktop"   
  rm data/Waydroid.desktop
  cp -r tools data "$pkgdir/usr/lib/waydroid/" 
  install -Dm644 -t "$pkgdir/etc" "$srcdir/gbinder.conf"
  install -Dm644 -t "$pkgdir/etc/gbinder.d" gbinder/anbox.conf
  install -Dm644 -t "$pkgdir/usr/lib/systemd/system" \
      debian/waydroid-container.service
  install -Dm644 ../id.waydro.setup-waydroid.policy -t \
      "${pkgdir}"/usr/share/polkit-1/actions
}

sha256sums=('SKIP'
            '87a21d401281735ea026d715ea79b36e01f9af084198de2761b32d5b58a343dd'
            'bd1cc3de8e1c3dd62562063f01ad33c0406380e8746f1ed3ef083834de422db5'
            '16a155c099f012048e913bffd999b58d470aa74f2a3e30854204e6b0a5de4738'
            'cd5406465d7f6f25ee641a023bd726ec846de24c11f3a86fd720c8a7e9402765')
