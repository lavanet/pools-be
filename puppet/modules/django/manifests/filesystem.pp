class django::filesystem (
  $user      = $django::conf::user,
  $home      = $django::conf::home,
  $path      = $django::conf::path,
  $venv      = $django::conf::venv,
  $puppet_sh = $django::conf::puppet_sh,
) {
  file { "$home/activate":
    ensure  => file,
    group   => $user,
    owner   => $user,
    mode    => "700",
    content => template("django/activate.erb"),
  } ->

  file_line { 'bashrc_activate':
    path => "$home/.bashrc",
    line => "source $home/activate",
  }

  file { "$home/node_mount":
    ensure  => file,
    group   => $user,
    owner   => $user,
    mode    => "700",
    content => template("django/node_mount.erb"),
  }

  file { "/bin/pm":
    ensure  => present,
    group   => 'root',
    owner   => 'root',
    mode    => "755",
    content => template("django/pm.erb"),
  }

  file { "/bin/pi":
    ensure  => present,
    group   => 'root',
    owner   => 'root',
    mode    => "755",
    content => template("django/pi.erb"),
  }

  file { "/bin/update":
    ensure  => present,
    group   => 'root',
    owner   => 'root',
    mode    => "744",
    content => template("django/update.erb"),
  }

  tidy { '/opt/puppetlabs/puppet/cache/reports':
    age     => '1d',
    matches => "*.yaml",
    recurse => true,
    rmdirs  => false,
    type    => ctime,
  }

  file { "/bin/apply":
    ensure  => file,
    group   => "root",
    owner   => "root",
    mode    => "744",
    content => template("django/apply.erb"),
  }

  file { "/bin/suu":
    ensure  => file,
    group   => "root",
    owner   => "root",
    mode    => "755",
    content => template("django/suu.erb"),
  }

  file { "/bin/ssc":
    ensure  => file,
    group   => "root",
    owner   => "root",
    mode    => "755",
    content => template("django/ssc.erb"),
  }
}
