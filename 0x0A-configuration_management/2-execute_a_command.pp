# Puppet manifest that executes a kill command

exec {'killmenow':
  path    => '/usr/bin/:/usr/sbin:/bin',
  command => 'pkill -f killmenow',
}
