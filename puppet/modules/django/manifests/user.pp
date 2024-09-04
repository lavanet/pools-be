class django::user (
  $home     = $django::conf::home,
  $user     = $django::conf::user,
  $key_file = "$home/.ssh/id_rsa",
) {
  group { $user:
    ensure => present,
  } ->

  user { $user:
    ensure     => present,
    groups     => [$user],
    home       => $home,
    managehome => true,
    shell      => '/bin/bash',
  } ->

  file { $home:
    ensure => directory,
    group  => $user,
    owner  => $user,
    mode   => "755",
  } ->

  file { "$home/.ssh":
    ensure => directory,
    group  => $user,
    owner  => $user,
    mode   => "700",
  } ->

  exec { "ssh-key-$user":
    user    => $user,
    path    => ["/usr/bin"],
    onlyif  => "test ! -f $key_file",
    command => "ssh-keygen -N \"\" -f $key_file",
  }
}
