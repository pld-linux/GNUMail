Summary:	Mail application for GNUstep
Summary(pl):	Aplikacja pocztowa dla ¶rodowiska GNUstep
Name:		GNUMail
Version:	1.1.2
%define cvs 20040729
Release:	3.%{cvs}.3
License:	GPL
Group:		X11/Applications
Source0:	%{name}-cvs-%{cvs}.tar.gz
# Source0-md5:	a20eded4368ce4363e67aac4540ac8d8
Patch0:	%{name}-pass-arguments.patch
URL:		http://www.collaboration-world.com/gnumail/
BuildRequires:	Pantomime-devel >= 1.1.2-4
BuildRequires:	gnustep-gui-devel >= 0.9.1
BuildRequires:	Addresses-devel >= 0.4.6
Requires:	Pantomime >= 1.1.2-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
GNUMail.app is a fully featured mail application. It offers the
following features:
- Hierarchical mailboxes support (Local or IMAP)
- Multiple POP3 and IMAP accounts support
- Multiple delivery agents (SMTP or local mailer)
- Full MIME support
- Filters support
- Address Book with groups support
- and more...

%description -l pl
GNUMail.app to w pe³ni funkcjonalna aplikacja pocztowa. Oferuje
nastêpuj±ce mo¿liwo¶ci:
- obs³ugê hierarchicznych skrzynek (lokalnych lub IMAP)
- obs³ugê wielu kont POP3 i IMAP
- wiele sposobów dorêczania (SMTP lub program lokalny)
- pe³n± obs³ugê MIME
- obs³ugê filtrów
- ksi±¿kê adresow± z obs³ug± grup
- i inne...

%prep
%setup -q -n %{name}
%patch0 -p1

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog docs/{PREFERENCES,README,TODO,WHOIS}

%dir %{_prefix}/System/Applications/GNUMail.app
%attr(755,root,root) %{_prefix}/System/Applications/GNUMail.app/GNUMail
%dir %{_prefix}/System/Applications/GNUMail.app/Resources
%{_prefix}/System/Applications/GNUMail.app/Resources/*.desktop
%{_prefix}/System/Applications/GNUMail.app/Resources/*.plist
%{_prefix}/System/Applications/GNUMail.app/Resources/*.tiff
%{_prefix}/System/Applications/GNUMail.app/Resources/Welcome
%{_prefix}/System/Applications/GNUMail.app/Resources/English.lproj
%lang(cs) %{_prefix}/System/Applications/GNUMail.app/Resources/Czech.lproj
%lang(fr) %{_prefix}/System/Applications/GNUMail.app/Resources/French.lproj
%lang(de) %{_prefix}/System/Applications/GNUMail.app/Resources/German.lproj
%lang(es) %{_prefix}/System/Applications/GNUMail.app/Resources/Spanish.lproj
%lang(sv) %{_prefix}/System/Applications/GNUMail.app/Resources/Swedish.lproj

%dir %{_prefix}/System/Applications/GNUMail.app/%{gscpu}
%dir %{_prefix}/System/Applications/GNUMail.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/GNUMail.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/GNUMail.app/%{gscpu}/%{gsos}/%{libcombo}/GNUMail
%{_prefix}/System/Applications/GNUMail.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp

%dir %{_prefix}/System/Library/GNUMail
%dir %{_prefix}/System/Library/GNUMail/*.prefs
%{_prefix}/System/Library/GNUMail/*.prefs/Resources
%attr(755,root,root) %{_prefix}/System/Library/GNUMail/*.prefs/%{gscpu}
%dir %{_prefix}/System/Library/GNUMail/Import.bundle
%{_prefix}/System/Library/GNUMail/Import.bundle/Resources
%attr(755,root,root) %{_prefix}/System/Library/GNUMail/Import.bundle/%{gscpu}

%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so.*
