class django::daphne (
  $user = $django::conf::user,
  $path = $django::conf::path,
  $home = $django::conf::home,
) {
  $daphne_path = "$home/daphne"

  file { $daphne_path:
    ensure => directory,
    group  => $user,
    owner  => $user,
  }

  exec { "daphne-restart":
    user        => $user,
    cwd         => $path,
    path        => ["/bin", "/usr/bin"],
    command     => "pkill -HUP daphne; true",
    refreshonly => true,
  }
}
