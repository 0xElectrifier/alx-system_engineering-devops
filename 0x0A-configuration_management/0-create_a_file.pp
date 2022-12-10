# My First `Puppet` resource creation
file {'school':
  content => 'I love Puppet',
  mode    => '0744',
  group   => 'www-data',
  owner   => 'www-data',
  path    => '/tmp/school',
}
