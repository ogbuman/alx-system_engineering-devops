# create a file in tmp folder with puppet 
file { '/tmp/school':
        content => 'I love Puppet',
        mode    => '0744',
        owner   => 'www-data',
        group   => 'www-data',
}
