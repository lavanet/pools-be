class django::supervisor (
  $user             = $django::conf::user,
  $home             = $django::conf::home,
  $path             = $django::conf::path,
  $project          = $django::conf::project,
  $venv             = $django::conf::venv,
  $celery_processes = $django::conf::celery_processes,
) {
  package { "supervisor": } ->

  file { "/etc/supervisor/conf.d/program_$user.conf":
    ensure  => file,
    group   => $user,
    owner   => $user,
    mode    => "644",
    content => template("django/supervisord.erb"),
    notify  => Exec["supervisor-reload"],
  } ->

  exec { "supervisor-reload":
    user        => "root",
    path        => ["/usr/bin", "/usr/local/bin"],
    command     => "supervisorctl reload",
    refreshonly => true,
  }
}
