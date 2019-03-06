test:
	python3 app.py --states conf/states.json --init conf/init.json

clean:
	rm -rf dist
