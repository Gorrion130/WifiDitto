# houdini
Script to bypass WiFi captive portals (e.g. at hotels, cruise ships etc.)

# Requirements (kali install and update code):

<code>
apt install hostapd aircrack-ng python3
</code>

First use:
<code>
  git clone https://github.com/ariakis/houdini/ && cd houdini
  chmod +x houdini
  cd modules && chmod +x *
  cd ..
</code>

Then just run houdini with
<code>
  ./houdini {name of access point once internet access is confirmed} {password of access point}
</code>

Please forgive ugly code, and enjoy!
