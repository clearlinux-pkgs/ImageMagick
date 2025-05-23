#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v22
# autospec commit: 247c192
#
# Source0 file verified with key 0x89AB63D48277377A (lexie.parsimoniae@imagemagick.org)
#
Name     : ImageMagick
Version  : 7.1.1.47
Release  : 307
URL      : https://imagemagick.org/archive/ImageMagick-7.1.1-47.tar.gz
Source0  : https://imagemagick.org/archive/ImageMagick-7.1.1-47.tar.gz
Source1  : https://imagemagick.org/archive/ImageMagick-7.1.1-47.tar.gz.asc
Source2  : 89AB63D48277377A.pkey
Summary  : ImageMagick - convert, edit, and compose images (ABI @MAGICK_ABI_SUFFIX@)
Group    : Development/Tools
License  : MIT
Requires: ImageMagick-bin = %{version}-%{release}
Requires: ImageMagick-data = %{version}-%{release}
Requires: ImageMagick-lib = %{version}-%{release}
Requires: ImageMagick-license = %{version}-%{release}
Requires: ImageMagick-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : bzip2-dev
BuildRequires : curl-dev
BuildRequires : file
BuildRequires : gnupg
BuildRequires : lcms2-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libwebp-dev
BuildRequires : openexr-dev
BuildRequires : pkgconfig(bzip2)
BuildRequires : pkgconfig(cairo-svg)
BuildRequires : pkgconfig(fftw3)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(libgvc)
BuildRequires : pkgconfig(libjpeg)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libraw_r)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libtiff-4)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(libwebpdemux)
BuildRequires : pkgconfig(libwebpmux)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(libzip)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(xt)
BuildRequires : pkgconfig(zlib)
BuildRequires : sed
BuildRequires : xdg-utils
BuildRequires : zip
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-configure.c-stateless-configuration.patch

%description
This directory contains a number of PerlMagick demonstration scripts.  Just
type

%package bin
Summary: bin components for the ImageMagick package.
Group: Binaries
Requires: ImageMagick-data = %{version}-%{release}
Requires: ImageMagick-license = %{version}-%{release}

%description bin
bin components for the ImageMagick package.


%package data
Summary: data components for the ImageMagick package.
Group: Data

%description data
data components for the ImageMagick package.


%package dev
Summary: dev components for the ImageMagick package.
Group: Development
Requires: ImageMagick-lib = %{version}-%{release}
Requires: ImageMagick-bin = %{version}-%{release}
Requires: ImageMagick-data = %{version}-%{release}
Provides: ImageMagick-devel = %{version}-%{release}
Requires: ImageMagick = %{version}-%{release}

%description dev
dev components for the ImageMagick package.


%package doc
Summary: doc components for the ImageMagick package.
Group: Documentation
Requires: ImageMagick-man = %{version}-%{release}

%description doc
doc components for the ImageMagick package.


%package lib
Summary: lib components for the ImageMagick package.
Group: Libraries
Requires: ImageMagick-data = %{version}-%{release}
Requires: ImageMagick-license = %{version}-%{release}

%description lib
lib components for the ImageMagick package.


%package license
Summary: license components for the ImageMagick package.
Group: Default

%description license
license components for the ImageMagick package.


%package man
Summary: man components for the ImageMagick package.
Group: Default

