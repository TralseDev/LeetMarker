import os
from Logger import Logger


TEMPLATE_PATH = f"{os.path.expanduser('~')}/.LeetMarker/app/template"


def create_template():
    try:
        with open(TEMPLATE_PATH, 'a+') as template:
            template.write("# DO NOT DELETE THIS FILE! THIS FILE IS THE TEMPLATE FOR ALL OTHER FILES THAT WILL BE CREATED BY LeetMarker_native.py\n#\n# Headline: [Headline]\n#\n# Link:\n# # for full link (with URL parameter): [LINK_FULL] ; i.e.: https://google.com/search?query=some+text\n# # for only domain name: [LINK_DOMAIN] ; i.e.: google.com\n# # for full link (without URL parameter): [LINK_HREF] ; i.e.: https://google.com/search\n# # for path (without URL parameter): [LINK_PATH] ; i.e.: /search\n# # for path (with URL parameter):  [LINK_PATH_FULL] ; i.e.: /search?query=some+text\n#\n# Copied text: [text]\n#\n# Time: [time]\n# # default: %Y:%M:%d ~ %H:%m:%S\n#\n#\n# OR: type in [DEFAULT] for default values\n#\n# [DEFAULT] template looks like:\n#\n# [Headline]\n# ----------\n# \n# Link: [LINK_FULL]\n#\n# Selected text: [text]\n#\n# Created @ [time]\n\n[DEFAULT]\n")

    except PermissionError:
        Logger.log("PLEASE RERUN LEETMAKRER_NATIVE AS SUDO!", 'c')
        exit(-1)


def template_file_exists(file_path: str = TEMPLATE_PATH) -> bool:
    return bool(os.path.isfile(file_path))


if __name__ == '__main__' and not template_file_exists():
    create_template()
