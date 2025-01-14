# This Puppet manifest terminates a process named "killmenow" using pkill
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'pgrep -f killmenow',
}