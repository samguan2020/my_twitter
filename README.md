copy/clone twitter-term-1
git checkout master
make sure vagrantfile.temp -> vagrantfile
vagrant up
vagrant provision
vagrant ssh
cd /vagrant
install redis using "30_33. 使用 Redis 对 Tweets, NewsFeed 进行缓存 (1).pptx"
install hbase using "40_Python 连接 HBase.pdf", http://http://192.168.33.10:16010/ to see hbase
install thrift usuing /home/vagrant/download, sudo make install
python manage.py migrates and python manage.py makemigrations
python manage.py test
python manage.py runserver 0.0.0.0:8000 and http://localhost
python manage.py createsuperuser
