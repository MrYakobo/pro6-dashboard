# pro6db-dashboard

**A web interface for viewing all your ProPresenter songs and playlists**

At sunday mornings, a very common question from the worship leader is "does this song exist in the ProPresenter database"?
That question can be answered with an easily accessible tool.

So, here we are.

## Technical Background

Propresenter6 manages it's database in PList XML (.pro6pl for playlists, .pro6 for song files). To make this data accessible for a web client, I've written conversion scripts to JSON.

For maximum availability, I recommend using [Cloudflare R2][1] (but any S3-compatible service ought to work) for hosting these JSON files. It's free and nice hosting. The program `pro6-dashboard-sync` takes care of that.

You can also self-host everything. Then you'll need to upload `songs.json` and `playlists.json`, generated from `pro6-dashboard-convert`, to your own web server.

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
pip3 install git+https://github.com/MrYakobo/pro6-dashboard#subdirectory=sync_service

# run once to init config
pro6-dashboard-sync

# edit the config with your s3 bucket credentials, then try syncing again
pro6-dashboard-sync

# when you see it's working, enable the service (will run every 30 minutes)
pro6-enable-service
```

The configuration resides in `~/.config/pro6-dashboard/config.toml`
and is documented in [the example config](./sync_service/pro6_dashboard_sync/example.config.toml)

## Deploying the web app

This will require `npm` to be installed on your development machine, to "burn-in" the S3 bucket url.

The web app requires the urls `$VITE_DATA_BASE_URL/songs.json` and `$VITE_DATA_BASE_URL/songs.json` to be accessible anonymously, and over CORS.

Build the web app like this:

```bash
cd web
npm install
VITE_DATA_BASE_URL=https://your-s3-compatible-server/bucket_name/data npm run build
```

Then deploy dist/* on your web server. I recommend using [Cloudflare Pages][2] for that.

```bash
# your own web server
scp dist/* your_server:/var/www

# cloudflare pages
npx wrangler pages project create
npx wrangler pages deploy dist
```

[1]: https://www.cloudflare.com/developer-platform/r2/
[2]: https://pages.cloudflare.com/