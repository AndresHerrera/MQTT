# MQTT and Mosquitto

### Install mosquitto

```bash
$ sudo aptitude install mosquitto
$ sudo aptitude install mosquitto-clients
```

Edit mosquitto.conf

```conf
listener 1883 0.0.0.0
allow_anonymous true
```

Start mosquitto

```bash
$ mosquitto -c mosquitto.conf
```

Subscriber home/kitchen/principal

```bash
$ mosquitto_sub -h 127.0.0.1 -p 1883 -t "home/kitchen/principal" -v
```

Subscriber config

```bash
$ mosquitto_sub -h 127.0.0.1 -p 1883 -t "home/#" -v
```

Publisher topic

```bash
$ mosquitto_pub -h 127.0.0.1 -p 1883 -t "home/kitchen/principal" -m "{ status: 'on' }"
```

Form Python

```bash
$ pip install --user paho-mqtt
```