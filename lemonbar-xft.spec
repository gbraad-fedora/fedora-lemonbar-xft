Name: lemonbar-xft
Version: 1.0
Release: 1.20150624g088ddb6%{?dist}

BuildRequires: libxcb-devel
BuildRequires: libXft-devel

Summary: A featherweight, lemon-scented, bar based on xcb

# The source for this package was pulled from upstream's vcs.  Use the
# following command to generate the tarball:
# curl -vfL http://github.com/krypt-n/bar/tarball/088ddb6 > rpmbuild/SOURCES/krypt-n-bar-g088ddb6.tar.gz

License: MIT
URL: https://github.com/krypt-n/bar
Source0: krypt-n-bar-g088ddb6.tar.gz

%description
lemonbar is a lightweight bar entirely based on XCB. Provides full UTF-8
support, basic formatting, RandR and Xinerama support and EWMH compliance
without wasting your precious memory.

%prep
%setup -n krypt-n-bar-088ddb6

%build
make

%install
rm -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/lemonbar
%doc /usr/share/man/man1/lemonbar.1.gz
%doc LICENSE

%changelog
* Thu Jun 25 2015 Eduardo Ito <itoed@yahoo.com> - 1.0-1.20150624g088ddb6
- Initial package release
