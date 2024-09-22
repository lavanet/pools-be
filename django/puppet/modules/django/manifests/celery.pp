class django::celery (
  $user = $django::conf::user,
  $home = $django::conf::home,
  $path = $django::conf::path,
) {
  $celery_path = "$home/celery"
  $celery_beat_pid = "$celery_path/beat.pid"
  $celery_worker_pid = "$celery_path/worker.pid"

  file { $celery_path:
    ensure => directory,
    group  => $user,
    owner  => $user,
  }

  exec { "celery-beat-restart":
    user        => $user,
    cwd         => $path,
    path        => ["/bin", "/usr/bin"],
    onlyif      => "test -f $celery_beat_pid",
    command     => "kill -HUP $(cat $celery_beat_pid)",
    refreshonly => true,
    require     => [
      Exec["migrate"],
      Exec["collectstatic"],
    ],
  }

  exec { "celery-worker-restart":
    user        => $user,
    cwd         => $path,
    path        => ["/bin", "/usr/bin"],
    onlyif      => "test -f $celery_worker_pid",
    command     => "kill -HUP $(cat $celery_worker_pid)",
    refreshonly => true,
    require     => [
      Exec["migrate"],
      Exec["collectstatic"],
    ],
  }
}
