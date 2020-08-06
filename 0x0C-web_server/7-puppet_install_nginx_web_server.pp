# Configure server with Puppet
package { 'nginx':
    ensure   => installed,
    provider => 'apt',
}

service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
    restart => 'sudo service nginx restart',
}

file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Holberton School',
}

file_line { '301 redirect':
    ensure => 'present',
    path   => '/etc/nginx/sites-available/default',
    line   => return 301 'https':#www.holbertonschool.com$request_uri;
    after  => '/var/www/html;'
}
