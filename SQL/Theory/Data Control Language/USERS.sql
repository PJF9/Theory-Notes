-- We can create users, meaning connections that have certain privileges on the
--   database. We can also grant or revoke privilages after creating, meaning to
--   give of take some actions that they can perform to the server

-- Server->Users and Privilages

-- To create a user we click on `Add Account`. Then a new window has opened and we
--   need to specify the user's information. Note that we can limit the locations
--   that the user have access to the server. By '%' we allow all locations
-- After that we hit apply and the new user has been created.

-- In the tab `Account Limits` we can add some limitations, such us the max queries
--   the user can have, the max connections per hour and the max connections at the
--   same time. By setting some of them 0 means no limitation

-- In `Administrative Roles` we can specify the exact administrative command and keywords 
--   that the new user can perform.

-- Finally in `Schema Privilages` we can create a new entry and specify the view level of
--   the user. We can also specify the commands he/she can use

-- After that hit 'Apply' and the new user has succesfully created

-- To enter as this user we create a new connection at the main screen of the Workbench
--   go to new connection, add the name, the username and then `Test Connection` and we are
--   ready to go.











