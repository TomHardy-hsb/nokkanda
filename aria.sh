if [ -z $TORRENT_TIMEOUT ]
then
   TORRENT_TIMEOUT=0
fi
tracker_list=$(curl -Ns https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/all.txt https://ngosang.github.io/trackerslist/trackers_all_http.txt https://newtrackon.com/api/all https://raw.githubusercontent.com/hezhijie0327/Trackerslist/main/trackerslist_tracker.txt | awk '$0' | tr '\n\n' ',')
aria2c --enable-rpc --rpc-listen-all=false --rpc-listen-port 6800 \
  --max-connection-per-server=8 --rpc-max-request-size=1024M \
  --seed-time=0.01 --min-split-size=10M --follow-torrent=mem --split=4 \
   --daemon=true --allow-overwrite=true --max-overall-download-limit=$MAX_DOWNLOAD_SPEED \
   --max-overall-upload-limit=1K --max-concurrent-downloads=$MAX_CONCURRENT_DOWNLOADS \
   --bt-stop-timeout=480 --peer-id-prefix=-qB4250- --user-agent=qBittorrent/4.4.2
