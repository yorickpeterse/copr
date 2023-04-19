SPEC := stylua.spec

srpm:
	rm -rf build
	spectool --define '_topdir build' -gR ${SPEC}
	rpmbuild --define '_topdir build' -bs ${SPEC}

clean:
	rm -rf build

.PHONY: srpm
