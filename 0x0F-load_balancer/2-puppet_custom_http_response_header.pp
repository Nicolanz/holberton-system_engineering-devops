# Configure a server
exec { 'configureItKnow':
command => "sed -i 's/server_name _;/add_header X-Served-By $HOSTNAME;/' /etc/nginx/sites-enabled/default;",
path    => ['/usr/bin', '/usr/sbin',],
}
