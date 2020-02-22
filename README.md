# HWID-Auth-System
[Note this is still very basic, but lots of features OTW!]

A Python API to verify a valid HWID with hwids stored in a MySQL Database

Based off of @xannyyyy 's https://github.com/xannyyyy/Hwid-Auth-Verify

Instead of HWIDs stored in a text file, they are now stored in a MySQL DB.

Here is the SQL query to run to create the table.
``CREATE TABLE `hwid` (
  `hwid` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;``

Edit Webapp.py to config your MySQL Database. 
