class django::postgresql (
  $user = $django::conf::user,
  $db_name = $django::conf::postgresql_db_name,
  $db_pass = $django::conf::postgresql_db_pass,
) {
  class { 'postgresql::server': } ->

  package { 'libpq-dev':
    ensure => present,
  } ->

  postgresql::server::role { $user:
    password_hash => postgresql::postgresql_password($user, $db_pass),
    createdb      => true,
    superuser     => true,
  } ->

  postgresql::server::db { $db_name:
    user => $user,
  }
}
