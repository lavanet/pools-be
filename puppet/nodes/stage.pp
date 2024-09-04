node /^stage\./ {
  class { "django::conf":
    user               => "lavapool",
    nginx_template     => "stage",
    ssh_template       => "stage",
    local_settings     => "stage",
    postgresql_db_pass => "1PXvaf2nWPWgmECqDw33_6WEWgMmoW9HGCnGjYuId7WAu9-VGotl5sr9IG9qxg9roQKQfn7ZUf7Nqn6hWT26CA",
    git_name           => "snickk/project-starter-test.git",
    git_branch         => "stage-pipeline",
    certbot            => false,
  } ->
  class { "django::core::stack": } ->
  class { "django::nginx::basicauth": }
}
