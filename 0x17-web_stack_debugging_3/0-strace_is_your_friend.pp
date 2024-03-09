# Fixes Apache web server that returns code 500 error

exec {'replace_php':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
