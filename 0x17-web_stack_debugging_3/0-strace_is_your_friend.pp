#fix It
exec { 'debugging':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/bin:/sbin:/bin:/usr/sbin'
}
