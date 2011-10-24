%global eclipse_base        %{_libdir}/eclipse
%global install_loc         %{_datadir}/eclipse/dropins
# Taken from update site so we match upstream
#  http://download.eclipse.org/mylyn/archive/3.5.1/v20110422-0200/
%global qualifier           v20110422-0200

Name: eclipse-mylyn-ide
Summary: Mylyn Context Connector: Eclipse IDE
Version: 3.5.1
Release: 1
License: EPL
URL: http://www.eclipse.org/mylyn

# bash fetch-eclipse-mylyn-ide.sh
Source0: eclipse-mylyn-ide-R_3_5_1-fetched-src.tar.bz2
Source1: fetch-eclipse-mylyn-ide.sh

BuildArch: noarch

BuildRequires: java-devel >= 1.5.0
BuildRequires: eclipse-platform >= 0:3.4.0
BuildRequires: eclipse-pde >= 0:3.4.0
BuildRequires: eclipse-mylyn >= 3.5.0
BuildRequires: eclipse-mylyn-context >= 3.5.0
BuildRequires: eclipse-mylyn-context-team >= 3.5.0

Requires: eclipse-platform >= 0:3.4.0
Requires: eclipse-mylyn >= 3.5.0
Requires: eclipse-mylyn-context >= 3.5.0
Requires: eclipse-mylyn-context-team >= 3.5.0
Obsoletes: eclipse-mylyn-ide < %{version}-%{release}

Group: Development/Java

%description
Mylyn Task-Focused UI extensions for the Eclipse IDE. 
Provides focusing of common IDE views and editors.

%prep
%setup -q -c

%build
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.ide_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -d "mylyn mylyn-context mylyn-context-team"

%install
install -d -m 755 %{buildroot}%{_datadir}/eclipse
install -d -m 755 %{buildroot}%{install_loc}/mylyn-ide

unzip -q -o -d %{buildroot}%{install_loc}/mylyn-ide \
 build/rpmBuild/org.eclipse.mylyn.ide_feature.zip

%files
%defattr(-,root,root,-)
%{install_loc}/mylyn-ide
%doc org.eclipse.mylyn.contexts/org.eclipse.mylyn.ide-feature/epl-v10.html
%doc org.eclipse.mylyn.contexts/org.eclipse.mylyn.ide-feature/license.html

