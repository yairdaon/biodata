hog:
	clear
	python2.7 hogsvd.py

get:
	clear
	python2.7 get_results.py

push:
	git push https://github.com/yairdaon/biodata.git

clean:
	rm -rvf *.png *~ *.pyc
