#!/usr/bin/env bash
# Change the OS configuration
exec { 'Fix hard limit':
  command => "sed -i '56c holberton hard nofile 1048576' /etc/security/limits.conf",
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}

exec { 'Fix soft limit':
  command => "sed -i '57c holberton soft nofile 1048576' /etc/security/limits.conf",
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}
