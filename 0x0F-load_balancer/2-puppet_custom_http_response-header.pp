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

exec { 'Create custom HTTP header':
    path    => '/usr/bin/env bash',
    command => "sed -i '/^\tserver_name.*/a \\tadd_header X-Served-By ${hostname};\n' /etc/nginx/sites-available/default"
}
