class django::uwsgi (
  $user            = $django::conf::user,
  $path            = $django::conf::path,
  $project         = $django::conf::project,
  $uwsgi_path      = "$django::conf::home/uwsgi",
  $uwsgi_ini       = "$uwsgi_path/uwsgi.ini",
  $uwsgi_pid       = "$uwsgi_path/uwsgi.pid",
  $uwsgi_processes = $django::conf::uwsgi_processes,
  $uwsgi_threads   = $django::conf::uwsgi_threads,
  $venv            = $django::conf::venv,
) {

  file { $uwsgi_path:
    ensure => directory,
    group  => $user,
    owner  => $user,
  }

  file { $uwsgi_ini:
    ensure  => file,
    group   => $user,
    owner   => $user,
    mode    => "700",
    content => template("django/uwsgi.erb"),
    require => File[$uwsgi_path],
    notify  => Exec["uwsgi-restart"],
  }

  exec { "uwsgi-restart":
    user        => $user,
    cwd         => $path,
    path        => ["/bin", "/usr/bin"],
    onlyif      => "test -f $uwsgi_pid",
    command     => "kill -HUP $(cat $uwsgi_pid)",
    refreshonly => true,
    require     => [
      Exec["venv-requirements"],
      File[$uwsgi_ini],
    ],
  }
}
