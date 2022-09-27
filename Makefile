combined:
	rm -f combined.csv
	ls ../test-lists/lists/??.csv | xargs -I % sh -c './extract-url.sh % >> combined.csv'
	wc -l combined.csv
