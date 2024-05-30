-- DCL stands for 'Data Cotrol Language' and through it we can:
-- 1) Monitor the status and the how operational is the server
-- 2) Create, delete and modify users
-- 3) Log certain actions that are being done to the database
-- 4) Modify the system variables
-- 5) Backup the database

-- To monitor the system via the Workbench we go to Server->Server Status
-- We can find information for our server, if our server is up, the traffic, cpu load, 
--   the users that are connected and other usefull data

-- On Server->Client Connections we can see details for each user that is connected to
--   the database. Details such us name, queries they are running, their state etc. We
--   can also kill quieries and disconnect a user from the server 

-- We can reboot the server using: Server->Startup/Shutdown

-- On Server->Status and System Variables we can see all the system variables and their
--   values, for changing and modifying if something about the connection break
