

## Setup

* setup your virtualenv.
* pip install -r requirements.txt
* start elasticsearch
* open your python shell `$ python`

    # To index the example links
    $ import main
    $ context = main.app.test_request_context('/', method='POST')
	$ context.push()
    $ main.index()
    
## Testerver setup

* No deployment script available
* flask server started in a tmux session (tmux attach)

	IP: 10.2.22.52
	user: elastic
	pass (für sudo): search
	PasswordAuthentication no (für ssh)

elastic ist in der Gruppe adm und sudo.

### Elasticsearch

	wget -O - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add -
	echo "deb https://packages.elastic.co/elasticsearch/2.x/debian stable main" | sudo tee -a /etc/apt/sources.list.d/elasticsearch-2.x.list
	sudo apt-get update && sudo apt-get install elasticsearch default-jdk
	
	sudo /bin/systemctl daemon-reload
	sudo /bin/systemctl enable elasticsearch.service
		
	sed -i 's/^#ES_HEAP_SIZE=2g/ES_HEAP_SIZE=2g/' /etc/default/elasticsearch
	
### Search app

	ssh-keygen -b 4096
	cat /root/.ssh/id_rsa.pub
	
Add /root/.ssh/id_rsa.pub as Gitlab deploy key
	
	mkdir -p /opt/linkbuilder_search/
	git clone git@code.feld-m.de:lilli.weiss/linkbuilder_search_prototype.git /opt/linkbuilder_search/appserver/
	 
	apt-get install python3 python3-virtualenv virtualenv
	virtualenv /opt/linkbuilder_search/virtualenv/ -p /usr/bin/python3
	cd /opt/linkbuilder_search/appserver/
	source ../virtualenv/bin/activate
	pip install -r requirements.txt


## Testserver stuff

### How to connect (connect via cabel or VPN)

Login via remote shell

	ssh -l elastic 10.2.22.52
	 
Become root user

	sudo su -

Start tmux session
 
	tmux attach
	
Press strg + "b" - followed by "n" to switch windows

Update project via git

	git pull
	
Check git "status" / Press "q" to close

	git log
	
Server starten
	

	cd /opt/linkbuilder_search/appserver/
	source ../virtualenv/bin/activate
	
	python main.py