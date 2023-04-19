SPEC := lua-language-server.spec
TOP := ${PWD}/build

prepare:
	rm -rf build
	spectool --define "_topdir ${TOP}" -gR ${SPEC}
	cp -p sources/* build/SOURCES/

srpm: prepare
	rpmbuild --define "_topdir ${TOP}" -bs ${SPEC}

rpm: prepare
	rpmbuild --define "_topdir ${TOP}" -bb ${SPEC}

clean:
	rm -rf build

.PHONY: srpm prepare
