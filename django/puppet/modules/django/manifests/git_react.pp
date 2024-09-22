class django::git_react (
  $user           = $django::conf::user,
  $path           = $django::conf::react_path,
  $git_react_name = $django::conf::git_react_name,
  $git_host       = "bitbucket.org",
  $git_url        = "git@$git_host:$git_react_name",
  $git_branch     = $django::conf::git_react_branch,
) {
  vcsrepo { $path:
    ensure   => latest,
    provider => git,
    source   => $git_url,
    user     => $user,
    revision => $git_branch,
  }
}
