import monitoring_thread
import os
import paramiko

# monitoring_thread.main(os.getcwd())

# import paramiko
 
# Create object of SSHClient and 
# connecting to SSH
ssh = paramiko.SSHClient()
 
# Adding new host key to the local 
# HostKeys object(in case of missing)
# AutoAddPolicy for missing host key to be set before connection setup.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
ssh.connect('172.21.174.83', port=22, username='atharva',
            password='pass@123', timeout=3)
 
# Execute command on SSH terminal 
# using exec_command
stdin, stdout1, stderr = ssh.exec_command('top -b -n 1 | grep %Cpu')
stdin, stdout2, stderr = ssh.exec_command("top -b -n 1 | grep 'MiB Mem'")
print(stdout1.read())
print(stdout2.read())