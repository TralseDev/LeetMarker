#!/bin/bash

YELLOW='\033[1;33m'
MAGENTA='\033[0;35m'
RESET='\033[0m'

printf "${YELLOW}[*] Restoring files...\n"

FOLDER_PATH="~/.LeetMarker/app/"
rm $FOLDER_PATH/ERROR $FOLDER_PATH/INFO $FOLDER_PATH/LOG 2> /dev/null

if [[ ! $(ls $FOLDER_PATH/template) ]]; then
    python3 $FOLDER_PATH/utils.py > /dev/null;
else
    printf "$YELLOW"
    echo -n "Restore default template file (y/N): "
    read template_option
    template_option=$(echo "$template_option" | tr '[:upper:]' '[:lower:]')
    if [[ $template_option == 'y' ]]; then
        printf "${YELLOW}[*] Restoring template file...\n"
        rm $FOLDER_PATH/template 2>/dev/null
        python3 $FOLDER_PATH/utils.py > /dev/null
        printf "${MAGENTA}[i] Restored template file!\n";
    fi
fi

echo -n 'Remove data folder (y/N): '
read option
option=$(echo "$option" | tr '[:upper:]' '[:lower:]')

if [[ $option == 'y' ]]; then
    printf "${YELLOW}[*] Removing files...\n"
    rm -rf $FOLDER_PATH/data 2>/dev/null
    printf "${MAGENTA}[i] Removed files!\n";
fi

mkdir data 2>/dev/null

printf "${MAGENTA}[i] Restored successfully!${RESET}\n"
