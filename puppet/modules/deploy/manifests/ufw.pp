class deploy::ufw {
  class { 'ufw': }
  ufw::allow { 'ssh':
    port => '22',
  }
  ufw::allow { 'http':
    port => '80',
  }
  ufw::allow { 'tls':
    port => '443',
  }
}
