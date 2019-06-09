.PHONY: play

play:
	python alien_invasion.py

unittest:
	coverage run --branch testAI.py 
	coverage report -m

pylint:
