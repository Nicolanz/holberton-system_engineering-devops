# kill a process
exec { 'Configure a server':
command => "sed -i 's/server_name _;/add_header X-Served-By $HOSTNAME;/' /etc/nginx/sites-enabled/default;",
path    => ['/usr/bin', '/usr/sbin',],
}
