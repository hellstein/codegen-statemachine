test:
	python3 app.py --states conf/machine.json --init conf/init.json

clean:
	rm -rf dist
