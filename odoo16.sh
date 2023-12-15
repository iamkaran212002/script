################################################################################################################################
################################################################################################################################
$echo"\n                                                                                                                       \n"
$echo"\n------               ####      ####         @@@@@@@@@          *****             *****       &&&&&&&&&&&&&&&&    ------\n"
$echo"\n------               ####     ####         @@@@@@@@@@@          *****           *****        &&&&        &&&&    ------\n"
$echo"\n------               ####    ####         @@@       @@@          *****         *****         &&&&        &&&&    ------\n"
$echo"\n------               ###########         @@@         @@@          *****       *****          &&&&&&&&&&&&&&&&    ------\n"
$echo"\n------               ####    ####       @@@@@@@@@@@@@@@@@          *****     *****           &&&&                ------\n"
$echo"\n------               ####     ####      @@@           @@@           *************            &&&&                ------\n"
$echo"\n------               ####      ####     @@@           @@@            ***********             &&&&                ------\n"

odoo="/etc/odoo.conf"
odooservice="/etc/systemd/system/odoo16.service"

odoo_conf="[options]
admin_passwd = YOUR_PASSWORD
db_host = False
db_port = False
db_user = odoo16
db_password = False
addons_path = /opt/odoo16/odoo16/addons,/opt/odoo16/odoo16/custom-addons
xmlrpc_port = 8069"
 
odoo_service="[Unit]
Description=Odoo16
Requires=postgresql.service
After=network.target postgresql.service
[Service]
Type=simple
SyslogIdentifier=odoo16
PermissionsStartOnly=true
User=odoo16
Group=odoo16
ExecStart=/opt/odoo16/odoo16-venv/bin/python3 /opt/odoo16/odoo16/odoo-bin -c /etc/odoo16.conf
StandardOutput=journal+console
[Install]
WantedBy=multi-user.target"

sudo touch /etc/odoo.conf
sudo touch /etc/systemd/system/odoo16.service

if sudo apt update ;then
    echo "\n----updated SuccessFully---\n"
else
    echo "\n---update Failed----\n"
fi
if sudo apt upgrade -y ;then
    echo "\n ---- upgrade Successfully ----\n"
else
    echo "\n ---- upgrade failed ----\n"
fi
if sudo useradd -m -d /opt/odoo16 -U -r -s /bin/bash odoo16 ;then
    echo "\n ----user added successfully ----\n"
else
    echo "\n ---- user added ----\n"
fi
if sudo apt install build-essential wget git python3-pip python3-dev python3-venv python3-wheel libfreetype6-dev libxml2-dev libzip-dev libsasl2-dev python3-setuptools libjpeg-dev zlib1g-dev libpq-dev libxslt1-dev libldap2-dev libtiff5-dev libopenjp2-7-dev ;then
    echo "\n ----Python package installed successfully ----\n" 
else
    echo "\n ----Python package installation failed ---\n"
fi
if sudo apt install postgresql ;then
    echo "\n ----installed postgresql Successfully----\n"
else
    echo "\n ----postgresql failed ----\n"
fi
if sudo su - postgres -c "createuser -s odoo16" ;then
    echo "\n ----user created successfully ----\n"
else
    echo "\n ----user creation failed ----\n"
fi
if sudo apt install wkhtmltopdf ;then
    echo "\n ----wkhtmlopdf installed successfully ----\n"
else
    echo "\n -----installation failed ----\n"
fi
if sudo -chown -R odoo16 /opt/odoo16 ;then
  echo "\n
sudo su - odoo16 <<EOF
fi
if git clone https://github.com/odoo/odoo.git --depth 1 --branch 16.0 odoo16 ;then
    echo "\n ---- cloned successfully ---- \n"
else
    echo "\n ---- cloned failed ---- \n"
if python3 -m venv odoo16-venv ;then
    echo "\n ---- python3 completed ----\n"
else
    echo "\n ---- python3 failed ----\n"
fi
if source odoo16-venv/bin/activate ;then
    echo "\n ---- Activated successfully ---- \n"
else
    echo "\n ---- activation failed ---- \n"
fi
if pip3 install wheel ;then
    echo "\n ----Installed wheel ----\n"
else 
    echo "\n ----Installation wheel failed ----\n"
fi
if pip3 install -r odoo16/requirements.txt ;then
    echo "\n ---- Requirements.txt installed ----\n"
else
    echo "\n ---- Requirements.txt failed ----\n"
fi
if deactivate ;then
    echo "\n ---- Deactivated successfully ----\n"
else
    echo "\n ---- Deactivated failed ---- \n"
fi
if sudo mkdir /opt/odoo16/odoo16/custom-addons ;then
    echo "\n ---- Directory created Successfully ---- \n"
else
    echo "\n ---- Directory creation failed ---- \n"
if exit ;then
    echo "\n ---- exit successfully ---- \n"
else
    echo "\n ---- exit failed ---- \n"
fi
EOF
if echo "$odoo_conf" | sudo tee "$odoo" > /dev/null ;then
        echo "\n ---- conf file created successfully ----\n" 
else
        echo "\n ---- conf file created failed ----\n"
fi

if echo "$odoo_service" | sudo tee "$odooservice" > /dev/null ;then
        echo "\n ---- service file created successfully ----\n"
else
        echo "\n ---- service file created failed ---- \n"
fi
sudo systemctl deamon-reload
sudo systemctl start odoo16
sudo systemctl status odoo16