# poppet file to fix a wordpress site 5xx error to 200 ok
# changing the misstyped .phpp to php in the /var/www/html/wp-settings.php file

exec{'fix worldpress-server-error'
    command => 'sed -i s/phpp/g /var/www/wp-settings.php',
    path    => '/user/bin/:/bin/',
}
