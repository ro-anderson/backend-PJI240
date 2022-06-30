.PHONY: build install_dist install_dev clean unit_test dkbuild dkrun change-version
.DEFAULT_GOAL := help

#################################################################################
# GLOBALS                                                                       #
#################################################################################
VERSION := $(shell grep __package_version setup.py | head -1 | cut -d \" -f2)

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Build python infra python .whl lib
build:
	@python3 setup.py bdist_wheel

## Install python infra python .whl lib
install_dist: build
	@pip3 install dist/infra*.whl --force-reinstall

## Install python infra python .whl lib and automatically update with pip install -e paramter
install_dev:
	@pip3 install --force-reinstall -e .

## Delete all unused artifacts and compiled python files
clean:
	@find ./ -type d -name 'dist' -exec rm -rf {} +;
	@find ./ -type d -name 'build' -exec rm -rf {} +;
	@find ./ -type d -name '*.egg-info' -exec rm -rf {} +;
	@find ./ -type d -name '.pytest_cache' -exec rm -rf {} +;
	@find ./ -type d -name 'spark-warehouse' -exec rm -rf {} +;
	@find ./ -type d -name 'metastore_db' -exec rm -rf {} +;
	@find ./ -type d -name '__pycache__' -exec rm -rf {} +;
	@find ./ -type f -name '*derby.log' -exec rm -f {} \;
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete

## Apply unit tests
unit_tests:
	@python3 -m pytest -s tests/unit

## Change the version to string received in the NEW_VERSION variable and show
change_version:
	@sed -i 's/$(VERSION)/$(NEW_VERSION)/g' setup.py
	@echo "VERSION: $(NEW_VERSION)"


#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
