# pro6db-dashboard

**A web interface for viewing all your ProPresenter songs and playlists**

At sunday mornings, a very common question from the worship leader is "does this song exist in the ProPresenter database"?
That question can be answered with an easily accessible tool.

So, here we are.

## Mac Client Setup

The pro6db-dashboard require the following propresenter files:

- The default pro6pl file, located at `~/Library/Application Support/RenewedVision/ProPresenter6/Playlists/ProPresenter6.pro6pl` by default
- The pro6 song files, located at `~/Documents/ProPresenter6` by default

For your convenience, I've created a service that can run on your Propresenter 6 Mac
that

1. converts the above mentioned files to json
2. copies the json files to a configured S3-compatible server

To install the service user-wide, run the following

```bash
pip install https://github.com/MrYakobo/pro6-dashboard

# run once to init config
pro6-dashboard-sync

# edit the config with your bucket credentials, then try syncing again
pro6-dashboard-sync

# when you see it's working, enable the service (will run every 30 minutes)
pro6-enable-service
```

The configuration resides in `~/.config/pro6-dashboard/config.toml`
and is documented in [the example config](./sync_service/pro6_dashboard_sync/example.config.toml)

## Deploying the web app

The web app requires the urls `$VITE_DATA_BASE_URL/data/songs.json` and `$VITE_DATA_BASE_URL/data/songs.json` to be accessible anonymously, and allow CORS.

Build the web app like this:

```bash
cd web
npm install
VITE_DATA_BASE_URL=https://your-s3-compatible-server/bucket_name npm run build
```

Then deploy dist/* on your web server.

```bash
scp dist/* your_server:/var/www
```