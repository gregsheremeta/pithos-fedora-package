Name:           pithos
Version:        1.1.1
Release:        1%{?dist}
Summary:        A Pandora client for the GNOME Desktop

Group:          Applications/File
License:        GPLv3
URL:            http://pithos.github.io/
Source0:        https://github.com/pithos/pithos/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel python3-setuptools desktop-file-utils

Requires:       python3-setuptools
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-ugly
Requires:       gstreamer1-plugins-bad-freeworld
Requires:       gtk3
Requires:       python3-gobject
Requires:       hicolor-icon-theme

%description
Pithos is a Pandora client for the GNOME Desktop.

%prep
%setup -q

%install
%{__python3} setup.py install --root=%{buildroot}

# Remove Unity specific icons
rm -rf %{buildroot}%{_datadir}/icons/ubuntu*

%post
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database &> /dev/null || :

%postun
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database &> /dev/null || :

%files
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.egg-info/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/

%changelog
* Mon May 18 2015 Greg Sheremeta <greg@gregsheremeta.com> - 1.1.1-1
- Remove pylast stuff.

* Mon May 18 2015 Greg Sheremeta <greg@gregsheremeta.com> - 1.1.1-1
- Bump version to 1.1.1.

* Sun May 10 2015 Greg Sheremeta <greg@gregsheremeta.com> - 1.1.0-1
- Bump version to 1.1.0.
  Shortened description.

* Mon Jan 5 2015 TingPing <tingping@tingping.se> - 1.0.1-2
- Fix importing pylast

* Sun Sep 21 2014 TingPing <tingping@tingping.se> - 1.0.1-1
- Bump version to 1.0.1

* Fri Jul 18 2014 TingPing <tingping@tingping.se> - 1.0.0-3
- Fix python2 sitelib macro

* Sat Jun 21 2014 TingPing <tingping@tingping.se> - 1.0.0-2
- Fix python2 sitelib macro

* Sat Jun 7 2014 TingPing <tingping@tingping.se> - 1.0.0-1
- Bump version to 1.0.0

* Fri Apr 18 2014 TingPing <tingping@tingping.se> - 0.3.18-2
- Fix dependency issue

* Thu Mar 27 2014 TingPing <tingping@tingping.se> - 0.3.18-1
- Initial package

