# Adds some content
node default {
file { '/etc/ssh/ssh_config':
ensure  => 'present',
content => '   IdentityFile ~/.ssh/holberton
   PasswordAuthentication no'
}
}
