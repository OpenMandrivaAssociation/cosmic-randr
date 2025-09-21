%undefine _debugsource_packages

Name:           cosmic-randr
Version:        1.0.0
%define beta beta.1
Release:        %{?beta:0.%{beta}.}1
Summary:        Library and utility for displaying and configuring Wayland outputs
License:        MPL-2.0
Group:          Toold/COSMIC
URL:            https://github.com/pop-os/cosmic-randr
Source0:        https://github.com/pop-os/cosmic-randr/archive/epoch-%{version}%{?beta:-%{beta}}/%{name}-epoch-%{version}%{?beta:-%{beta}}.tar.gz
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
%autosetup -n %{name}-epoch-%{version}%{?beta:-%{beta}} -a1 -p1
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
