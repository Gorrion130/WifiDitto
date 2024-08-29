# WifiDitto

A script to bypass a whole bunch of WiFi captive portals (e.g. at hotels, cruise ships etc.)

# Dependencies

<li>bash</li></ul>

# Installation

<h3>General installation</h3> 

It's pretty easy! Just execute the following command:

<pre><code>git clone https://github.com/Gorrion130/WifiDitto/ && cd WifiDitto && makepkg -si</code></pre>

# How to use it

Just run WifiDitto with

<pre><code>sudo wifiditto {wireless interface name} {target AP name}</code></pre>

For example, if your interface was called <code>wlan0</code> and you were targeting <code>Free Hotel WiFi</code>, then you would run

<pre><code>sudo wifiditto wlan0 'Free Hotel WiFi'</code></pre>

This will start scanning for associated MAC addresses. Once you think there are enough clients in airodump-ng, hit ctrl-c and then each MAC assoctiated to your target will be checked for internet access.

If one of the MACs does have internet access, you'll be asked if you would like to start a hotspot on your device (if you're nice and want to share) or just keep it all for yourself. Mwahahahaa.

If it doesn't work at first, maybe try walking around with your device in order to gain more MAC addresses to check.

That's it. Please forgive ugly code, and enjoy!
