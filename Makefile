test:
	cd scripts && flake83.sh
	cd cookiecutter/hooks && flake83.sh
	cd documents && noutf8.sh
