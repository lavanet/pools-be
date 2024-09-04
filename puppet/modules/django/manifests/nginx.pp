class django::nginx (
  $project   = $django::conf::project,
  $certbot   = $django::conf::certbot,
  $path      = $django::conf::path,
  $site_path = "$django::conf::home/nginx",
  $site_conf = "$django::conf::project.conf",
  $template  = "django/nginx_site.$django::conf::nginx_template.erb",
) {
  package { "nginx": }

  service { "nginx":
    ensure  => running,
    enable  => true,
    require => Package["nginx"],
  }

  exec { "nginx-remove-default":
    onlyif  => "test -f /etc/nginx/sites-enabled/default",
    command => "rm default",
    cwd     => "/etc/nginx/sites-enabled",
    path    => ["/bin", "/usr/bin"],
  }

  exec { "nginx-reload":
    command     => "nginx -s reload",
    cwd         => "/etc/nginx/",
    path        => ["/bin", "/usr/bin", "/usr/sbin/"],
    refreshonly => true,
  }

  if $certbot { $certbot_ensure = present }
  else { $certbot_ensure = absent }

  file { $site_path:
    ensure  => directory,
    group   => "root",
    owner   => "root",
    require => Package["nginx"],
  } ->

  file { "$site_path/common.conf":
    ensure  => file,
    group   => "root",
    owner   => "root",
    mode    => "644",
    content => template("django/nginx_common.erb"),
    notify  => Exec["nginx-reload"],
  } ->

  file { "$site_path/common-ssl.conf":
    ensure  => file,
    group   => "root",
    owner   => "root",
    mode    => "644",
    content => template("django/nginx_common_ssl.erb"),
    notify  => Exec["nginx-reload"],
  } ->

  file { "$site_path/localhost.crt":
    ensure  => file,
    group   => "root",
    owner   => "root",
    mode    => "644",
    source => "puppet:///modules/django/nginx/localhost.crt",
    notify  => Exec["nginx-reload"],
  } ->

  file { "$site_path/localhost.key":
    ensure  => file,
    group   => "root",
    owner   => "root",
    mode    => "600",
    source => "puppet:///modules/django/nginx/localhost.key",
    notify  => Exec["nginx-reload"],
  } ->

  file { "$site_path/$site_conf":
    ensure  => file,
    group   => "root",
    owner   => "root",
    mode    => "644",
    content => template($template),
    notify  => Exec["nginx-reload"],
  } ->

  file { "/etc/nginx/sites-enabled/$site_conf":
    ensure  => "link",
    group   => "root",
    owner   => "root",
    target  => "$site_path/$site_conf",
    notify  => Exec["nginx-reload"],
    require => Exec["nginx-remove-default"],
  } ->

  cron { "certbot-renew":
    ensure  => $certbot_ensure,
    command => 'certbot renew --noninteractive --post-hook "nginx -s reload"',
    user    => "root",
    minute  => "0",
    hour    => "0",
    weekday => "1",
  }

  file { "/etc/logrotate.d/nginx-$project":
    ensure  => file,
    group   => "root",
    owner   => "root",
    mode    => "644",
    content => template("django/nginx_logrotate.erb"),
    require => Package["nginx"],
  }
}


class django::nginx::basicauth (
  $site_path = "$django::conf::home/nginx",
) {
  file { "$site_path/htpasswd":
    ensure => file,
    group  => "root",
    owner  => "root",
    mode   => "644",
    source => "puppet:///modules/django/nginx/htpasswd",
    notify => Exec["nginx-reload"],
  }
}
