###########################################################################################
##                                                                                       ##
##                       - Auteur : SMAINI Smail -                                       ##
##                                                                                       ##
##                   - Email  : smaini.smail@gmail.com -                                 ##
##                                                                                       ##
##               - Github     : https://github.com/SMAINI-Smail -                        ##
##                                                                                       ##
##        - Projet 6    : Participez à la vie de la communauté Open Source -             ##
##                                                                                       ##
###########################################################################################


import subprocess
import os
from pathlib import Path
from os import chdir as cd
list_fichier_usr_bin = os.listdir('/usr/bin')
list_fichier_usr_sbin = os.listdir('/usr/sbin')


list_fichier = os.listdir('/var/log/')
if "install_environement_wordpress_app.log"in list_fichier : 
    Path('./install_environement_wordpress_app.log').touch()  
else :
    Path('./install_environement_wordpress_app.log').touch()

### Ouverture du fichier install_environement_wordpress_app.log
fichier = open("./install_environement_wordpress_app.log", "w")

### Mise a jour du systeme d'exploitation 
print("Mise a jour du systeme d'exploitation \n \n  ")
fichier.write("Mise a jour du systeme d'exploitation  \n \n  ")
update_system= subprocess.Popen(["apt", "update"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

update_system.stdin.write(update_system.stdout.encoding)
update_system.stdin.close()
for line in update_system.stdout.read():     
    fichier.write(line)

update_system_2= subprocess.Popen(["apt", "full-upgrade", "-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
update_system_2.stdin.write(update_system_2.stdout.encoding)
update_system_2.stdin.close()
for line in update_system_2.stdout.read():       
    fichier.write(line)
fichier.write("fin de la mise à jour du systeme \n \n  ")

print("fin de la mise à jour du systeme \n \n  ")


### Installation et configuration du serveur apache 2
fichier.write("Installation et configuration du serveur apache 2 \n \n  ")
print("Installation et configuration du serveur apache 2 \n \n  ")

# Vérifier si Apache2 existe
if "apache2"in list_fichier_usr_sbin :

    # desinstallation d'Apache2
    print("Le serveur web apache2 est dèja installé\n \n  ")
    fichier.write("Le serveur web apache2 est dèja installé\n \n  ")
    print("desinstallation du serveur apache2 ...\n \n  ")
    fichier.write("desinstallation du serveur apache2 ...\n \n  ")
    fichier.write("desinstaller apache2 \n \n  ")
    remove_apache= subprocess.Popen(["apt-get", "autoremove", "--purge", "apache2"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    remove_apache.stdin.write(remove_apache.stdout.encoding)
    remove_apache.stdin.close()
    for line in remove_apache.stdout.read():       
        fichier.write(line)
    print("Fin de desinstallation du serveur apache2 \n \n  ")

## Installation d'Apache2
print("Debut d'installation du serveur apache2 \n \n  ")
message_apache= "Installation du serveur web appache en cours \n \n  "
fichier.write(message_apache)
install_apache= subprocess.Popen(["apt", "install", "apache2", "-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
install_apache.stdin.write(install_apache.stdout.encoding)
install_apache.stdin.close()
for line in install_apache.stdout.read():       
    fichier.write(line)
fichier.write("fin d'installation du serveur \n \n  ")
print("Fin d'installation du serveur apache2 \n \n  ")

## lancement du serveur apache 2
print("lancement  du serveur apache 2 au démarrage du system \n \n  ")
fichier.write("lancement  du serveur apache 2 au démarrage du system \n \n  ")
lance_apache= subprocess.Popen(["systemctl", "enable", "apache2"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
lance_apache.stdin.write(lance_apache.stdout.encoding)
lance_apache.stdin.close()
for line in lance_apache.stdout.read():          
    fichier.write(line)

## Activation des modules:  headers,deflate,rewrite, SSL
fichier.write("Activation des modules: headers, deflate, rewrite, SSL \n\n\n \n  ")
fichier.write("Activation de headers  \n \n  ")
print("activation de headers \n \n  ")
active_headers= subprocess.Popen(["a2enmod", "headers"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
active_headers.stdin.write(active_headers.stdout.encoding)
active_headers.stdin.close()
for line in active_headers.stdout.read(): 
    fichier.write(line)

fichier.write("Activation de rewrite  \n \n  ")
print("activation de rewrite \n \n  ")
active_rewrite= subprocess.Popen(["a2enmod", "rewrite"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
active_rewrite.stdin.write(active_rewrite.stdout.encoding)
active_rewrite.stdin.close()
for line in active_rewrite.stdout.read():   
    fichier.write(line)

fichier.write("Activation de deflate  \n \n  ")
print("activation de deflate \n \n  ")
active_deflate= subprocess.Popen(["a2enmod", "deflate"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
active_deflate.stdin.write(active_deflate.stdout.encoding)
active_deflate.stdin.close()
for line in active_deflate.stdout.read():   
    fichier.write(line)
fichier.write("Activation de SSL  \n \n  ")
print("activation de ssl")
active_SSL= subprocess.Popen(["a2enmod", "SSL"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
active_SSL.stdin.write(active_SSL.stdout.encoding)
active_SSL.stdin.close()
for line in active_SSL.stdout.read():   
   fichier.write(line)

## Configuration du fichier apache2.conf pour  cacher la version du serveur apache2 sur le navigateur 
fichier.write("configurer le fichier apache2.conf \n \n  ")
print("configurer le fichier apache2.conf \n \n  ")
droit_apache= subprocess.Popen(["chmod", "+w ", "/etc/apache2/apache2.conf"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
droit_apache.stdin.write(droit_apache.stdout.encoding)
droit_apache.stdin.close()
for line in droit_apache.stdout.read(): 
    fichier.write(line)
apache_conf = open("/etc/apache2/apache2.conf", "a")
apache_conf.write("\n \n  ServerTokens Prod")
apache_conf.close()

## redemarrer le serveur apache 2
print("redemarrer le serveur  apache2 \n \n  ")
fichier.write("Redemarrage du serveur apache 2  \n \n  ")
reboot_apache= subprocess.Popen([  "systemctl", "restart", "apache2"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
reboot_apache.stdin.write(reboot_apache.stdout.encoding)
reboot_apache.stdin.close()
for line in reboot_apache.stdout.read():   
    fichier.write(line)

## supprimer le fichier /var/www/html/index.html 
fichier.write("supprimer le fichier /var/www/html/index.html  \n \n  ")
print("supprimer le fichier /var/www/html/index.html \n \n   ")
delete_index= subprocess.Popen([  "rm","-f""/var/www/html/index.html"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
delete_index.stdin.write(delete_index.stdout.encoding)
delete_index.stdin.close()
for line in delete_index.stdout.read(): 
    fichier.write(line)

## creation du dossier /var/www/html/wordpress/ 
fichier.write("creation du dossier /var/www/html/wordpress/ \n \n  ")
print("creation du dossier /var/www/html/wordpress/  \n \n  ")
cree_dossier= subprocess.Popen([  "mkdir", "/var/www/html/wordpress/"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
cree_dossier.stdin.write(cree_dossier.stdout.encoding)
cree_dossier.stdin.close()
for line in cree_dossier.stdout.read():   
    fichier.write(line)

## Configuration du fichier /etc/apache2/sites-enabled/000-default.conf   
fichier.write("configuration du fichier /etc/apache2/sites-enabled/000-default.conf  \n \n  ")
print("configuration du fichier /etc/apache2/sites-enabled/000-default.conf \n \n  ")

delete_index= subprocess.Popen([  "rm","-f""/etc/apache2/sites-enabled/000-default.conf"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
delete_index.stdin.write(delete_index.stdout.encoding)
delete_index.stdin.close()
for line in delete_index.stdout.read(): 
    fichier.write(line)

Path('/etc/apache2/sites-enabled/000-default.conf').touch()

# ouvrir le fichier /etc/apache2/sites-enabled/000-default.conf
apache_config = open("/etc/apache2/sites-enabled/000-default.conf", "w")
apache_config.write("<VirtualHost *:80> \n\n \n  ")
apache_config.write("ServerAdmin webmaster@localhost   \n \n  ")
apache_config.write("DocumentRoot /var/www/html/wordpress/ \n\n \n  ")
apache_config.write("ErrorLog ${APACHE_LOG_DIR}/error.log \n \n  ")
apache_config.write("CustomLog ${APACHE_LOG_DIR}/access.log combined\n\n \n  ")
apache_config.write(" </VirtualHost> \n \n  ")
apache_config.close()

fichier.write("Fin de l'installation et de la configuration du serveur apache 2 \n \n  ")
print("Fin de l'installation et de la configuration du serveur apache 2 - ")


fichier.write("Installation et configuration PHP \n \n  ")
print("Installation et configuration PHP \n \n  ")

# Vérifier si PHP existe
if "php"in list_fichier_usr_bin  :
    ## desinsatller php
    fichier.write( "  Le programme PHP est dèja installé sur le serveur  \n \n  ")
    print( "  Le programme PHP est dèja installé sur le serveur  \n \n  ")
    fichier.write("desinstaller php \n \n  ")
    print("desinstaller php \n \n  ")
    purge_php= subprocess.Popen(["apt-get","remove", "--purge", "php7.*", "php8.*","-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    purge_php.stdin.write(purge_php.stdout.encoding) 
    purge_php.stdin.close()
    for line in purge_php.stdout.read():       
        fichier.write(line)
    auto_remove= subprocess.Popen(["apt-get", "autoremove","-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    auto_remove.stdin.write(auto_remove.stdout.encoding)
    auto_remove.stdin.close()
    for line in auto_remove.stdout.read():       
        fichier.write(line) 
    update_sys= subprocess.Popen(["apt-get", "update","-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    update_sys.stdin.write(update_sys.stdout.encoding)
    update_sys.stdin.close()
    for line in update_sys.stdout.read():       
        fichier.write(line) 
    print("Fin de desinstallation de php")

## installer php 
fichier.write("Debut d'installation de php  \n \n   ")
print("Debut d'installation de php \n \n    ")
# installation des dependances 
fichier.write("Installation des dépendances \n \n   ")
print("Installation des dépendances \n \n   ")
install_dependance= subprocess.Popen(["apt-get", "install", "ca-certificates", "apt-transport-https", "software-properties-common", "wget", "curl", "lsb-release", "-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
install_dependance.stdin.write(install_dependance.stdout.encoding)
install_dependance.stdin.close()
for line in install_dependance.stdout.read(): 
    fichier.write(line)

# install php8.1
fichier.write("Installation de php8.1 \n \n    ")
print("Installation de php8.1 \n \n    ")
install_php= subprocess.Popen(["apt", "install", "php8.1","php8.1-mysql","-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
install_php.stdin.write(install_php.stdout.encoding)
install_php.stdin.close()
for line in install_php.stdout.read(): 
    fichier.write(line)
fichier.write("Installation de libapache2-mod-php8.1 \n \n  ")
print("Installation de libapache2-mod-php8.1 \n \n  ")
install_libapache2= subprocess.Popen([  "apt", "install", "libapache2-mod-php8.1", "-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
install_libapache2.stdin.write(install_libapache2.stdout.encoding)
install_libapache2.stdin.close()
for line in install_libapache2.stdout.read(): 
    fichier.write(line)

restart_apache= subprocess.Popen(["systemctl", "restart","apache2"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
restart_apache.stdin.write(restart_apache.stdout.encoding)
restart_apache.stdin.close()
for line in restart_apache.stdout.read():       
    fichier.write(line) 


## installer les dependance de php dont a besoin l'application                                               
install_php_2= subprocess.Popen(["apt", "install","php8.1-common","php8.1-curl","php8.1-bcmath","php8.1-intl","php8.1-mbstring","php8.1-xmlrpc","php8.1-gd","php8.1-xml","php8.1-cli","php8.1-zip","-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
install_php_2.stdin.write(install_php_2.stdout.encoding)
install_php_2.stdin.close()
for line in install_php_2.stdout.read(): 
    fichier.write(line)

install_performance= subprocess.Popen(["apt", "install", "php8.1-fpm", "libapache2-mod-fcgid","-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
install_performance.stdin.write(install_performance.stdout.encoding)
install_performance.stdin.close()
for line in install_performance.stdout.read(): 
    fichier.write(line)
proxy= subprocess.Popen(["a2enmod", "proxy_fcgi","setenvif"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
proxy.stdin.write(proxy.stdout.encoding)
proxy.stdin.close()
for line in proxy.stdout.read():       
    fichier.write(line) 
fpm= subprocess.Popen(["a2enmod", "php8.1-fpm "] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
fpm.stdin.write(fpm.stdout.encoding)
fpm.stdin.close()
for line in fpm.stdout.read():       
    fichier.write(line) 
restart_apache= subprocess.Popen(["systemctl", "restart","apache2"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
restart_apache.stdin.write(restart_apache.stdout.encoding)
restart_apache.stdin.close()
for line in fpm.stdout.read():       
    fichier.write(line) 

fichier.write("Fin de l'installation et de la configuration PHP \n \n  ")
print("Fin de l'installation et de la configuration PHP \n \n  ")




fichier.write("Installation et configuration du serveur mariadb \n \n  ")
print("Installation et configuration du serveur mariadb \n \n  ")

if "mariadb"in list_fichier_usr_bin  :
    #Desinstallation de mariadb 
    print("Le serveur MariaDB est dèja installé sur le serveur, on procede a sa desinstallation \n \n  ")
    fichier.write("Le serveur MariaDB est dèja installé sur le serveur, on procede a sa desinstallation\n \n  ")
    stop_maria= subprocess.Popen(["systemctl", "stop", "mysql"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stop_maria.stdin.write(stop_maria.stdout.encoding)
    stop_maria.stdin.close()
    for line in stop_maria.stdout.read():     
        fichier.write(line)
    remove_maria= subprocess.Popen(["apt-get", "--purge","remove", "mariadb-server","-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    remove_maria.stdin.write(remove_maria.stdout.encoding)
    remove_maria.stdin.close()
    for line in remove_maria.stdout.read():       
        fichier.write(line)
    remove_mysql_common= subprocess.Popen(["apt-get", "--purge","remove", "mysql-common","-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    remove_mysql_common.stdin.write(remove_mysql_common.stdout.encoding)
    remove_mysql_common.stdin.close()
    for line in remove_mysql_common.stdout.read():       
        fichier.write(line)
    auto_remove= subprocess.Popen(["apt-get", "autoremove","-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    auto_remove.stdin.write(auto_remove.stdout.encoding)
    auto_remove.stdin.close()
    for line in auto_remove.stdout.read():       
        fichier.write(line) 

    print("Fin de desinstallation de  mariadb")

## installation de mariadb-serveur    
fichier.write("Début de l'installation de MariaDB \n \n  ")
print("Installation de MariaDB en cours ... \n \n  ")
install_maria= subprocess.Popen([  "apt", "install", "mariadb-server","-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
install_maria.stdin.write(install_maria.stdout.encoding)
install_maria.stdin.close()
for line in install_maria.stdout.read():   
    fichier.write(line)
fichier.write("Fin de l'installation de MariaDB \n \n  ")
print("Fin de l'installation de MariaDB \n \n  ")

## Autoriser mariadb a démarrer avec le boot du système
fichier.write("lancement  de MariaDb au démarrage du system \n \n  ")
print(" lancement  de MariaDb au démarrage du systeme \n \n  ")
lance_maria= subprocess.Popen(["systemctl", "enable", "mariadb"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
lance_maria.stdin.write(lance_maria.stdout.encoding)
lance_maria.stdin.close()
for line in lance_maria.stdout.read():     
    fichier.write(line)
    
## reboot du maria
fichier.write("redemarré le serveur MariaDB  \n \n  ")
print("redemarré le serveur MariaDB \n \n  ")
reboot_maria= subprocess.Popen(["systemctl", "restart", "mariadb"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
reboot_maria.stdin.write(reboot_maria.stdout.encoding)
reboot_maria.stdin.close()
for line in reboot_maria.stdout.read():
    fichier.write(line)
    
## Securisé l'instance de mariaDB 
fichier.write("creer un nouveau USER   \n \n  ")
print("creer un nouveau USER \n \n  ")
new_user= subprocess.Popen(["mariadb", "-e", "CREATE USER 'admin_wp'@'localhost' IDENTIFIED BY 'passwd_wp';"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
new_user.stdin.write(new_user.stdout.encoding)
new_user.stdin.close()
for line in new_user.stdout.read():
    fichier.write(line)

## Creation d'une base de donnée
fichier.write("creer une nouvelle base de donnée  \n \n  ")
print("creer une nouvelle base de donnée \n \n  ")
new_database= subprocess.Popen(["mariadb", "-e", "CREATE DATABASE database_wp;"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
new_database.stdin.write(new_database.stdout.encoding)
new_database.stdin.close()
for line in new_database.stdout.read():
    fichier.write(line)

## Ajouter les privileges
fichier.write("ajouter les privileges pour le nouveau utilisateur sur la nouvelle base de donnée  \n \n  ")
print("ajouter les privileges pour le nouveau utilisateur sur la nouvelle base de donnée  \n \n  ")
privileges= subprocess.Popen(["mariadb", "-e", "GRANT ALL PRIVILEGES ON database_wp.* TO 'admin_wp'@'localhost' ;"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
privileges.stdin.write(privileges.stdout.encoding)
privileges.stdin.close()
for line in new_user.stdout.read():
    fichier.write(line)

fichier.write("FLUSH PRIVILEGES  \n \n  ")
flush_privileges= subprocess.Popen(["mariadb", "-e", "FLUSH PRIVILEGES;"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
flush_privileges.stdin.write(flush_privileges.stdout.encoding)
flush_privileges.stdin.close()
for line in new_user.stdout.read():
    fichier.write(line)

fichier.write("Fin de l'installation et de la configuration du serveur mariadb \n \n  ")
print("Fin de l'installation et de la configuration du serveur mariadb \n \n  ")




fichier.write("Installation et configuration de Wordpress \n \n  ")
print("Installation et configuration de Wordpress \n \n  ")

##  installation de wp cli

fichier.write("ajouter le repository tiagohillebrandt/wp-cli  \n \n  ")
print("ajouter le repository tiagohillebrandt/wp-cli \n \n  ")


add_repo= subprocess.Popen(["add-apt-repository","--yes", "ppa:tiagohillebrandt/wp-cli"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
add_repo.stdin.write(add_repo.stdout.encoding)
add_repo.stdin.close()
for line in add_repo.stdout.read():       
    fichier.write(line) 

fichier.write("mettre a jours le systeme  \n \n  ")
print("mettre a jours le systeme  ")
update= subprocess.Popen(["apt-get","update", "-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
update.stdin.write(update.stdout.encoding)
update.stdin.close()
for line in update.stdout.read(): 
    fichier.write(line)

fichier.write("installer wp-cli  \n \n  ")
print("installer wp-cli \n \n  ")
install_wp= subprocess.Popen(["apt-get","install", "wp-cli"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
install_wp.stdin.write(install_wp.stdout.encoding)
install_wp.stdin.close()
for line in install_wp.stdout.read(): 
    fichier.write(line)

## acceder au dossier /var/www/html/wordpress/
cd('/var/www/html/wordpress/')
fichier.write("telecharger wordpress  \n \n  ")
print("telecharger wordpress  ")
download_wp= subprocess.Popen(["wp","--allow-root", "core", "download"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
download_wp.stdin.write(download_wp.stdout.encoding)
download_wp.stdin.close()
for line in download_wp.stdout.read(): 
    fichier.write(line)

## donner les droits pour le fichier /var/www/html/wordpress/
fichier.write("donner les droits pour le fichier /var/www/html/wordpress/  \n \n  ")
print("donner les droits pour le fichier /var/www/html/wordpress/ \n \n   ")
droit_html= subprocess.Popen(["chown", "-R", "www-data:www-data", "/var/www/html/wordpress/"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
droit_html.stdin.write(droit_html.stdout.encoding)
droit_html.stdin.close()
for line in droit_html.stdout.read(): 
    fichier.write(line)

## generation du fichier /var/www/html/wordpress/wp-config.php (ou se trouve toute les configurations necessaire pour une application wordpress)
fichier.write("generation du fichier /var/www/html/wordpress/wp-config.php \n \n  ")
print("generation du fichier /var/www/html/wordpress/wp-config.php \n \n  ")
generate_config_php= subprocess.Popen(["wp","--allow-root", "config", "create", "--dbname=database_wp","--dbuser=admin_wp", "--dbpass=passwd_wp", "--dbhost=localhost", "--dbprefix=projet6_"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
generate_config_php.stdin.write(generate_config_php.stdout.encoding)
generate_config_php.stdin.close()
for line in generate_config_php.stdout.read(): 
    fichier.write(line)
droit_data= subprocess.Popen(["chown", "-R","www-data:www-data", "/var/www/html/wordpress/wp-config.php"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
droit_data.stdin.write(droit_data.stdout.encoding)
droit_data.stdin.close()
for line in droit_data.stdout.read():
    fichier.write(line)

droit_600= subprocess.Popen(["chmod", "600", "/var/www/html/wordpress/wp-config.php"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
droit_600.stdin.write(droit_600.stdout.encoding)
droit_600.stdin.close()
for line in droit_600.stdout.read():
    fichier.write(line)

droit_755= subprocess.Popen(["chmod","-R", "755", "$(find /var/www/html/wordpress/ -type d)"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
droit_755.stdin.write(droit_755.stdout.encoding)
droit_755.stdin.close()
for line in droit_755.stdout.read():
    fichier.write(line)

droit_644= subprocess.Popen(["chmod","-R", "644", "$(find /var/www/html/wordpress/ -type f)"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
droit_644.stdin.write(droit_644.stdout.encoding)
droit_644.stdin.close()
for line in droit_644.stdout.read():
    fichier.write(line)

## Recuperation de la base de donnée de wordpress
fichier.write("injection de la base de donnée wordpress dans la base de donnée cree auparavant  \n \n  ")
print("injection de la base de donnée wordpress dans la base de donnée cree auparavant \n \n   ")
create_data_base= subprocess.Popen(["wp", "--allow-root","db", "create"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
create_data_base.stdin.write(create_data_base.stdout.encoding)
create_data_base.stdin.close()
for line in create_data_base.stdout.read():
    fichier.write(line)

## Supprission du fichier /var/www/html/wordpress/wp-config-sample.php qui a fait office d'exemple pour le fichier wp-config.php
fichier.write("Supprission du fichier /var/www/html/wordpress/wp-config-sample.php   \n \n  ")
print("Supprission du fichier /var/www/html/wordpress/wp-config-sample.php \n \n  ")
delete_config_sample= subprocess.Popen(["rm", "-f","/var/www/html/wordpress/wp-config-sample.php"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
delete_config_sample.stdin.write(delete_config_sample.stdout.encoding)
delete_config_sample.stdin.close()
for line in delete_config_sample.stdout.read():
    fichier.write(line)

## Creation du premier site de l'application installer 
fichier.write("Creation du site de l'application \n \n  ")
print("Creation du site de l'application \n \n  ")
install_site= subprocess.Popen(["wp", "--allow-root","core", "install","--url=http://192.168.1.200/", "--title='Projet_6'", "--admin_user=admin", "--admin_password=passwd_wp","--admin_email=admin@gmail.fr",] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
install_site.stdin.write(install_site.stdout.encoding)
install_site.stdin.close()
for line in install_site.stdout.read(): 
    fichier.write(line)
## Ajouter un noueau theme 
new_theme= subprocess.Popen(["wp", "--allow-root","theme", "install","twentytwentytwo", "--activate"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
new_theme.stdin.write(new_theme.stdout.encoding)
new_theme.stdin.close()
for line in new_theme.stdout.read(): 
    fichier.write(line)

fichier.write("Fin de l'installation et de la configuration de wordpress\n \n  ")
print("Fin de l'installation et de la configuration de wordpress \n \n  ")



fichier.write("Fin de l'installation de l'environnement \n \n  ")
fichier.close()
print("Fin de l'installation de l'environnement ")
