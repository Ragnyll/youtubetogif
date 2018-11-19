# youtube_to_gif
Tested on python 3.6.5

install requirements with `pip -r requirements.txt`.

Takes a link from youtube and puts a clip starting at start and ending at end

```
Args:
    youtube_address (str): the full address to the youtube video.
    output_path (str): the absolute path to the location output file.
        Format: /location/absolute/path/[filename]
    start (float): time to start the gif at
        Format: m.ssss
    end (float): time to end the gif at
        Format: m.ssss
```

Usage:
```
youtube_to_gif.py YOUTUBE_ADDRESS OUTPUT_PATH START END
or
youtube_to_gif.py --youtube-address YOUTUBE_ADDRESS --output-path OUTPUT_PATH --start START --end END
```
