C=dpkg-deb --build
PROJECT=mistlogic
VERSION=0.1
REVISION=1
PACKAGE=$(PROJECT)_$(VERSION)-$(REVISION)

DEBIAN_DIR=$(PACKAGE)/DEBIAN/
PROJECT_DIR=$(PACKAGE)/etc/$(PROJECT)
PYTHON_DIST=$(PACKAGE)/usr/lib/python2.7/dist-packages/

all: $(PACKAGE)

$(PACKAGE): 
	mkdir -p $(DEBIAN_DIR)
	mkdir -p $(PYTHON_DIST)
	mkdir -p $(PROJECT_DIR)
	cp control $(DEBIAN_DIR)
	cp -r ../mistlogic/ $(PYTHON_DIST)
	cp -r ../modules/* $(PROJECT_DIR)

	$(C) $(PACKAGE)

clean:
	rm -rf $(PACKAGE)*
