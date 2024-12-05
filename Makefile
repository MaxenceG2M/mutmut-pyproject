PYTHON=./.venv/bin/python
MUTMUT=./.venv/bin/mutmut

test:
	$(PYTHON) -m unittest discover -b -t tests/ -p '*_test.py' tests/

mutmut:
	$(MUTMUT) run > mutmut.log
