import os
from os import path
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
SCREENSHOTS_FOLDER = path.expandvars(os.environ.get("SCREENSHOTS_FOLDER"))
screenshots = {}


class Screenshot:
    def __init__(self, date, time, char_name, event_name, file_name):
        self.char_name = char_name
        self.date = date
        self.time = time
        self.event_name = event_name
        self.file_name = file_name

    def __str__(self):
        return f"{self.date} {self.time} {self.char_name} {self.event_name} {self.file_name}"


def read_folder(folder):
    dir_list = os.listdir(folder)
    for file in dir_list:
        metadata = file.split(".")[0].split("_")
        screenshot = Screenshot(metadata[0], metadata[1], metadata[2], metadata[3], file)
        if screenshot.char_name not in screenshots.keys():
            screenshots[screenshot.char_name] = {}
        if screenshot.event_name not in screenshots[screenshot.char_name].keys():
            screenshots[screenshot.char_name][screenshot.event_name] = {}
        i = len(screenshots[screenshot.char_name][screenshot.event_name])
        screenshots[screenshot.char_name][screenshot.event_name][i] = screenshot


def mov_files(folder, screenshots):
    for character, events in screenshots.items():
        print(f"{folder}")
        print(f"{character}")
        for event, items in events.items():
            print(f"\t{event} {items}")


if __name__ == '__main__':
    read_folder(SCREENSHOTS_FOLDER)
    print(screenshots)
    mov_files(SCREENSHOTS_FOLDER, screenshots)
