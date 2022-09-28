combined:
	rm -f combined.csv
	ls ../test-lists/lists/??.csv | xargs -I % sh -c './extract-url.sh % >> combined.csv'
	wc -l combined.csv
https_freq:
	rm -f https.csv
	echo "cc,http,https" > https.csv
	ls ../test-lists/lists/??.csv | xargs -I % sh -c './https_frequency.sh % >> https.csv'
