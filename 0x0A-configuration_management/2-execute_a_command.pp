# create a manifest that kills a process
exec { 'pkill':
  command => 'pkill -x killmenow',
  path    => '/usr/bin/',
  returns => [0,1],
}