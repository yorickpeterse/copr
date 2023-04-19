SPEC := neovim-gtk.spec
GIT_SPEC := $(realpath neovim-gtk-git.spec)

srpm:
	rm -rf build
	spectool --define '_topdir build' -gR ${SPEC}
	rpmbuild --define '_topdir build' -bs ${SPEC}

git:
	rm -rf build/neovim-gtk
	git clone --depth=1 https://github.com/Lyude/neovim-gtk.git build/neovim-gtk
	mkdir -p build/SRPMS
	cp ${GIT_SPEC} build/neovim-gtk
	cd build/neovim-gtk && rpkg srpm --outdir . && mv *.src.rpm ../SRPMS/

clean:
	rm -rf build

.PHONY: srpm clean git
