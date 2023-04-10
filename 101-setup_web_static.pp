# Redoing the setup of the server using puppet


# nginx configuration to be used

$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://youtube.com/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"
package { 'nginx':
  ensure => 'installed',
}


file { '/etc/nginx/sites-available/default':
  ensure => 'file',
  content => $nginx_conf,
  require => Package['nginx'],
}

file { '/data':
  ensure => 'directory'
}

file { '/data/web_static':
  ensure => 'directory',
}

file { '/data/web_static/releases':
  ensure => 'directory',
  require => File['/data/web_static'],
}

file { '/data/web_static/shared':
  ensure => 'directory',
  require => File['/data/web_static'],
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
  require => [
    File['/data/web_static/releases'],
    File['/data/web_static/shared'],
  ],
}

file { '/data/web_static/releases/test/index.html':
  ensure => 'file',
  content => '<html><body>Hello, World!</body></html>',
  require => File['/data/web_static/releases/test'],
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  require => File['/data/web_static'],
}

service { 'nginx':
  ensure => 'running',
  enable => true,
  require => [
    Package['nginx'],
    File['/etc/nginx/sites-available/default'],
    File['/data/web_static/current'],
  ],
}
