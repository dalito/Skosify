.PHONY: test docs build

test:
	pytest

doc:
	rm -rf docs/_build
	$(MAKE) -C docs html

build:
	hatch build
