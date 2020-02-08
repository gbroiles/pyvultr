# pyvultr

Python 3 implementation of command line interface to Vultr.com API.

Environment variable VULTRAPI must be set to your Vultr API, for Bash try:

    export VULTRAPI="blahblahblah"

Examples:

    vtpy list server -- list all servers in your account
    vtpy list active -- list all active servers in your account
    vtpy list plans -- list available plans w/ locations
    vtpy list allplans -- list all plans, even when no locations offer them right now
    vypy list locations -- list datacenter/locations
    vtpy kill <SUBID> [<SUBID>] -- DESTROY one or more servers (THIS IS DESTRUCTIVE, THERE IS NO 'CONFIRM' STEP, BE CAREFUL)
