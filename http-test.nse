--The Head
local stdnse = require "stdnse"
local shortport = require "shortport"

description = [[

]]
---
-- @usage nmap --script http-webmin-helloworld.nse <target>


catagories = {"safe", "default"}
author = "Joshua M."

--The Rules
portrule = shortport.port_or_service ()

--The Action
action = function(host, port)

end