# Sets up your client SSH configuration file to use a private key and
# authenticate without a password
include stdlib

file_line { 'USE private key':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'TURN OFF Password Auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