%description man
man components for the ImageMagick package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 89AB63D48277377A' gpg.status
%setup -q -n ImageMagick-7.1.1-47
cd %{_builddir}/ImageMagick-7.1.1-47
%patch -P 1 -p1
pushd ..
cp -a ImageMagick-7.1.1-47 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1743430526
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --disable-openmp \
--enable-hugepages
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --disable-openmp \
--enable-hugepages
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1743430526
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ImageMagick
cp %{_builddir}/ImageMagick-7.1.1-47/Magick++/LICENSE %{buildroot}/usr/share/package-licenses/ImageMagick/e35708150f9609098e95bf25b6b5d4908f999666 || :
cp %{_builddir}/ImageMagick-7.1.1-47/NOTICE %{buildroot}/usr/share/package-licenses/ImageMagick/023310790971bdf976590c24416fcb00ec9785ec || :
cp %{_builddir}/ImageMagick-7.1.1-47/www/Magick++/COPYING %{buildroot}/usr/share/package-licenses/ImageMagick/9fbc78241e625956288a5ef6797d540b58197565 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
## install_append content
mkdir -p %{buildroot}/usr/share/defaults/ImageMagick-7/
mv config/policy.xml %{buildroot}/usr/share/defaults/ImageMagick-7/policy.xml
cp %{buildroot}/etc/ImageMagick-7/* %{buildroot}/usr/share/defaults/ImageMagick-7/
mkdir -p %{buildroot}/usr/share/ImageMagick-7/
install www/source/magic.xml %{buildroot}/usr/share/ImageMagick-7/magic.xml
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/ImageMagick-7.1.1/config-Q16HDRI/configure.xml

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/magick
/usr/bin/Magick++-config
/usr/bin/MagickCore-config
/usr/bin/MagickWand-config
/usr/bin/animate
/usr/bin/compare
/usr/bin/composite
/usr/bin/conjure
/usr/bin/convert
/usr/bin/display
/usr/bin/identify
/usr/bin/import
/usr/bin/magick
/usr/bin/magick-script
/usr/bin/mogrify
/usr/bin/montage
/usr/bin/stream

%files data
%defattr(-,root,root,-)
/usr/share/ImageMagick-7/english.xml
/usr/share/ImageMagick-7/francais.xml
/usr/share/ImageMagick-7/locale.xml
/usr/share/ImageMagick-7/magic.xml
/usr/share/defaults/ImageMagick-7/colors.xml
/usr/share/defaults/ImageMagick-7/delegates.xml
/usr/share/defaults/ImageMagick-7/log.xml
/usr/share/defaults/ImageMagick-7/mime.xml
/usr/share/defaults/ImageMagick-7/policy.xml
/usr/share/defaults/ImageMagick-7/quantization-table.xml
/usr/share/defaults/ImageMagick-7/thresholds.xml
/usr/share/defaults/ImageMagick-7/type-apple.xml
/usr/share/defaults/ImageMagick-7/type-dejavu.xml
/usr/share/defaults/ImageMagick-7/type-ghostscript.xml
/usr/share/defaults/ImageMagick-7/type-urw-base35-type1.xml
/usr/share/defaults/ImageMagick-7/type-urw-base35.xml
/usr/share/defaults/ImageMagick-7/type-windows.xml
/usr/share/defaults/ImageMagick-7/type.xml

%files dev
%defattr(-,root,root,-)
/usr/include/ImageMagick-7/Magick++.h
/usr/include/ImageMagick-7/Magick++/Blob.h
/usr/include/ImageMagick-7/Magick++/CoderInfo.h
/usr/include/ImageMagick-7/Magick++/Color.h
/usr/include/ImageMagick-7/Magick++/Drawable.h
/usr/include/ImageMagick-7/Magick++/Exception.h
/usr/include/ImageMagick-7/Magick++/Functions.h
/usr/include/ImageMagick-7/Magick++/Geometry.h
/usr/include/ImageMagick-7/Magick++/Image.h
/usr/include/ImageMagick-7/Magick++/Include.h
/usr/include/ImageMagick-7/Magick++/Montage.h
/usr/include/ImageMagick-7/Magick++/Pixels.h
/usr/include/ImageMagick-7/Magick++/ResourceLimits.h
/usr/include/ImageMagick-7/Magick++/STL.h
/usr/include/ImageMagick-7/Magick++/SecurityPolicy.h
/usr/include/ImageMagick-7/Magick++/Statistic.h
/usr/include/ImageMagick-7/Magick++/TypeMetric.h
/usr/include/ImageMagick-7/MagickCore/MagickCore.h
/usr/include/ImageMagick-7/MagickCore/animate.h
/usr/include/ImageMagick-7/MagickCore/annotate.h
/usr/include/ImageMagick-7/MagickCore/artifact.h
/usr/include/ImageMagick-7/MagickCore/attribute.h
/usr/include/ImageMagick-7/MagickCore/blob.h
/usr/include/ImageMagick-7/MagickCore/cache-view.h
/usr/include/ImageMagick-7/MagickCore/cache.h
/usr/include/ImageMagick-7/MagickCore/channel.h
/usr/include/ImageMagick-7/MagickCore/cipher.h
/usr/include/ImageMagick-7/MagickCore/client.h
/usr/include/ImageMagick-7/MagickCore/coder.h
/usr/include/ImageMagick-7/MagickCore/color.h
/usr/include/ImageMagick-7/MagickCore/colormap.h
/usr/include/ImageMagick-7/MagickCore/colorspace.h
/usr/include/ImageMagick-7/MagickCore/compare.h
/usr/include/ImageMagick-7/MagickCore/composite.h
/usr/include/ImageMagick-7/MagickCore/compress.h
/usr/include/ImageMagick-7/MagickCore/configure.h
/usr/include/ImageMagick-7/MagickCore/constitute.h
/usr/include/ImageMagick-7/MagickCore/decorate.h
/usr/include/ImageMagick-7/MagickCore/delegate.h
/usr/include/ImageMagick-7/MagickCore/deprecate.h
/usr/include/ImageMagick-7/MagickCore/display.h
/usr/include/ImageMagick-7/MagickCore/distort.h
/usr/include/ImageMagick-7/MagickCore/distribute-cache.h
/usr/include/ImageMagick-7/MagickCore/draw.h
/usr/include/ImageMagick-7/MagickCore/effect.h
/usr/include/ImageMagick-7/MagickCore/enhance.h
/usr/include/ImageMagick-7/MagickCore/exception.h
/usr/include/ImageMagick-7/MagickCore/feature.h
/usr/include/ImageMagick-7/MagickCore/fourier.h
/usr/include/ImageMagick-7/MagickCore/fx.h
/usr/include/ImageMagick-7/MagickCore/gem.h
/usr/include/ImageMagick-7/MagickCore/geometry.h
/usr/include/ImageMagick-7/MagickCore/histogram.h
/usr/include/ImageMagick-7/MagickCore/identify.h
/usr/include/ImageMagick-7/MagickCore/image-view.h
/usr/include/ImageMagick-7/MagickCore/image.h
/usr/include/ImageMagick-7/MagickCore/layer.h
/usr/include/ImageMagick-7/MagickCore/linked-list.h
/usr/include/ImageMagick-7/MagickCore/list.h
/usr/include/ImageMagick-7/MagickCore/locale_.h
/usr/include/ImageMagick-7/MagickCore/log.h
/usr/include/ImageMagick-7/MagickCore/magic.h
/usr/include/ImageMagick-7/MagickCore/magick-baseconfig.h
/usr/include/ImageMagick-7/MagickCore/magick-config.h
/usr/include/ImageMagick-7/MagickCore/magick-type.h
/usr/include/ImageMagick-7/MagickCore/magick.h
/usr/include/ImageMagick-7/MagickCore/matrix.h
/usr/include/ImageMagick-7/MagickCore/memory_.h
/usr/include/ImageMagick-7/MagickCore/method-attribute.h
/usr/include/ImageMagick-7/MagickCore/methods.h
/usr/include/ImageMagick-7/MagickCore/mime.h
/usr/include/ImageMagick-7/MagickCore/module.h
/usr/include/ImageMagick-7/MagickCore/monitor.h
/usr/include/ImageMagick-7/MagickCore/montage.h
/usr/include/ImageMagick-7/MagickCore/morphology.h
/usr/include/ImageMagick-7/MagickCore/nt-base.h
/usr/include/ImageMagick-7/MagickCore/opencl.h
/usr/include/ImageMagick-7/MagickCore/option.h
/usr/include/ImageMagick-7/MagickCore/paint.h
/usr/include/ImageMagick-7/MagickCore/pixel-accessor.h
/usr/include/ImageMagick-7/MagickCore/pixel.h
/usr/include/ImageMagick-7/MagickCore/policy.h
/usr/include/ImageMagick-7/MagickCore/prepress.h
/usr/include/ImageMagick-7/MagickCore/profile.h
/usr/include/ImageMagick-7/MagickCore/property.h
/usr/include/ImageMagick-7/MagickCore/quantize.h
/usr/include/ImageMagick-7/MagickCore/quantum.h
/usr/include/ImageMagick-7/MagickCore/random_.h
/usr/include/ImageMagick-7/MagickCore/registry.h
/usr/include/ImageMagick-7/MagickCore/resample.h
/usr/include/ImageMagick-7/MagickCore/resize.h
/usr/include/ImageMagick-7/MagickCore/resource_.h
/usr/include/ImageMagick-7/MagickCore/segment.h
/usr/include/ImageMagick-7/MagickCore/semaphore.h
/usr/include/ImageMagick-7/MagickCore/shear.h
/usr/include/ImageMagick-7/MagickCore/signature.h
/usr/include/ImageMagick-7/MagickCore/splay-tree.h
/usr/include/ImageMagick-7/MagickCore/static.h
/usr/include/ImageMagick-7/MagickCore/statistic.h
/usr/include/ImageMagick-7/MagickCore/stream.h
/usr/include/ImageMagick-7/MagickCore/string_.h
/usr/include/ImageMagick-7/MagickCore/studio.h
/usr/include/ImageMagick-7/MagickCore/threshold.h
/usr/include/ImageMagick-7/MagickCore/timer.h
/usr/include/ImageMagick-7/MagickCore/token.h
/usr/include/ImageMagick-7/MagickCore/transform.h
/usr/include/ImageMagick-7/MagickCore/type.h
/usr/include/ImageMagick-7/MagickCore/utility.h
/usr/include/ImageMagick-7/MagickCore/version.h
/usr/include/ImageMagick-7/MagickCore/vision.h
/usr/include/ImageMagick-7/MagickCore/visual-effects.h
/usr/include/ImageMagick-7/MagickCore/widget.h
/usr/include/ImageMagick-7/MagickCore/xml-tree.h
/usr/include/ImageMagick-7/MagickCore/xwindow.h
/usr/include/ImageMagick-7/MagickWand/MagickWand.h
/usr/include/ImageMagick-7/MagickWand/animate.h
/usr/include/ImageMagick-7/MagickWand/compare.h
/usr/include/ImageMagick-7/MagickWand/composite.h
/usr/include/ImageMagick-7/MagickWand/conjure.h
/usr/include/ImageMagick-7/MagickWand/deprecate.h
/usr/include/ImageMagick-7/MagickWand/display.h
/usr/include/ImageMagick-7/MagickWand/drawing-wand.h
/usr/include/ImageMagick-7/MagickWand/identify.h
/usr/include/ImageMagick-7/MagickWand/import.h
/usr/include/ImageMagick-7/MagickWand/magick-cli.h
/usr/include/ImageMagick-7/MagickWand/magick-image.h
/usr/include/ImageMagick-7/MagickWand/magick-property.h
/usr/include/ImageMagick-7/MagickWand/method-attribute.h
/usr/include/ImageMagick-7/MagickWand/mogrify.h
/usr/include/ImageMagick-7/MagickWand/montage.h
/usr/include/ImageMagick-7/MagickWand/operation.h
/usr/include/ImageMagick-7/MagickWand/pixel-iterator.h
/usr/include/ImageMagick-7/MagickWand/pixel-wand.h
/usr/include/ImageMagick-7/MagickWand/stream.h
/usr/include/ImageMagick-7/MagickWand/wand-view.h
/usr/include/ImageMagick-7/MagickWand/wandcli.h
/usr/lib64/libMagick++-7.Q16HDRI.so
/usr/lib64/libMagickCore-7.Q16HDRI.so
/usr/lib64/libMagickWand-7.Q16HDRI.so
/usr/lib64/pkgconfig/ImageMagick-7.Q16HDRI.pc
/usr/lib64/pkgconfig/ImageMagick.pc
/usr/lib64/pkgconfig/Magick++-7.Q16HDRI.pc
/usr/lib64/pkgconfig/Magick++.pc
/usr/lib64/pkgconfig/MagickCore-7.Q16HDRI.pc
/usr/lib64/pkgconfig/MagickCore.pc
/usr/lib64/pkgconfig/MagickWand-7.Q16HDRI.pc
/usr/lib64/pkgconfig/MagickWand.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/ImageMagick-7/LICENSE
/usr/share/doc/ImageMagick-7/images/ImageMagick.ico
/usr/share/doc/ImageMagick-7/images/affine.png
/usr/share/doc/ImageMagick-7/images/annotate.png
/usr/share/doc/ImageMagick-7/images/arc.png
/usr/share/doc/ImageMagick-7/images/atop.gif
/usr/share/doc/ImageMagick-7/images/background.jpg
/usr/share/doc/ImageMagick-7/images/bitcoin.svg
/usr/share/doc/ImageMagick-7/images/black.png
/usr/share/doc/ImageMagick-7/images/bluebells_clipped.jpg
/usr/share/doc/ImageMagick-7/images/bluebells_darker.jpg
/usr/share/doc/ImageMagick-7/images/bluebells_lin.jpg
/usr/share/doc/ImageMagick-7/images/bluebells_log.jpg
/usr/share/doc/ImageMagick-7/images/button.gif
/usr/share/doc/ImageMagick-7/images/color-thresholding-gray.gif
/usr/share/doc/ImageMagick-7/images/color-thresholding-hsv-rgb.gif
/usr/share/doc/ImageMagick-7/images/color-thresholding-hsv.gif
/usr/share/doc/ImageMagick-7/images/color-thresholding-rgb.gif
/usr/share/doc/ImageMagick-7/images/color-thresholding.gif
/usr/share/doc/ImageMagick-7/images/color-thresholding.jpg
/usr/share/doc/ImageMagick-7/images/configure.jpg
/usr/share/doc/ImageMagick-7/images/convex-hull-barn-closure.jpg
/usr/share/doc/ImageMagick-7/images/convex-hull-barn.jpg
/usr/share/doc/ImageMagick-7/images/convex-hull-blocks-closure.png
/usr/share/doc/ImageMagick-7/images/convex-hull-blocks.png
/usr/share/doc/ImageMagick-7/images/convex-hull.png
/usr/share/doc/ImageMagick-7/images/cylinder_shaded.png
/usr/share/doc/ImageMagick-7/images/difference.png
/usr/share/doc/ImageMagick-7/images/examples.jpg
/usr/share/doc/ImageMagick-7/images/frame.jpg
/usr/share/doc/ImageMagick-7/images/fuzzy-magick.png
/usr/share/doc/ImageMagick-7/images/gaussian-blur.png
/usr/share/doc/ImageMagick-7/images/granite.png
/usr/share/doc/ImageMagick-7/images/imade_art2.jpg
/usr/share/doc/ImageMagick-7/images/label.gif
/usr/share/doc/ImageMagick-7/images/logo-sm-flop.png
/usr/share/doc/ImageMagick-7/images/logo-sm-fx.png
/usr/share/doc/ImageMagick-7/images/logo-sm.png
/usr/share/doc/ImageMagick-7/images/logo.eps
/usr/share/doc/ImageMagick-7/images/logo.jpg
/usr/share/doc/ImageMagick-7/images/logo.png
/usr/share/doc/ImageMagick-7/images/montage.jpg
/usr/share/doc/ImageMagick-7/images/mountains-clahe.jpg
/usr/share/doc/ImageMagick-7/images/mountains-equalize.jpg
/usr/share/doc/ImageMagick-7/images/mountains.jpg
/usr/share/doc/ImageMagick-7/images/navy.png
/usr/share/doc/ImageMagick-7/images/objects.gif
/usr/share/doc/ImageMagick-7/images/objects.jpg
/usr/share/doc/ImageMagick-7/images/objects.png
/usr/share/doc/ImageMagick-7/images/over.gif
/usr/share/doc/ImageMagick-7/images/patterns/bricks.png
/usr/share/doc/ImageMagick-7/images/patterns/checkerboard.png
/usr/share/doc/ImageMagick-7/images/patterns/circles.png
/usr/share/doc/ImageMagick-7/images/patterns/crosshatch.png
/usr/share/doc/ImageMagick-7/images/patterns/crosshatch30.png
/usr/share/doc/ImageMagick-7/images/patterns/crosshatch45.png
/usr/share/doc/ImageMagick-7/images/patterns/fishscales.png
/usr/share/doc/ImageMagick-7/images/patterns/gray0.png
/usr/share/doc/ImageMagick-7/images/patterns/gray10.png
/usr/share/doc/ImageMagick-7/images/patterns/gray100.png
/usr/share/doc/ImageMagick-7/images/patterns/gray15.png
/usr/share/doc/ImageMagick-7/images/patterns/gray20.png
/usr/share/doc/ImageMagick-7/images/patterns/gray25.png
/usr/share/doc/ImageMagick-7/images/patterns/gray30.png
/usr/share/doc/ImageMagick-7/images/patterns/gray35.png
/usr/share/doc/ImageMagick-7/images/patterns/gray40.png
/usr/share/doc/ImageMagick-7/images/patterns/gray45.png
/usr/share/doc/ImageMagick-7/images/patterns/gray5.png
/usr/share/doc/ImageMagick-7/images/patterns/gray50.png
/usr/share/doc/ImageMagick-7/images/patterns/gray55.png
/usr/share/doc/ImageMagick-7/images/patterns/gray60.png
/usr/share/doc/ImageMagick-7/images/patterns/gray65.png
/usr/share/doc/ImageMagick-7/images/patterns/gray70.png
/usr/share/doc/ImageMagick-7/images/patterns/gray75.png
/usr/share/doc/ImageMagick-7/images/patterns/gray80.png
/usr/share/doc/ImageMagick-7/images/patterns/gray85.png
/usr/share/doc/ImageMagick-7/images/patterns/gray90.png
/usr/share/doc/ImageMagick-7/images/patterns/gray95.png
/usr/share/doc/ImageMagick-7/images/patterns/hexagons.png
/usr/share/doc/ImageMagick-7/images/patterns/horizontal.png
/usr/share/doc/ImageMagick-7/images/patterns/horizontal2.png
/usr/share/doc/ImageMagick-7/images/patterns/horizontal3.png
/usr/share/doc/ImageMagick-7/images/patterns/horizontalsaw.png
/usr/share/doc/ImageMagick-7/images/patterns/hs_bdiagonal.png
/usr/share/doc/ImageMagick-7/images/patterns/hs_cross.png
/usr/share/doc/ImageMagick-7/images/patterns/hs_diagcross.png
/usr/share/doc/ImageMagick-7/images/patterns/hs_fdiagonal.png
/usr/share/doc/ImageMagick-7/images/patterns/hs_horizontal.png
/usr/share/doc/ImageMagick-7/images/patterns/hs_vertical.png
/usr/share/doc/ImageMagick-7/images/patterns/left30.png
/usr/share/doc/ImageMagick-7/images/patterns/left45.png
/usr/share/doc/ImageMagick-7/images/patterns/leftshingle.png
/usr/share/doc/ImageMagick-7/images/patterns/octagons.png
/usr/share/doc/ImageMagick-7/images/patterns/right30.png
/usr/share/doc/ImageMagick-7/images/patterns/right45.png
/usr/share/doc/ImageMagick-7/images/patterns/rightshingle.png
/usr/share/doc/ImageMagick-7/images/patterns/smallfishscales.png
/usr/share/doc/ImageMagick-7/images/patterns/vertical.png
/usr/share/doc/ImageMagick-7/images/patterns/vertical2.png
/usr/share/doc/ImageMagick-7/images/patterns/vertical3.png
/usr/share/doc/ImageMagick-7/images/patterns/verticalbricks.png
/usr/share/doc/ImageMagick-7/images/patterns/verticalleftshingle.png
/usr/share/doc/ImageMagick-7/images/patterns/verticalrightshingle.png
/usr/share/doc/ImageMagick-7/images/patterns/verticalsaw.png
/usr/share/doc/ImageMagick-7/images/piechart.png
/usr/share/doc/ImageMagick-7/images/radial-gradient.png
/usr/share/doc/ImageMagick-7/images/reconstruct.jpg
/usr/share/doc/ImageMagick-7/images/red-ball.png
/usr/share/doc/ImageMagick-7/images/red-circle.png
/usr/share/doc/ImageMagick-7/images/right.gif
/usr/share/doc/ImageMagick-7/images/rose-over.png
/usr/share/doc/ImageMagick-7/images/rose-sigmoidal.png
/usr/share/doc/ImageMagick-7/images/rose.jpg
/usr/share/doc/ImageMagick-7/images/rose.png
/usr/share/doc/ImageMagick-7/images/rose.pnm
/usr/share/doc/ImageMagick-7/images/script.png
/usr/share/doc/ImageMagick-7/images/smile.gif
/usr/share/doc/ImageMagick-7/images/sponsor.jpg
/usr/share/doc/ImageMagick-7/images/sprite.jpg
/usr/share/doc/ImageMagick-7/images/t-shirt.png
/usr/share/doc/ImageMagick-7/images/wand.ico
/usr/share/doc/ImageMagick-7/images/wand.png
/usr/share/doc/ImageMagick-7/images/white-highlight.png
/usr/share/doc/ImageMagick-7/images/wizard.jpg
/usr/share/doc/ImageMagick-7/images/wizard.png
/usr/share/doc/ImageMagick-7/index.html
/usr/share/doc/ImageMagick-7/www/Magick++/Blob.html
/usr/share/doc/ImageMagick-7/www/Magick++/Cache.fig
/usr/share/doc/ImageMagick-7/www/Magick++/Cache.png
/usr/share/doc/ImageMagick-7/www/Magick++/Cache.svg
/usr/share/doc/ImageMagick-7/www/Magick++/ChangeLog.html
/usr/share/doc/ImageMagick-7/www/Magick++/CoderInfo.html
/usr/share/doc/ImageMagick-7/www/Magick++/Color.html
/usr/share/doc/ImageMagick-7/www/Magick++/Documentation.html
/usr/share/doc/ImageMagick-7/www/Magick++/Drawable.html
/usr/share/doc/ImageMagick-7/www/Magick++/Drawable_example_1.png
/usr/share/doc/ImageMagick-7/www/Magick++/Enumerations.html
/usr/share/doc/ImageMagick-7/www/Magick++/Exception.html
/usr/share/doc/ImageMagick-7/www/Magick++/FormatCharacters.html
/usr/share/doc/ImageMagick-7/www/Magick++/Future.html
/usr/share/doc/ImageMagick-7/www/Magick++/Geometry.html
/usr/share/doc/ImageMagick-7/www/Magick++/Image++.html
/usr/share/doc/ImageMagick-7/www/Magick++/Image.fig
/usr/share/doc/ImageMagick-7/www/Magick++/Image.html
/usr/share/doc/ImageMagick-7/www/Magick++/Image.png
/usr/share/doc/ImageMagick-7/www/Magick++/ImageDesign.html
/usr/share/doc/ImageMagick-7/www/Magick++/ImageMagick.png
/usr/share/doc/ImageMagick-7/www/Magick++/Install.html
/usr/share/doc/ImageMagick-7/www/Magick++/Magick++.png
/usr/share/doc/ImageMagick-7/www/Magick++/Montage.html
/usr/share/doc/ImageMagick-7/www/Magick++/NEWS.html
/usr/share/doc/ImageMagick-7/www/Magick++/PixelPacket.html
/usr/share/doc/ImageMagick-7/www/Magick++/Pixels.html
/usr/share/doc/ImageMagick-7/www/Magick++/Quantum.html
/usr/share/doc/ImageMagick-7/www/Magick++/README.txt
/usr/share/doc/ImageMagick-7/www/Magick++/STL.html
/usr/share/doc/ImageMagick-7/www/Magick++/TypeMetric.html
/usr/share/doc/ImageMagick-7/www/Magick++/index.html
/usr/share/doc/ImageMagick-7/www/Magick++/magick.css
/usr/share/doc/ImageMagick-7/www/Magick++/montage-sample-framed.jpg
/usr/share/doc/ImageMagick-7/www/Magick++/right_triangle.png
/usr/share/doc/ImageMagick-7/www/Magick++/thumbnail-anatomy-framed.fig
/usr/share/doc/ImageMagick-7/www/Magick++/thumbnail-anatomy-framed.jpg
/usr/share/doc/ImageMagick-7/www/Magick++/thumbnail-anatomy-plain.fig
/usr/share/doc/ImageMagick-7/www/Magick++/thumbnail-anatomy-plain.jpg
/usr/share/doc/ImageMagick-7/www/Magick++/thumbnail-sample-framed.jpg
/usr/share/doc/ImageMagick-7/www/Magick++/thumbnail-sample-plain.jpg
/usr/share/doc/ImageMagick-7/www/advanced-linux-installation.html
/usr/share/doc/ImageMagick-7/www/advanced-unix-installation.html
/usr/share/doc/ImageMagick-7/www/advanced-windows-installation.html
/usr/share/doc/ImageMagick-7/www/animate.html
/usr/share/doc/ImageMagick-7/www/api/Image++.html
/usr/share/doc/ImageMagick-7/www/api/animate.html
/usr/share/doc/ImageMagick-7/www/api/annotate.html
/usr/share/doc/ImageMagick-7/www/api/attribute.html
/usr/share/doc/ImageMagick-7/www/api/blob.html
/usr/share/doc/ImageMagick-7/www/api/cache-view.html
/usr/share/doc/ImageMagick-7/www/api/cache.html
/usr/share/doc/ImageMagick-7/www/api/channel.html
/usr/share/doc/ImageMagick-7/www/api/cipher.html
/usr/share/doc/ImageMagick-7/www/api/color.html
/usr/share/doc/ImageMagick-7/www/api/colormap.html
/usr/share/doc/ImageMagick-7/www/api/colorspace.html
/usr/share/doc/ImageMagick-7/www/api/compare.html
/usr/share/doc/ImageMagick-7/www/api/composite.html
/usr/share/doc/ImageMagick-7/www/api/constitute.html
/usr/share/doc/ImageMagick-7/www/api/decorate.html
/usr/share/doc/ImageMagick-7/www/api/deprecate.html
/usr/share/doc/ImageMagick-7/www/api/display.html
/usr/share/doc/ImageMagick-7/www/api/distort.html
/usr/share/doc/ImageMagick-7/www/api/draw.html
/usr/share/doc/ImageMagick-7/www/api/drawing-wand.html
/usr/share/doc/ImageMagick-7/www/api/effect.html
/usr/share/doc/ImageMagick-7/www/api/enhance.html
/usr/share/doc/ImageMagick-7/www/api/exception.html
/usr/share/doc/ImageMagick-7/www/api/feature.html
/usr/share/doc/ImageMagick-7/www/api/fourier.html
/usr/share/doc/ImageMagick-7/www/api/fx.html
/usr/share/doc/ImageMagick-7/www/api/histogram.html
/usr/share/doc/ImageMagick-7/www/api/image-view.html
/usr/share/doc/ImageMagick-7/www/api/image.html
/usr/share/doc/ImageMagick-7/www/api/layer.html
/usr/share/doc/ImageMagick-7/www/api/list.html
/usr/share/doc/ImageMagick-7/www/api/magick++-classes.html
/usr/share/doc/ImageMagick-7/www/api/magick-deprecate.html
/usr/share/doc/ImageMagick-7/www/api/magick-image.html
/usr/share/doc/ImageMagick-7/www/api/magick-property.html
/usr/share/doc/ImageMagick-7/www/api/magick-wand.html
/usr/share/doc/ImageMagick-7/www/api/magick.html
/usr/share/doc/ImageMagick-7/www/api/memory.html
/usr/share/doc/ImageMagick-7/www/api/mime.html
/usr/share/doc/ImageMagick-7/www/api/module.html
/usr/share/doc/ImageMagick-7/www/api/mogrify.html
/usr/share/doc/ImageMagick-7/www/api/monitor.html
/usr/share/doc/ImageMagick-7/www/api/montage.html
/usr/share/doc/ImageMagick-7/www/api/morphology.html
/usr/share/doc/ImageMagick-7/www/api/paint.html
/usr/share/doc/ImageMagick-7/www/api/pixel-iterator.html
/usr/share/doc/ImageMagick-7/www/api/pixel-wand.html
/usr/share/doc/ImageMagick-7/www/api/profile.html
/usr/share/doc/ImageMagick-7/www/api/property.html
/usr/share/doc/ImageMagick-7/www/api/quantize.html
/usr/share/doc/ImageMagick-7/www/api/registry.html
/usr/share/doc/ImageMagick-7/www/api/resize.html
/usr/share/doc/ImageMagick-7/www/api/resource.html
/usr/share/doc/ImageMagick-7/www/api/segment.html
/usr/share/doc/ImageMagick-7/www/api/shear.html
/usr/share/doc/ImageMagick-7/www/api/signature.html
/usr/share/doc/ImageMagick-7/www/api/statistic.html
/usr/share/doc/ImageMagick-7/www/api/stream.html
/usr/share/doc/ImageMagick-7/www/api/transform.html
/usr/share/doc/ImageMagick-7/www/api/version.html
/usr/share/doc/ImageMagick-7/www/api/vision.html
/usr/share/doc/ImageMagick-7/www/api/wand-view.html
/usr/share/doc/ImageMagick-7/www/architecture.html
/usr/share/doc/ImageMagick-7/www/assets/bootstrap.bundle.min.js
/usr/share/doc/ImageMagick-7/www/assets/bootstrap.min.css
/usr/share/doc/ImageMagick-7/www/assets/color-modes.js
/usr/share/doc/ImageMagick-7/www/changelog.html
/usr/share/doc/ImageMagick-7/www/cipher.html
/usr/share/doc/ImageMagick-7/www/cite.html
/usr/share/doc/ImageMagick-7/www/clahe.html
/usr/share/doc/ImageMagick-7/www/color-management.html
/usr/share/doc/ImageMagick-7/www/color-thresholding.html
/usr/share/doc/ImageMagick-7/www/color.html
/usr/share/doc/ImageMagick-7/www/command-line-options.html
/usr/share/doc/ImageMagick-7/www/command-line-processing.html
/usr/share/doc/ImageMagick-7/www/command-line-tools.html
/usr/share/doc/ImageMagick-7/www/compare.html
/usr/share/doc/ImageMagick-7/www/compose.html
/usr/share/doc/ImageMagick-7/www/composite.html
/usr/share/doc/ImageMagick-7/www/conjure.html
/usr/share/doc/ImageMagick-7/www/connected-components.html
/usr/share/doc/ImageMagick-7/www/contact.html
/usr/share/doc/ImageMagick-7/www/convert.html
/usr/share/doc/ImageMagick-7/www/convex-hull.html
/usr/share/doc/ImageMagick-7/www/defines.html
/usr/share/doc/ImageMagick-7/www/develop.html
/usr/share/doc/ImageMagick-7/www/display.html
/usr/share/doc/ImageMagick-7/www/distribute-pixel-cache.html
/usr/share/doc/ImageMagick-7/www/download.html
/usr/share/doc/ImageMagick-7/www/escape.html
/usr/share/doc/ImageMagick-7/www/examples.html
/usr/share/doc/ImageMagick-7/www/exception.html
/usr/share/doc/ImageMagick-7/www/export.html
/usr/share/doc/ImageMagick-7/www/favicon.ico
/usr/share/doc/ImageMagick-7/www/formats.html
/usr/share/doc/ImageMagick-7/www/fx.html
/usr/share/doc/ImageMagick-7/www/gradient.html
/usr/share/doc/ImageMagick-7/www/high-dynamic-range.html
/usr/share/doc/ImageMagick-7/www/history.html
/usr/share/doc/ImageMagick-7/www/identify.html
/usr/share/doc/ImageMagick-7/www/import.html
/usr/share/doc/ImageMagick-7/www/index.html
/usr/share/doc/ImageMagick-7/www/install-source.html
/usr/share/doc/ImageMagick-7/www/jp2.html
/usr/share/doc/ImageMagick-7/www/license.html
/usr/share/doc/ImageMagick-7/www/links.html
/usr/share/doc/ImageMagick-7/www/magick++.html
/usr/share/doc/ImageMagick-7/www/magick-cache.html
/usr/share/doc/ImageMagick-7/www/magick-core.html
/usr/share/doc/ImageMagick-7/www/magick-script.html
/usr/share/doc/ImageMagick-7/www/magick-vector-graphics.html
/usr/share/doc/ImageMagick-7/www/magick-wand.html
/usr/share/doc/ImageMagick-7/www/magick.html
/usr/share/doc/ImageMagick-7/www/miff.html
/usr/share/doc/ImageMagick-7/www/mirror.html
/usr/share/doc/ImageMagick-7/www/mogrify.html
/usr/share/doc/ImageMagick-7/www/montage.html
/usr/share/doc/ImageMagick-7/www/motion-picture.html
/usr/share/doc/ImageMagick-7/www/multispectral-imagery.html
/usr/share/doc/ImageMagick-7/www/news.html
/usr/share/doc/ImageMagick-7/www/opencl.html
/usr/share/doc/ImageMagick-7/www/openmp.html
/usr/share/doc/ImageMagick-7/www/perl-magick.html
/usr/share/doc/ImageMagick-7/www/porting.html
/usr/share/doc/ImageMagick-7/www/privacy-policy.html
/usr/share/doc/ImageMagick-7/www/quantize.html
/usr/share/doc/ImageMagick-7/www/resources.html
/usr/share/doc/ImageMagick-7/www/search.html
/usr/share/doc/ImageMagick-7/www/security-policy.html
/usr/share/doc/ImageMagick-7/www/sitemap.html
/usr/share/doc/ImageMagick-7/www/source/analyze.c
/usr/share/doc/ImageMagick-7/www/source/coder.xml
/usr/share/doc/ImageMagick-7/www/source/colors.xml
/usr/share/doc/ImageMagick-7/www/source/configure.xml
/usr/share/doc/ImageMagick-7/www/source/contrast.c
/usr/share/doc/ImageMagick-7/www/source/core.c
/usr/share/doc/ImageMagick-7/www/source/delegates.xml
/usr/share/doc/ImageMagick-7/www/source/english.xml
/usr/share/doc/ImageMagick-7/www/source/examples.pl
/usr/share/doc/ImageMagick-7/www/source/francais.xml
/usr/share/doc/ImageMagick-7/www/source/incantation.msl
/usr/share/doc/ImageMagick-7/www/source/locale.xml
/usr/share/doc/ImageMagick-7/www/source/log.xml
/usr/share/doc/ImageMagick-7/www/source/magic.xml
/usr/share/doc/ImageMagick-7/www/source/mgk.c
/usr/share/doc/ImageMagick-7/www/source/mime.xml
/usr/share/doc/ImageMagick-7/www/source/piechart.mvg
/usr/share/doc/ImageMagick-7/www/source/piechart.svg
/usr/share/doc/ImageMagick-7/www/source/policy.xml
/usr/share/doc/ImageMagick-7/www/source/quantization-table.xml
/usr/share/doc/ImageMagick-7/www/source/thresholds.xml
/usr/share/doc/ImageMagick-7/www/source/type-apple.xml
/usr/share/doc/ImageMagick-7/www/source/type-dejavu.xml
/usr/share/doc/ImageMagick-7/www/source/type-ghostscript.xml
/usr/share/doc/ImageMagick-7/www/source/type-urw-base35.xml
/usr/share/doc/ImageMagick-7/www/source/type-windows.xml
/usr/share/doc/ImageMagick-7/www/source/type.xml
/usr/share/doc/ImageMagick-7/www/source/wand.c
/usr/share/doc/ImageMagick-7/www/stream.html
/usr/share/doc/ImageMagick-7/www/support.html
/usr/share/doc/ImageMagick-7/www/vpat.html
/usr/share/doc/ImageMagick-7/www/wand.png
/usr/share/doc/ImageMagick-7/www/webp.html

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libMagick++-7.Q16HDRI.so.5.0.0
/V3/usr/lib64/libMagickCore-7.Q16HDRI.so.10.0.2
/V3/usr/lib64/libMagickWand-7.Q16HDRI.so.10.0.2
/usr/lib64/libMagick++-7.Q16HDRI.so.5
/usr/lib64/libMagick++-7.Q16HDRI.so.5.0.0
/usr/lib64/libMagickCore-7.Q16HDRI.so.10
/usr/lib64/libMagickCore-7.Q16HDRI.so.10.0.2
/usr/lib64/libMagickWand-7.Q16HDRI.so.10
/usr/lib64/libMagickWand-7.Q16HDRI.so.10.0.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ImageMagick/023310790971bdf976590c24416fcb00ec9785ec
/usr/share/package-licenses/ImageMagick/9fbc78241e625956288a5ef6797d540b58197565
/usr/share/package-licenses/ImageMagick/e35708150f9609098e95bf25b6b5d4908f999666

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ImageMagick.1
/usr/share/man/man1/Magick++-config.1
/usr/share/man/man1/MagickCore-config.1
/usr/share/man/man1/MagickWand-config.1
/usr/share/man/man1/animate.1
/usr/share/man/man1/compare.1
/usr/share/man/man1/composite.1
/usr/share/man/man1/conjure.1
/usr/share/man/man1/convert.1
/usr/share/man/man1/display.1
/usr/share/man/man1/identify.1
/usr/share/man/man1/import.1
/usr/share/man/man1/magick-script.1
/usr/share/man/man1/magick.1
/usr/share/man/man1/mogrify.1
/usr/share/man/man1/montage.1
/usr/share/man/man1/stream.1
