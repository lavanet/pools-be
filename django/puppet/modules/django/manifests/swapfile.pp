class django::swapfile {
  swap_file::files { 'default':
    ensure => present,
  }
}
