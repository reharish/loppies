version = 0.0.1_Beta
description = Handy Scripts on BASH env

INSTALL_DIR = /usr/share/loppies

all: build

build:

	mkdir -p build
	mkdir -p build/$(INSTALL_DIR)/bin
	cp -a bin/* build/$(INSTALL_DIR)/bin
	cp -a loppies build/$(INSTALL_DIR)

deb: build

	fpm -s dir -t deb -n loppies				\
		-v $(version)                         	\
		--maintainer rengarajharish@gmail.com   	\
		-C "build/" -a noarch                  	\
		-d python3                         			\
		--url "https://reharish.github.io/cv"           		\
		--description "$(description)"        		\
		--after-install deb_script/postinst.sh 	\
		--after-remove deb_script/postrm.sh	\
		.

clean:
	rm -rf build/
	rm -rf *.deb

distclean:
	rm -rf *~
	rm -rf #*
