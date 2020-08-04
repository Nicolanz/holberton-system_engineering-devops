# kill a process
exec { 'killItNow':
command => 'pkill killmenow',
path    => ['/usr/bin', '/usr/sbin',],
}
