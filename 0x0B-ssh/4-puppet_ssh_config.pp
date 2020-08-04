# Use Puppet to make changes to config file
file_line { 'change config file':
    path => '~/.ssh/holberton',
    line => 'PasswordAuthentication no',
}
