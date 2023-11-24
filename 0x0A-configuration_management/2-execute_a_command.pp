#Kills the process named "killmenow" using pkill
exec { 'kill_killmenow_process':
command => 'pkill killmenow',
refreshonly => true,
onlyif => 'pgrep killmenow
}
