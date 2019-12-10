# Beer List

This project aims to provide simple interface to get lists of beers from my favourite pubs.

## Supported pubs

* [Malt Worm](https://maltworm.cz/)
* [Ochutnávková pivnice](http://ochutnavkovapivnice.cz/)
* [Craftbeer bottle shop & bar](https://www.facebook.com/Craftbeerbottleshopbar/)

## Howto use

The parsers can be used separately, there are just a few simple dependencies.

To run as web service under Apache:
* check out the code to a web accessible directory with PHP support
* change owner of `tmp` directory to that of the web server (e.g. www-data)
* allow mod_rewrite (a2enmod rewrite)
* allow .htaccess for the dir
```
        <Directory /var/www/html/beer>
                AllowOverride All
        </Directory>
```
