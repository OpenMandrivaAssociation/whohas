Name:		whohas
Version:	0.29
Release:	1
Summary:	Command line tool searching package in different distributions
Group:		Development/Other
License:	GPLv2+
URL:		http://www.philippwesche.org/200811/whohas/intro.html
Source0:	http://www.philippwesche.org/200811/whohas/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl-libwww-perl

%description
whohas is a command line tool that allows querying several package lists
at once - currently supported are Arch, Debian, Fedora, Gentoo, Mandriva,
openSUSE, Slackware (and linuxpackages.net), Source Mage, Ubuntu, FreeBSD,
NetBSD, OpenBSD, Fink, MacPorts and Cygwin. whohas is written in Perl and was
designed to help package maintainers find ebuilds, pkgbuilds and similar
package definitions from other distributions to learn from. However, it can
also be used by normal users who want to know:

- Which distribution provides packages on which the user depends.
- What version of a given package is in use in each distribution, or in each
release of a distribution (implemented only for Debian).

%prep
%setup -q

%build

%install
install -m 755 -D program/whohas %{buildroot}%{_bindir}/whohas
mv usr/share/man/de/man1/whohas.1 usr/share/man/de/man1/whohas.1.old
iconv -f ISO_8859-1 -t UTF-8 usr/share/man/de/man1/whohas.1.old > usr/share/man/de/man1/whohas.1
xz -zk usr/share/man/man1/whohas.1 usr/share/man/de/man1/whohas.1
install -m 644 -D usr/share/man/man1/whohas.1.xz %{buildroot}%{_mandir}/man1/whohas.1.xz
install -m 644 -D usr/share/man/de/man1/whohas.1.xz %{buildroot}%{_mandir}/de/man1/whohas.1.xz

%files
%{_bindir}/whohas
%defattr(644,root,root,755)
%doc intro.txt LICENSE TODO.txt Changelog
%{_mandir}/man1/whohas.1.xz
%lang(de)%{_mandir}/de/man1/whohas.1.xz
