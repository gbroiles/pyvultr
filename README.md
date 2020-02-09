# pyvultr

Python 3 implementation of command line interface to Vultr.com API.

Environment variable VULTRAPI must be set to your Vultr API. In Bash, for example:

    export VULTRAPI="blahblahblah"

Examples:

    vtpy list server -- list all servers in your account
    vtpy list active -- list all active servers in your account
    vtpy list plans -- list available plans w/ locations
    vtpy list allplans -- list all plans, even when no locations offer them right now
    vypy list locations -- list datacenter/locations
    vtpy list ssh -- list SSH keys
    vtpy list fw -- list firewall IDs
    vtpy list os -- list available OSes
    vtpy kill <SUBID> [<SUBID>] -- DESTROY one or more servers (THIS IS DESTRUCTIVE, THERE IS NO 'CONFIRM' STEP, BE CAREFUL)
    vtpy status <SUBID> [<SUBID>] -- get detailed status for one or more server
    vtpy create <datacenter> <VPS plan> <OS ID> <Private Net?> <SSHKey ID> <Firewall ID> [hostname] [tag(s] -- create new server
    vtpy copy <SUBID> [new hostname] -- create new server by duplicating an existing server configuration
