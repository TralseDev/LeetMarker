# LeetMarker

LeetMarker is my first Firefox extension. It saves all selected text on any website into a file.

## Getting Started

### Native installation
Python version 3+
```
git clone https://github.com/TralseDev/LeetMarker.git
cd LeetMarker
chmod +x ./install.sh
./install.sh
```

### Installing add-on
1. Open Firefox
2. Go to `about:config` and set `xpinstall.signatures.required` to `false` to be able to install unsigned add-ons
3. Press Ctrl+Shift+A and then press Settings (gear icon) next to the add-on search bar
4. Select "`Install Add-on from Fileâ€¦`"
5. Select file: `~/.LeetMarker/release.xpi` and allow the extension
6. Have fun! You can find all log files and saved data inside directory: `~/.LeetMarker/app` and `~/.LeetMarker/app/data`!

## Authors

Tralse

## Version History

* 1.0 (23.5.2022)
    * Stable version

## License

This project is licensed under the GNU General Public License v3.0 (GNU GPLv3 License)