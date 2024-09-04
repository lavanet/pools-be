node /^dev\./ {
  class { "django::conf":
    user               => "vagrant",
    path               => "/vagrant",
    nginx_template     => "dev",
    postgresql_db_pass => "a",
    deploy             => false,
    autodeploy         => false,
    puppet_sh          => '/vagrant/puppet/sh',
    swap               => false,
  } ->
  class { "django::core": }
}
