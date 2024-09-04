class django::cache (
  $user = $django::conf::user,
  $path = $django::conf::path,
  $venv = $django::conf::venv,
) {
  exec { "clear-cache":
    user        => $user,
    cwd         => $path,
    path        => ["$venv/bin"],
    command     => "python manage.py clear_cache",
    refreshonly => true,
    require     => [
      Exec["uwsgi-restart"],
      Exec["celery-beat-restart"],
      Exec["celery-worker-restart"],
    ],
  }
}
