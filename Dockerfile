FROM registry.fedoraproject.org/fedora:latest

RUN dnf -y install rpm-build make gcc libxcb-devel libXft-devel ; dnf clean all
