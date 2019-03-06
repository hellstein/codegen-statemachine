test:
	python3 generator.py --states conf/states.json --init conf/init.json

clean:
	rm -rf dist
