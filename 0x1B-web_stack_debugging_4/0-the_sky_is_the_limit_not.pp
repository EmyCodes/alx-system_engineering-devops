# Adjust the web stack to increase the limit to 2048
file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT='-n 2048'\n",
}
