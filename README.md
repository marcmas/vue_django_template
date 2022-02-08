# vue_django_template
vue in django template
# install webpack-bundle-tracker
#### https://github.com/django-webpack/django-webpack-loader
#### npm install --save-dev webpack-bundle-tracker
### create vue.config.js and add this
##### change ports in webpack-stats.json for all created apps
````
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    publicPath: "http://0.0.0.0:8080",
    outputDir: "./dist/",

    chainWebpack: config => {
        config.optimization.splitChunks(false)

        config.plugin('BundleTracker').use(BundleTracker, [
            {
                filename: './webpack-stats.json'
            }
        ])

        config.resolve.alias.set('__STATIC__', 'static')

        config.devServer
            .public('http://0.0.0.0:8080')
            .host('0.0.0.0')
            .port(8080)
            .hotOnly(true)
            .watchOptions({poll: 1000})
            .https(false)
            .headers({'Access-Control-Allow-Origin': ['\*']})
    }
};
````
# install django-webpack-loader
#### https://github.com/django-webpack/django-webpack-loader
#### pip install django-webpack-loader
#### add to install apps
````
WEBPACK_LOADER = {
    'POOLS': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'webpack_bundles/', # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'polls/frontend/webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
        'LOADER_CLASS': 'webpack_loader.loader.WebpackLoader',
    },
    'POOLS2': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'webpack_bundles/', # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'polls2/frontend/webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
        'LOADER_CLASS': 'webpack_loader.loader.WebpackLoader',
    }
}
````
#index.html first app
````
{% load render_bundle from webpack_loader %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% render_bundle 'app' 'css' 'POOLS' %}
    <title>Document</title>
</head>
<body>
    <h1>some data 2asdsad</h1>
    <div id="app"></div>
    {% render_bundle 'app' 'js' 'POOLS' %}
</body>
</html>
````
#index.html second app
````
{% load render_bundle from webpack_loader %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% render_bundle 'app' 'css' 'POOLS2' %}
    <title>Document</title>
</head>
<body>
    <h1>some data 2asdsad</h1>
    <div id="app"></div>
    {% render_bundle 'app' 'js' 'POOLS2' %}
</body>
</html>
````
