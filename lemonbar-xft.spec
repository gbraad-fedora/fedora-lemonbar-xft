%global project https://github.com/PH111P/bar
%global version 1.3

%global debug_package %{nil}
%global _enable_debug_package 0
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name:          lemonbar-xft
Version:       %{version}
Release:       1.20210227a8d8e9d%{?dist}

BuildRequires: libxcb-devel
BuildRequires: libXft-devel
BuildRequires: make
BuildRequires: gcc
BUildRequires: perl-podlators

Summary:       A featherweight, lemon-scented, bar based on xcb

# The source for this package was pulled from upstream's vcs.  Use the
# following command to generate the tarball:
# curl -vfL http://github.com/ph111p/bar/tarball/a8d8e9d > rpmbuild/SOURCES/ph111p-bar-a8d8e9d.tar.gz

License:       MIT
URL:           %{project}
Source0:       PH111P-bar-a8d8e9d.tar.gz

%description
lemonbar is a lightweight bar entirely based on XCB. Provides full UTF-8
support, basic formatting, RandR and Xinerama support and EWMH compliance
without wasting your precious memory.

%prep
%setup -n PH111P-bar-a8d8e9d

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
* Sat Feb 27 2021 Gerard Braad <me@gbraad.nl> - 1.3-1.20210227a8d8e9d
- Updated package release

* Thu Jun 25 2015 Eduardo Ito <itoed@yahoo.com> - 1.0-1.20150624g088ddb6
- Initial package release
