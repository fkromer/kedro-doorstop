# format code
fc:
	black kedro_doorstop/

# format imports
fi:
	isort -sp .isort.cfg -rc kedro_doorstop/

# check bandit
cb:
	bandit -r kedro_doorstop

# check pylint
cp:
	pylint kedro_doorstop

#check mypy
cm:
	mypy -p kedro_doorstop

# export requirements
er:
	poetry export --without-hashes -f requirements.txt > requirements.txt

# export test-requirements
etr:
	poetry export --without-hashes --dev -f requirements.txt > test_requirements.txt

# build wheel
bw:
	python setup.py check -ms
	python setup.py bdist_wheel --universal
