# Install nginx with puppet

exec {'install':
	provider  => shell,
	command   => 'sudo apt-get -y update; sudo apt-get -y install nginx;
	echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html;
	sudo sed -i "s/server_name _;/server_name _;\n\t
	rewrite ^\/redirect_me rewrite ^ https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;/"
	 /etc/nginx/sites-available/default; sudo service nginx start',

}
