SPEC := colemak-dh-ortho.spec

srpm:
	rm -rf build
	spectool --define '_topdir build' -gR ${SPEC}
	mkdir -p build/SOURCES
	cp -p sources/* build/SOURCES/
	rpmbuild --define '_topdir build' -bs ${SPEC}

clean:
	rm -rf build

.PHONY: srpm
