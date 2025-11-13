Summary:	External JavaScript for yt-dlp supporting many runtimes
Name:		yt-dlp-ejs
Version:	0.3.1
Release:	1
License:	Unlicense
Group:		Applications
Source0:	https://github.com/yt-dlp/ejs/releases/download/%{version}/yt_dlp_ejs-%{version}.tar.gz
# Source0-md5:	7001eea74deef76530524aa29741186e
# tar -xf yt_dlp_ejs-%{version}.tar.gz
# npm -C yt_dlp_ejs-%{version} install --ignore-scripts --cpu noarch --no-audit --no-fund --no-update-check
# find yt_dlp_ejs-%{version}/node_modules -type d -name prebuilds -prune -exec rm -r {} +
# tar -C yt_dlp_ejs-%{version} -acf yt-dlp-ejs-node_modules-%{version}.tar.xz node_modules
Source1:	%{name}-node_modules-%{version}.tar.xz
# Source1-md5:	08b224446bd6dbe690d2a9ccec33a792
Patch0:		manual-bundle.patch
URL:		https://github.com/yt-dlp/ejs
BuildRequires:	nodejs
BuildRequires:	python3 >= 1:3.10
BuildRequires:	python3-build
BuildRequires:	python3-hatch-vcs
BuildRequires:	python3-hatchling >= 1.27.0
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
ExclusiveArch:	%{ix86} %{x86_64} %{armv7} %{armv8} aarch64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
External JavaScript for yt-dlp supporting many runtimes.

%package -n python3-yt-dlp-ejs
Summary:	External JavaScript for yt-dlp supporting many runtimes
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.10
Suggests:	nodejs

%description -n python3-yt-dlp-ejs
External JavaScript for yt-dlp supporting many runtimes.

%prep
%setup -q -n yt_dlp_ejs-%{version} -a1
%patch -P0 -p1

%build
%py3_build_pyproject

node ./node_modules/.bin/rollup -c

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

cp -p dist/yt.solver.core.min.js $RPM_BUILD_ROOT%{py3_sitescriptdir}/yt_dlp_ejs/yt/solver/core.min.js
cp -p dist/yt.solver.lib.min.js $RPM_BUILD_ROOT%{py3_sitescriptdir}/yt_dlp_ejs/yt/solver/lib.min.js

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python3-yt-dlp-ejs
%defattr(644,root,root,755)
%doc LICENSE README.md
%dir %{py3_sitescriptdir}/yt_dlp_ejs
%{py3_sitescriptdir}/yt_dlp_ejs/*.py
%{py3_sitescriptdir}/yt_dlp_ejs/__pycache__
%dir %{py3_sitescriptdir}/yt_dlp_ejs/yt
%{py3_sitescriptdir}/yt_dlp_ejs/yt/*.py
%{py3_sitescriptdir}/yt_dlp_ejs/yt/__pycache__
%dir %{py3_sitescriptdir}/yt_dlp_ejs/yt/solver
%{py3_sitescriptdir}/yt_dlp_ejs/yt/solver/*.py
%{py3_sitescriptdir}/yt_dlp_ejs/yt/solver/__pycache__
%{py3_sitescriptdir}/yt_dlp_ejs/yt/solver/core.min.js
%{py3_sitescriptdir}/yt_dlp_ejs/yt/solver/lib.min.js
%{py3_sitescriptdir}/yt_dlp_ejs-%{version}.dist-info
