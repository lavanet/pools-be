class deploy::autodeploy (
  $enabled = $django::conf::autodeploy,
  $puppet_sh = $django::conf::puppet_sh,
) {

  cron { 'autodeploy':
    command => "cd $puppet_sh && ./apply.py",
    user    => 'root',
    minute  => "*/5",
    ensure  => $enabled ? {
      true    => present,
      default => absent,
    },
  }
}
