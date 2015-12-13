# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.define "flask" do |flask|
        flask.vm.box = "debian-8.2"
        flask.vm.box_url = "https://github.com/one-love/vagrant-base-box/releases/download/v0.1/debian-8.2-x86_64.box"
        flask.vm.network :private_network, ip: "192.168.87.10"
        flask.vm.hostname = "flask.vagrant"
        flask.vm.provision "shell", path: "install-docker.sh"
    end
end
