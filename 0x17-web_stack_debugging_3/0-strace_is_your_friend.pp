#fix It
exec { 'debugging':
    command => 'sed -i s/phpp/php/ /var/www/html/wp-settings.php',
    path    => '/usr/bin:/sbin:/bin:/usr/sbin'
}
