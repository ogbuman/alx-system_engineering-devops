# puppet script that renames files .

exec { 'rename_file':
  command => 'sudo cp /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  path    => '/bin',
  onlyif  => 'test -f /var/www/html/wp-includes/class-wp-locale.php',
}
