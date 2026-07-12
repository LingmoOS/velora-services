Name:           lingmo-services
Version:        1.0.0
Release:        1%{?dist}
Summary:        DDE Services for Lingmo OS
License:        LGPL-3.0-or-later
URL:            https://github.com/LingmoOS/lingmo-services
Source0:        dde-services-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.16
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(dtk6core)

%description
DDE Services provides background services and DBus interfaces
for the Lingmo desktop environment.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DVERSION=%{version}
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE*
%{_bindir}/lingmo-services*
%{_libdir}/lingmo-services/
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/*.service

%changelog
* Tue Jun 18 2025 LingmoOS Build System <dev@lingmo.os> - %{version}-1
- Initial RPM packaging for local source build
