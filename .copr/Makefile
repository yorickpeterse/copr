TOP := ${PWD}/build

srpm:
	spectool --define "_topdir ${TOP}" -gR ${spec}
	cp -r sources/* ${TOP}/SOURCES || true
	rpmbuild --define "_topdir ${TOP}" -bs ${spec}
	mv ${TOP}/SRPMS/*.src.rpm ${outdir}

.PHONY: srpm
