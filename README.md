# My Graduation Thesis using ThuThesis template
To simplify the process, I pushed the compiled class file to github

# What's ThuThesis?
ThuThesis is an abbreviation of <b>T</b>sing<b>h</b>ua <b>U</b>niversity <b>Thesis</b> LaTeX Template.

This package establishes a simple and easy-to-use LaTeX template for Tsinghua dissertations, including general undergraduate research papers, masters theses, doctoral theses, doctoral dissertations, and post-doc reports. Additional support for other formats (what else is there?) will be added continuously. An English translation of this README follows the Chinese below.

* Check the  [FAQ](https://github.com/xueruini/thuthesis/wiki/FAQ)
* [Github Issues](http://github.com/xueruini/thuthesis/issues)
* [TeX@newsmth](http://www.newsmth.net/nForum/#!board/TeX)
* [ThuThesis@Google Groups](http://groups.google.com/group/thuthesis)

# Compile

```shell
xetex thuthesis.ins
latex -xelatex main
```

## Targets
* `make all`       same as `make thesis && make shuji && make doc`;
* `make cls`       generate template file;
* `make thesis`    generate thesis main.pdf;
* `make shuji`     generate book spine for printing shuji.pdf;
* `make doc`       generate documentation thuthesis.pdf;
* `make clean`     delete all examples' files (excluding main.pdf);
* `make cleanall`  delete all examples' files and main.pdf;
* `make distclean` delete all examples' and templates' files and PDFs.
