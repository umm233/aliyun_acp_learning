#!/bin/bash

# Check if Firefox is installed.  Different distributions might have slightly 
# different ways of checking, so we'll try a few common methods.

if which firefox >/dev/null 2>&1; then
  echo "Firefox is already installed."
else
  if command -v firefox >/dev/null 2>&1; then  # Another check, more portable.
    echo "Firefox is already installed."
  else
    if [ -f /usr/bin/firefox ]; then  # Check for the binary directly.
      echo "Firefox is already installed."
    else
      echo "Firefox is not installed.  Running install_firefox.sh..."
      # Run the installation script. Make it executable first if necessary.
      sudo install -d -m 0755 /etc/apt/keyrings

      wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null

      gpg -n -q --import --import-options import-show /etc/apt/keyrings/packages.mozilla.org.asc | awk '/pub/{getline; gsub(/^ +| +$/,""); if($0 == "35BAA0B33E9EB396F59CA838C0BA5CE6DC6315A3") print "\nThe key fingerprint matches ("$0").\n"; else print "\nVerification failed: the fingerprint ("$0") does not match the expected one.\n"}'

      echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null

      echo '
Package: *
Pin: origin packages.mozilla.org
Pin-Priority: 1000
' | sudo tee /etc/apt/preferences.d/mozilla

      sudo apt-get update -qq && sudo apt-get install firefox -y -qq


      # Check installation result.
      if which firefox >/dev/null 2>&1; then
        echo "Firefox installed successfully."
      else
        echo "Firefox installation failed. Check install_firefox.sh for errors."
      fi
    fi
  fi
fi