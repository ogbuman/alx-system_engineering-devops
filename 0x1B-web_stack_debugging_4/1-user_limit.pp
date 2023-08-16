# fix OS limit a holberton user

exec { 'replace-hard':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 8192/" /etc/security/limits.conf',
  before   => Exec['replace-soft'],
  }

exec { 'replace-soft':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 4096/" /etc/security/limits.conf',
  }
