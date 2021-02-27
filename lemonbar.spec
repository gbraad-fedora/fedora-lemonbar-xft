%global project https://github.com/LemonBoy/bar
%global version 1.4

%global debug_package %{nil}
%global _enable_debug_package 0
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name:          lemonbar
Version:       %{version}
Release:       1.202102272e8ac2c%{?dist}

BuildRequires: libxcb-devel

Summary:       A featherweight, lemon-scented, bar based on xcb

# The source for this package was pulled from upstream's vcs.  Use the
# following command to generate the tarball:
# curl -vfL http://github.com/LemonBoy/bar/tarball/2e8ac2c > rpmbuild/SOURCES/LemonBoy-bar-2e8ac2c.tar.gz

License:       MIT
URL:           %{project}
Source0:       LemonBoy-bar-2e8ac2c.tar.gz

%description
lemonbar is a lightweight bar entirely based on XCB. Provides full UTF-8
support, basic formatting, RandR and Xinerama support and EWMH compliance
without wasting your precious memory.

%prep
%setup -n LemonBoy-bar-2e8ac2c

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
* Sat Feb 27 2021 Gerard Braad <me@gbraad.nl> - 1.4-1.202102272e8ac2c
- Updated package release

* Thu Jun 25 2015 Eduardo Ito <itoed@yahoo.com> - 1.0-1.20150624g088ddb6
- Initial package release
