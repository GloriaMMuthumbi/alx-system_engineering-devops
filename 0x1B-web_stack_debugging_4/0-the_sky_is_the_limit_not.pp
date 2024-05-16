#increases amount of traffic handled by Nginx server

#increases the ULIMIT of default file
exec {'fix--for-ngix':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}


#restarts Nginx


exec { 'nginx-restart':
  command => 'nginx restart',
  path    =>'/etc/init.d/'
}
