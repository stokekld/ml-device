C=dpkg-deb --build
PROJECT=mistlogic
VERSION=0.1
REVISION=1
PACKAGE=$(PROJECT)_$(VERSION)-$(REVISION)

DEBIAN_DIR=$(PACKAGE)/DEBIAN/
PYTHON_DIST=$(PACKAGE)/usr/lib/python2.7/dist-packages/

all: $(PACKAGE)

$(PACKAGE): 
	mkdir -p $(DEBIAN_DIR)
	mkdir -p $(PYTHON_DIST)
	cp control $(DEBIAN_DIR)
	cp ../db/MistDB.py $(PYTHON_DIST)

	$(C) $(PACKAGE)

clean:
	rm -rf $(PACKAGE)*
