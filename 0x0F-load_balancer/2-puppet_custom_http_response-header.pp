# Create custom HTTP header response using Puppet
exec { 'update':
    command => "/usr/bin/apt-get -y update"
}

package { 'nginx':
    ensure   => 'installed',
    provider => 'apt',
    require => Exec['update']
}

exec { 'Create custom HTTP header':
    command => "/usr/bin/env sed -i '/^\tserver_name.*/a \\\tadd_header X-Served-By ${hostname};\n' /etc/nginx/sites-available/default"
    require => Package['nginx']
}

service { 'restart':
    ensure  => running,
    require => Exec['Create custom HTTP header'],
    restart => 'sudo service nginx restart',
}
