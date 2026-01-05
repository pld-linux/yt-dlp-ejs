Summary:	External JavaScript for yt-dlp supporting many runtimes
Name:		yt-dlp-ejs
Version:	0.3.1
Release:	1
License:	Unlicense
Group:		Applications
Source0:	https://github.com/yt-dlp/ejs/releases/download/%{version}/yt_dlp_ejs-%{version}.tar.gz
# Source0-md5:	7001eea74deef76530524aa29741186e
Source1:	https://github.com/yt-dlp/ejs/releases/download/%{version}/yt.solver.core.min.js
# Source1-md5:	01dd51093cd5140ab4a829e9f2a77c17
Source2:	https://github.com/yt-dlp/ejs/releases/download/%{version}/yt.solver.lib.min.js
# Source2-md5:	7fbcfdf209230f48e7a5ce656ba9bfda
Patch0:		manual-bundle.patch
URL:		https://github.com/yt-dlp/ejs
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
%setup -q -n yt_dlp_ejs-%{version}
%patch -P0 -p1

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{py3_sitescriptdir}/yt_dlp_ejs/yt/solver/core.min.js
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{py3_sitescriptdir}/yt_dlp_ejs/yt/solver/lib.min.js

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
