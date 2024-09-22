node /^prod\./ {
  class { "django::conf":
    user               => "lavapool",
    postgresql_db_pass => "1PXvaf2nWPWgmECqDw33_6WEWgMmoW9HGCnGjYuId7WAu9-VGotl5sr9IG9qxg9roQKQfn7ZUf7Nqn6hWT26CA",
    git_name           => "snickk/project-starter-test.git",
    git_branch         => "prod-pipeline",
    autodeploy         => true,
    certbot            => false,
  } ->
  class { "django::core::stack": }
}
