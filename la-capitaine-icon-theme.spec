%global themename La-Capitaine

Name: la-capitaine-icon-theme
Version: 0.6.2
Release: 1
Summary: Icon pack designed to integrate with most desktop environments
BuildArch: noarch

# For a breakdown of the licensing, see COPYING and LICENSE
License: GPLv3+ and MIT
URL: https://krourke.org/projects/art/la-capitaine-icon-theme
Source0: https://github.com/keeferrourke/la-capitaine-icon-theme/archive/v%{version}/%{name}-%{version}.tar.gz

Requires: adwaita-icon-theme
Requires: gnome-icon-theme
Requires: hicolor-icon-theme

%description
La Capitaine is an icon pack — designed to integrate with most desktop
environments. The set of icons takes inspiration from the latest iterations of
macOS and Google's Material Design through the use of visually pleasing
gradients, shadowing, and simple icon geometry.

%prep
%autosetup -p1

%build
%configure

%install
mkdir -p %{buildroot}%{_datadir}/icons/%{themename}
cp -rp actions %{buildroot}%{_datadir}/icons/%{themename}
cp -rp animations %{buildroot}%{_datadir}/icons/%{themename}
cp -rp apps %{buildroot}%{_datadir}/icons/%{themename}
cp -rp devices %{buildroot}%{_datadir}/icons/%{themename}
cp -rp emblems %{buildroot}%{_datadir}/icons/%{themename}
cp -rp emotes %{buildroot}%{_datadir}/icons/%{themename}
cp -rp mimetypes %{buildroot}%{_datadir}/icons/%{themename}
cp -rp panel %{buildroot}%{_datadir}/icons/%{themename}
cp -rp places %{buildroot}%{_datadir}/icons/%{themename}
cp -rp status %{buildroot}%{_datadir}/icons/%{themename}
install -Dpm0644 index.theme %{buildroot}%{_datadir}/icons/%{themename}/index.theme

touch %{buildroot}%{_datadir}/icons/%{themename}/icon-theme.cache

# Remove executable bit
chmod -x %{buildroot}%{_datadir}/icons/%{themename}/apps/scalable/org.gabmus.hydrapaper.svg

%transfiletriggerin -- %{_datadir}/icons/%{themename}
gtk-update-icon-cache --force %{_datadir}/icons/%{themename} &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/%{themename}
gtk-update-icon-cache --force %{_datadir}/icons/%{themename} &>/dev/null || :

%files
%license COPYING LICENSE
%doc README.md Credits.md Thanks.md
%{_datadir}/icons/%{themename}/actions/
%{_datadir}/icons/%{themename}/animations/
%{_datadir}/icons/%{themename}/apps/
%{_datadir}/icons/%{themename}/devices/
%{_datadir}/icons/%{themename}/emblems/
%{_datadir}/icons/%{themename}/emotes/
%{_datadir}/icons/%{themename}/index.theme
%{_datadir}/icons/%{themename}/mimetypes/
%{_datadir}/icons/%{themename}/panel/
%{_datadir}/icons/%{themename}/places/
%{_datadir}/icons/%{themename}/status/
%dir %{_datadir}/icons/%{themename}
%ghost %{_datadir}/icons/%{themename}/icon-theme.cache
