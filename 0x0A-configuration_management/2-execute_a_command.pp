#Kills the process named "killmenow" using pkill
exec { 'killmenow':
command => 'pkill -f killmenow',
path => 'usr/bin',
}
