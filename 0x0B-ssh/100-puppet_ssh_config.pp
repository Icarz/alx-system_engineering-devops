file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',    # Path to the SSH client configuration file
  line  => 'PasswordAuthentication no',  # Disable password authentication
  match => '^#PasswordAuthentication',  # Ensure the correct line is updated
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',      # Path to the SSH client configuration file
  line  => 'IdentityFile ~/.ssh/school',  # Specify the private key to use
  match => '^#IdentityFile',            # Ensure the correct line is updated
}
