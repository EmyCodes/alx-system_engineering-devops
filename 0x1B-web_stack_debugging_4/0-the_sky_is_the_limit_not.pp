file { '/etc/default/nginx':
  ensure => file,
  content => "ULIMIT='-n 4000'\n",
}
