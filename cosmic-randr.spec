%undefine _debugsource_packages

Name:           cosmic-randr
Version:        1.0.0
Release:        0.alpha4.0
Summary:        Library and utility for displaying and configuring Wayland outputs
License:        MPL-2.0
Group:          Toold/COSMIC
URL:            https://github.com/pop-os/cosmic-randr
Source0:        https://github.com/pop-os/cosmic-randr/archive/epoch-%{version}-alpha.4/%{name}-epoch-%{version}-alpha.4.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(wayland-client)

%description
COSMIC RandR is both a library and command line utility for displaying and
configuring Wayland outputs. Each display is represented as an "output head",
whereas all supported configurations for each display is represented as "output modes".

%prep
%autosetup -n %{name}-epoch-%{version}-alpha.4 -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
