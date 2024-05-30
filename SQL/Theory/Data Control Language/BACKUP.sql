-- We can backup either the entire database or certain tables, on Server->Data Export
-- Then we choose the database and the tables we want to backup. Left to `Select Views` we
--   can see a dropdown menu in which we should choose `Dump Stracture and Data`
-- Then we need to select all the ticks bellow, for procedures, triggers and events

-- Then we have two option. Either save each table on a file, or save the entire database
--   on a single file

-- At the end, check the last boxes and hit `Start Export`
-- The default storage for the backup is on 'Documents'

-- To add the database to our schemas we go to Server->Data Import and choose the second dot
--   `Import from Self-Contained File`
-- Then we create a default traget schema and on `Import Progress` we hit `Start Import` and we
--   are ready to go
