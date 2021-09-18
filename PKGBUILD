# Maintainer: Dan Johansen <strit@manjaro.org>
# Contributor: Danct12 <danct12@disroot.org>
# Contributor: Bart Ribbers <bribbers@disroot.org>

pkgname=waydroid
pkgver=r30.15bbf62
pkgrel=2.0
pkgdesc="A container-based approach to boot a full Android system on a regular Linux system"
arch=('any')
url='https://github.com/waydroid'
license=('GPL')
depends=('lxc' 'python' 'python-gbinder' 'python-gobject')
makedepends=('git')
optdepends=('waydroid-image: Android image for use with waydroid')
_commit="15bbf62e43e8e2482aab809d24153fcbfc83a7bf"
source=("waydroid::git+https://github.com/waydroid/waydroid.git#commit=$_commit"
  gbinder.conf)

pkgver() {
  cd "$pkgname"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  cd waydroid
  install -dm755 "$pkgdir/usr/lib/waydroid"
  install -dm755 "$pkgdir/usr/share/applications"
  install -dm755 "$pkgdir/usr/bin"
  cp -r tools data "$pkgdir/usr/lib/waydroid/"
  mv "$pkgdir/usr/lib/waydroid/data/Waydroid.desktop" "$pkgdir/usr/share/applications"
  echo "X-Purism-FormFactor=Workstation;Mobile;" >> "$pkgdir/usr/share/applications/Waydroid.desktop"
  cp waydroid.py "$pkgdir/usr/lib/waydroid/"
  ln -s /usr/lib/waydroid/waydroid.py "$pkgdir/usr/bin/waydroid"

  install -Dm644 -t "$pkgdir/etc" "$srcdir/gbinder.conf"
  install -Dm644 -t "$pkgdir/etc/gbinder.d" gbinder/anbox.conf
  install -Dm644 -t "$pkgdir/usr/lib/systemd/system" debian/waydroid-container.service
}

sha256sums=('SKIP'
            '87a21d401281735ea026d715ea79b36e01f9af084198de2761b32d5b58a343dd')
