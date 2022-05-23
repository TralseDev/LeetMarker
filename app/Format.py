import re
import os
from Logger import Logger
from datetime import datetime


PATH = f"{os.path.expanduser('~')}/.LeetMarker/app/"
TEMPLATE_PATH = f"{PATH}template"


class InvalidLink(Exception):
    '''
        Is raised when invalid link is set as link
    '''


class Format:
    '''
        Format class
    '''

    def __init__(self, output_format: str = TEMPLATE_PATH, time_format: str = "%Y:%M:%d ~ %H:%m:%S"):
        '''
            Formats should be set (if needed)
        '''
        with open(output_format) as output_file:
            lines = output_file.readlines()
            for line in lines:
                if line.startswith('#'):
                    lines.remove(line)
                    continue
                self.default = '[DEFAULT]' in line

        self.__link_formats = [
            "[LINK_FULL]", "[LINK_DOMAIN]", "[LINK_HREF]", "[LINK_PATH]", "[LINK_PATH_FULL]"
        ]
        self.output_format = output_format

        self.link_format = "[FULL_LINK]"
        self.time_format = time_format

        self.headline = None
        self.link = None
        self.selected_text = None
        self.time = datetime.now().strftime(
            time_format.replace('[', '').replace(']', ''))

        self.regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            # domain...
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    def validate_link(self, link: str) -> bool:
        return re.match(self.regex, link) is not None

    def set_headline(self, headline: str):
        self.headline = headline

    def set_selected_text(self, text: str):
        self.selected_text = text

    def set_link(self, link: str):
        if not self.validate_link(link):
            raise InvalidLink(f"{link}")

        self.link = link

    def get_link(self, link_format: str):
        '''
            :link: has to be full link including domain name, path and url parameters
        '''

        link = self.link

        if link_format == "[LINK_DOMAIN]":
            link = link.split("://")[1].split("/")[0]

        elif link_format == "[LINK_HREF]":
            link = link.split("?")[0]

        elif link_format == "[LINK_PATH]":
            link = ('/' + link.split('/', 3)[-1]).split('?')[0]

        elif link_format == "[LINK_PATH_FULL]":
            link = '/' + link.split('/', 3)[-1]

        #self.link = link
        return link

    def set_time(self):
        self.time = datetime.now().strftime(self.time_format)

    def write(self):
        for i in {self.headline, self.link, self.selected_text}:
            if not i:
                Logger.log(
                    f"ProgrammingError: One of the variables was not set! Exiting...", 'e')
                exit(-1)

        if self.default:
            format_string = f"""{self.headline}
{"-" * (len(self.headline))}

Link: {self.link}

Selected text: {self.selected_text}

Created @ {self.time}

"""

        else:
            with open(self.output_format, 'r') as file:
                format_file = file.readlines()
                format_string = "".join(
                    line for line in format_file if not line.startswith('#')
                )

                # set link
                for f in self.__link_formats:
                    format_string = format_string.replace(f, self.get_link(f))

                # set headline
                format_string = format_string.replace(
                    '[Headline]', self.headline)

                # set selected text
                format_string = format_string.replace(
                    '[text]', self.selected_text)

                # set time
                format_string = format_string.replace('[time]', self.time)

        if not os.path.isdir(f"{PATH}data"):
            os.mkdir(f"{PATH}data")

        directory = f"{PATH}data/{self.get_link('[LINK_DOMAIN]')}"
        if not os.path.isdir(directory):
            os.mkdir(directory)

        with open(f"{directory}/{self.headline}", 'a+') as output_file:
            output_file.write(format_string + '\n')

        return format_string
