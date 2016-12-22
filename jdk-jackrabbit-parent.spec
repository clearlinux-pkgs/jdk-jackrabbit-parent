Name     : jdk-jackrabbit-parent
Version  : 2.2.5
Release  : 1
URL      : http://repo.maven.apache.org/maven2/org/apache/jackrabbit/jackrabbit-parent/2.2.5/jackrabbit-parent-2.2.5.pom
Source0  : http://repo.maven.apache.org/maven2/org/apache/jackrabbit/jackrabbit-parent/2.2.5/jackrabbit-parent-2.2.5.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/maven-poms/jackrabbit-parent.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/jackrabbit-parent.xml \
%{buildroot}/usr/share/maven-poms/jackrabbit-parent.pom \
%{buildroot}/usr/share/java/jackrabbit-parent.jar \

%files
%defattr(-,root,root,-)
/usr/share/maven-metadata/jackrabbit-parent.xml
/usr/share/maven-poms/jackrabbit-parent.pom
