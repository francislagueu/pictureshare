PictureShare
============

Django picture sharing site

Jerry Ma (ma127)

Yifan Yin (yin6)

Features
--------

- Accounts
  
  - Registration
  - E-mail activiation
  - Login
  - Change password
  - Forgot password

- Browsing

  - No authentication: browse public photos and albums
  - Authentication: browse most recent public AND user photos and albums

- Album/Photo Viewing & Management
  
  - Will only show album/photo if public OR user's
  - Timestamps and titles for albums and photos
  - Button to delete album/photo
  - Button to change privacy settings
  - Upload photo page
  - Add album page
  - Image files of private photos are inaccessible until authenticated with
    user's account
  - Albums and photos have unique privacy settings - a public album can 
    include private pictures, which will not be shown in the public view
  - Photos can be in multiple albums

- Search Engine: basic search engine finds albums/photos where the title or
  author username matches the query (sorted by date). Privacy filters are
  built-in.
  
Development
-----------

This site is currently being developed on a Micro AWS EC2 Instance (Ubuntu),
backed by an Amazon RDS Instance (MySQL Community Edition). The development
server is linked by default to ec.ohofzero.com:8000 and may not be up at
all times.
