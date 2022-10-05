#!/bin/sh

echo 'Copying Mono'
script_dir=$(dirname "$0")
cp -R $script_dir/Mono /tmp

echo 'Copying VS Code Settings'
cp $script_dir/settings.json $HOME/Library/Application\ Support/Code/User/