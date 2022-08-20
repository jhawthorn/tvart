# tvart
Self hosted flask app with preact frontend to upload art to a Samsung "The Frame" TV.

Based on https://github.com/xchwarze/samsung-tv-ws-api

### Usage

```
docker run -d -n tvart -e TV_IP=<your TV's IP> -p 8080:8080 ghcr.io/jhawthorn/tvart:main
```

---

<img width="1086" alt="Screen Shot 2022-08-20 at 12 09 54 PM" src="https://user-images.githubusercontent.com/131752/185762740-8b1528e8-6551-4026-b53e-e846a5b64dec.png">
