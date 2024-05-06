bikebus_times.zip: bikebus_times
	zip -r bikebus_times.zip bikebus_times

bikebus_times: bikebus_times.py Lexend-Medium.ttf
	mkdir -p bikebus_times && python bikebus_times.py

clean:
	rm -r bikebus_times Lexend-Medium.ttf

Lexend-Medium.ttf:
	wget https://github.com/googlefonts/lexend/raw/main/fonts/lexend/ttf/Lexend-Medium.ttf
