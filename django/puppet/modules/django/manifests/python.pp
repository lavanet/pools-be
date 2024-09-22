class django::python (
  $user = $django::conf::user,
  $home = $django::conf::home,
  $path = $django::conf::path,
  $venv = $django::conf::venv,
) {
  package { "python3": } ->
  package { "python3-dev": } ->
  package { "python3-pip": } ->
  package { "python3-venv": } ->
  package { "python3-cffi": } ->

  exec { $venv:
    user    => $user,
    cwd     => $home,
    path    => "/usr/bin",
    command => "python3 -m venv $venv",
    unless  => "test -d $venv",
    notify  => Exec["venv-requirements"],
  } ->

  exec { "venv-requirements":
    user        => $user,
    cwd         => $path,
    path        => ["$venv/bin", "/usr/bin"],
    command     => "pip install -r requirements.txt",
    onlyif      => "test -f requirements.txt",
    refreshonly => true,
  } ->

  exec { "migrate":
    user        => $user,
    cwd         => $path,
    path        => ["$venv/bin"],
    command     => "python manage.py migrate --noinput",
    refreshonly => true,
  } ->

  exec { "collectstatic":
    user        => $user,
    cwd         => $path,
    path        => ["$venv/bin"],
    command     => "python manage.py collectstatic --link --noinput",
    refreshonly => true,
  } ->

  class { "django::celery": }
}
