class django::core {
  class { "django::system": } ->
  class { "django::utils": } ->
  class { "django::user": } ->
  class { "django::filesystem": } ->
  class { "django::postgresql": } ->
  class { "django::python": } ->
  class { "django::nginx": }

  if $django::conf::swap {
    class { "django::swapfile": }
  }
}

class django::core::stack {
  if $django::conf::deploy {
    class { "deploy": } ->
    class { "deploy::autodeploy": }
  }

  class { "django::core": } ->
  class { "django::git":
    notify => [
      Exec["venv-requirements"],
      Exec["migrate"],
      Exec["collectstatic"],
      Exec["uwsgi-restart"],
      Exec["celery-beat-restart"],
      Exec["celery-worker-restart"],
      Exec["clear-cache"],
    ], } ->
  class { "django::uwsgi": } ->
  class { "django::supervisor": } ->
  class { "django::cache": }

  if $django::conf::git_react_name {
    class { "django::git_react":
      require => Class["django::git"],
    }
  }
}
