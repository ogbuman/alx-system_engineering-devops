from fabric.api import *

env.hosts = ["18.209.225.63", "100.25.17.109"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


def do_install_mysql():
    """ Install MySQL """
    sudo("apt update")
    sudo("apt install -y mysql-server-5.7")
    sudo("mysql --version")
    sudo("ufw allow mysql")


def do_create_mysql_user(username, admin_password, password):
    """ Create MySQL user """
    create_user_cmd = f"CREATE USER IF NOT EXISTS '{username}'@'localhost' IDENTIFIED BY '{password}';"
    grant_permissions_cmd = f"GRANT REPLICATION CLIENT ON *.* TO '{username}'@'localhost';"
    mysql_cmd = f"mysql -u root -p{admin_password} -e \"{create_user_cmd} {grant_permissions_cmd}\""
    run(mysql_cmd, pty=True)
    test_cmd = f"mysql -u root -p{admin_password} -e \"SELECT user, host FROM mysql.user;\""
    run(command=test_cmd, pty=True)


def do_create_database(admin_password, database_name):
    """ Create MySQL database """
    create_database_cmd = f"CREATE DATABASE IF NOT EXISTS {database_name};"
    mysql_cmd = f"mysql -u root -p{admin_password} -e \"{create_database_cmd}\""
    run(mysql_cmd, pty=True)
    test_cmd = f"mysql -u root -p{admin_password} -e \"SHOW DATABASES;\""
    run(command=test_cmd, pty=True)


def do_create_table_and_insert(admin_password, user, database_name, user_password, table_name):
    """ Create MySQL table and insert data """
    use_database_cmd = f"USE {database_name};"
    create_table_cmd = f"CREATE TABLE IF NOT EXISTS nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256));"
    insert_data_cmd = f"INSERT INTO nexus6 (name) VALUES ('Davies'), ('John'), ('Jo');"
    grant_select_cmd = f"GRANT SELECT ON {database_name}.{table_name} TO '{user}'@'localhost';"
    mysql_cmd = f"mysql -u root -p{admin_password} -e \"{use_database_cmd} {create_table_cmd} {insert_data_cmd} {grant_select_cmd}\""
    run(mysql_cmd, pty=True)
    test_cmd = f"mysql -u {user} -p{user_password} -e \"{use_database_cmd} SELECT * FROM nexus6;\""
    run(command=test_cmd, pty=True)


def do_create_replica_user(admin_password, replica_password, holberton_user):
    """ Create MySQL replica user """
    create_replica_user_cmd = f"CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY '{replica_password}';"
    grant_replica_cmd = f"GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';"
    hbtn_grant_select_user_cmd = f"GRANT SELECT ON mysql.user TO '{holberton_user}'@'localhost';"
    mysql_cmd = f"mysql -u root -p{admin_password} -e \"{create_replica_user_cmd} {grant_replica_cmd} {hbtn_grant_select_user_cmd}\""
    run(mysql_cmd, pty=True)
    test_cmd = f"mysql -u root -p{admin_password} -e \"SELECT user, host FROM mysql.user;\""
    run(command=test_cmd, pty=True)
