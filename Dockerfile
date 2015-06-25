FROM fedora:22

RUN dnf -y install rpm-build make gcc libxcb-devel libXft-devel ; dnf clean all
