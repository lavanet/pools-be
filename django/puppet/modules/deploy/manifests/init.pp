class deploy (
  $username = 'deploy',
) {

  class { 'deploy::user':
    username => $username,
  }

  class { 'deploy::filesystem':
    username => $username,
    require  => Class['deploy::user'],
  }

  class { 'deploy::ssh':
    require => Class['deploy::filesystem'],
  }

  package { "fail2ban": }

  service { "puppet":
    ensure => stopped,
    enable => false,
  }

  service { "mcollective":
    ensure => stopped,
    enable => false,
  }

  class { 'deploy::ufw': }
}
