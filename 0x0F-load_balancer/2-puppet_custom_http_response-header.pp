# Create custom HTTP header response using Puppet
package { 'nginx':
    ensure   => installed,
    provider => 'apt',
}

service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
    restart => 'sudo service nginx restart',
}

file {'/etc/nginx/sites-available/default':
    ensure => file
}

file_line { 'Create a custom HTTP header':
    ensure => 'present',
    path   => '/etc/nginx/sites-available/default',
    line   => add_header X-Served-By $hostname;
    after  => 'server_name _;'
}
