# Configuration Management with Puppet

This project demonstrates the use of Puppet for configuration management. It includes tasks to create files, install packages, and execute commands using Puppet manifests.

## Tasks

1. **Create a File**: Creates a file `/tmp/school` with specific properties.
2. **Install a Package**: Installs Flask version 2.1.0 using pip3.
3. **Execute a Command**: Kills processes named `killmenow` using the `exec` resource.

## How to Use
- Ensure Puppet 5.5 and puppet-lint 2.1.1 are installed.
- Run `puppet-lint` to check manifest syntax.
- Apply manifests using `puppet apply <filename>.pp`.

## Requirements
- Ubuntu 20.04 LTS
- Puppet 5.5
- puppet-lint 2.1.1
