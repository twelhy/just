#!/bin/bash
ipv6=$(curl -6 -s ifconfig.me)

if [[ -n "$ipv6" ]]; then
    echo "IPv6 found: $ipv6"
    curl "https://www.duckdns.org/update?domains=twelhy&token=3ca4f6bf-ac33-4366-9e16-f4b0a94765a2&verbose=true&ipv6=$ipv6"
else
    echo "No IPv6 address detected!"
fi
