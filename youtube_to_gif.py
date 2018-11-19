#!/usr/bin/python3
"""This script takes a video from youtube and puts a clip from it into a gif
"""

from datetime import datetime
import fire
from moviepy.editor import *
from os import listdir
from os import path
from pytube import YouTube
from shutil import rmtree
from tempfile import mkdtemp


def create_gif_from_youtube_video(youtube_address, output_path, start, end):
    """Takes a link from youtube and puts a clip starting at start and ending at end

    Args:
        youtube_address (str): the full address to the youtube video.
        output_path (str): the absolute path to the location output file.
            Format: /location/absolute/path/[filename]
        start (float): time to start the gif at
            Format: m.ssss
        end (float): time to end the gif at
            Format: m.ssss

    Returns:
        None
    """
    try:
        temp_dir = mkdtemp()
        YouTube(youtube_address).streams.first().download(temp_dir)
        start_min, start_sec = int(start), float('%.2f' % ((start - int(start)) * 100))
        end_min, end_sec = int(end), float('%.2f' % ((end - int(end)) * 100))
        clip = (VideoFileClip('{}/{}'.format(temp_dir, listdir(temp_dir)[0]))
                .subclip((start_min,start_sec),(end_min, end_sec)))
        if path.basename(output_path) is '':
            clip.write_gif('{}/{}.gif'.format(path.dirname(output_path), datetime.now().strftime('%Y-%m-%d.%H.%M.%S')))
        else:
            clip.write_gif(output_path)
    except Exception as e:
        print(e)
    finally:
        rmtree(temp_dir)


if __name__ == '__main__':
    fire.Fire(create_gif_from_youtube_video)
