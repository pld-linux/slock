Summary:	slock - a simple X display locker
Name:		slock
Version:	1.0
Release:	0.1
License:	MIT
Group:		Applications
Source0:	http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
# Source0-md5:	98503f0dae5acc15c90b81ffd423f987
URL:		http://tools.suckless.org/slock
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the simplest X screen locker we are aware of. It is stable and
quite a lot of people in our community are using it every day when
they are out with friends or fetching some food from the local pub.

%prep
%setup -q

%build
cat << 'EOF' >> config.mk
PREFIX=%{_prefix}
CFLAGS:=%{rpmcflags} $(filter-out -Os,$(CFLAGS))
LDFLAGS:=%{rpmldflags} $(LDFLAGS)
EOF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(4755,root,root) %{_bindir}/slock
#%{_mandir}/man1/slock.1*
