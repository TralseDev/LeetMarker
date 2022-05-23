#!/bin/bash

echo "[*] Installation started!"
mkdir ~/.mozilla/native-messaging-hosts 2>/dev/null
home=$HOME
homedir=${home//[\/]/\\/}
sed -i "s/~/${homedir}/" ./app/LeetMarker_native.json
sed -i "s/~/${homedir}/" ./app/restore.sh
cp ./app/LeetMarker_native.json ~/.mozilla/native-messaging-hosts/LeetMarker_native.json
cd ../
mv ./LeetMarker ~/.LeetMarker
cd ~/.LeetMarker/app
chmod +x *.py
chmod +x ./restore.sh
./restore.sh
echo "[*] Installed successfully!"
