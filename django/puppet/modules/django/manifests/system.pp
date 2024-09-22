class django::system (
  $timezone = $django::conf::timezone,
) {
  class { 'timezone':
    timezone => $timezone,
  }

  package { "chrony": } ->
  service { "chrony":
    ensure => running,
    enable => true,
  }
}
