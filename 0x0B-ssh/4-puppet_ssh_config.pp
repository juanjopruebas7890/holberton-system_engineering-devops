# ssh config using puppet
file { '/etc/ssh/ssh_config':
    ensure  => file,
    content => 'Host my_server
    HostName 35.196.86.108
    User ubuntu
    IdentityFile ~/.ssh/holberton
    PasswordAuthentication no',
}