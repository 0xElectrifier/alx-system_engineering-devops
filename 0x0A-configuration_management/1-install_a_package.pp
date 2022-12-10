# Installs 'flask' from 'pip3'

python::pip { 'flask':
  ensure       => '2.1.0',
  pip_provider => 'pip3',
  pkgname      => 'flask',
}
