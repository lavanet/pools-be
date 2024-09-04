class django::utils {
  package { "build-essential": }
  package { "gettext": }
  package { "htop": }
  package { "libffi-dev": }
  # package { "libfreetype6-dev": } # Installed package reinstalls everytime puppet runs.
  package { "libjpeg-dev": }
  package { "libmemcached-dev": }
  package { "libcairo2": }
  package { "libgdk-pixbuf2.0-0": }
  package { "libpango-1.0-0": }
  package { "libpangocairo-1.0-0": }
  package { "libpng-dev": }
  package { "memcached": }
  package { "net-tools": }
  package { "redis-server": }
  package { "screen": }
  package { "shared-mime-info": }
  package { "slurm": }
  package { "tree": }
  package { "zlib1g-dev": }
}
