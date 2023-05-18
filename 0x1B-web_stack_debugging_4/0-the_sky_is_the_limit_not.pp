# A puppet manifest to change user limit
exec { 'change_value_to_50':
  command => "/bin/sed -i 's/5/50/g' /etc/security/limits.conf",
}

exec { 'change_value_to_40':
  command => "/bin/sed -i 's/4/40/g' /etc/security/limits.conf",
}
