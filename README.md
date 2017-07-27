# MistLogic Device

## Módulo de Red

Se necesitan añadir las siguientes lineas al archivo `/etc/network/interfaces`.

```bash
allow-hotplug wlan0
iface wlan0 inet manual
post-up /usr/bin/python /etc/mistlogic/netctl.py
```
