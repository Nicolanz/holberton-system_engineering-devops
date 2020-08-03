# Creates a file with puppet
node default {
file { '/tmp/holberton':
ensure  => 'present',
mode    => '0744',
group   => 'www-data',
owner   => 'www-data',
content => 'I love Puppet',
}
}
