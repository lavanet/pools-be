class django::git (
  $user           = $django::conf::user,
  $path           = $django::conf::path,
  $project        = $django::conf::project,
  $git_name       = $django::conf::git_name,
  $git_branch     = $django::conf::git_branch,
  $git_host       = "bitbucket.org",
  $git_url        = "git@$git_host:$git_name",
  $known_hosts    = "$django::conf::home/.ssh/known_hosts",
  $local_settings = $django::conf::local_settings,
) {

  exec { "$git_host-ssh-keyscan":
    user    => $user,
    path    => ["/bin", "/usr/bin"],
    unless  => "grep -q $git_host $known_hosts",
    command => "ssh-keyscan -H $git_host >> $known_hosts && echo \"# $git_host\" >> $known_hosts",
  } ->

  vcsrepo { $path:
    ensure   => latest,
    provider => git,
    source   => $git_url,
    user     => $user,
    revision => $git_branch,
  } ->

  file { "$path/config/local_settings.py":
    ensure  => file,
    group   => $user,
    owner   => $user,
    mode    => "600",
    content => template("django/local_settings.erb"),
  } ->

  file { "$path/config/local_env.py":
    ensure => file,
    group  => $user,
    owner  => $user,
    mode   => "600",
  }
}
