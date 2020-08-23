test:
	@# We need this because for some reason I haven't yet figured out,
	@# running pytest alone doesn't get picked up by pyenv.
	python -m pytest

clean:
	find . -name "__pycache__" | xargs rm -r
	rm -rf .pytest_cache

.PHONY: test clean
